import sys
import re
import numpy as np
from scipy.special import sph_harm, genlaguerre
from scipy.ndimage import gaussian_filter
from skimage.measure import marching_cubes
import matplotlib
try:
    matplotlib.use('Qt5Agg')
except:
    pass

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.colors import LinearSegmentedColormap

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QFrame, QVBoxLayout, QHBoxLayout, 
                               QGridLayout, QGroupBox, QLabel, QComboBox, 
                               QSpinBox, QDoubleSpinBox, QPushButton, QWidget, 
                               QPlainTextEdit, QMessageBox)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1250, 850)
        
        self.verticalLayout = QVBoxLayout(Frame)
        
        #控制面板
        self.control_group = QGroupBox(Frame)
        self.control_group.setTitle(u"杂化轨道参数设置")
        self.control_layout = QGridLayout(self.control_group)
        
        # 1. 杂化类型
        self.label_hybrid_type = QLabel(u"杂化类型:", self.control_group)
        self.control_layout.addWidget(self.label_hybrid_type, 0, 0)
        
        self.combo_hybrid_type = QComboBox(self.control_group)
        self.combo_hybrid_type.addItems(["sp杂化", "sp2杂化", "sp3杂化 (等性)", "sp3杂化 (水/不等性)", "sp3d2杂化", "sp3d3杂化", "自定义杂化"])
        self.control_layout.addWidget(self.combo_hybrid_type, 0, 1)
        
        # 2. 可视化类型
        self.label_viz_type = QLabel(u"可视化类型:", self.control_group)
        self.control_layout.addWidget(self.label_viz_type, 1, 0)
        self.combo_viz_type = QComboBox(self.control_group)
        self.combo_viz_type.addItems(["3D等值面可视化", "电子云可视化", "截面图可视化"])
        self.control_layout.addWidget(self.combo_viz_type, 1, 1)
        
        # 3. 空间范围
        self.label_space = QLabel(u"空间范围 (a0):", self.control_group)
        self.control_layout.addWidget(self.label_space, 2, 0)
        self.spin_space = QSpinBox(self.control_group)
        self.spin_space.setRange(5, 100)
        self.spin_space.setValue(18) 
        self.control_layout.addWidget(self.spin_space, 2, 1)
        
        # 4. 网格点数
        self.label_num_points = QLabel(u"网格精度 (点/轴):", self.control_group)
        self.control_layout.addWidget(self.label_num_points, 3, 0)
        self.spin_num_points = QSpinBox(self.control_group)
        self.spin_num_points.setRange(30, 200)
        self.spin_num_points.setValue(60)
        self.control_layout.addWidget(self.spin_num_points, 3, 1)

        # 5. 自定义矩阵输入区域
        self.group_custom = QGroupBox(u"自定义矩阵配置", self.control_group)
        self.layout_custom = QVBoxLayout(self.group_custom)
        
        self.label_basis = QLabel(u"基组定义 (请按顺序对应矩阵列):")
        self.combo_basis_set = QComboBox()
        self.combo_basis_set.addItems([
            "sp基组: s, pz",
            "sp2基组: s, px, py",
            "sp3基组: s, px, py, pz",
            "sp3d2基组: s, px, py, pz, dx2-y2, dz2",
            "sp3d3基组: s, px, py, pz, dz2, dx2-y2, dxy"
        ])
        self.layout_custom.addWidget(self.label_basis)
        
        self.label_matrix = QLabel(u"系数矩阵 (支持直接粘贴 Numpy 数组或纯数字):")
        self.input_matrix = QPlainTextEdit()
        self.input_matrix.setPlaceholderText("[[0.707, 0.707], [0.707, -0.707]]")
        self.input_matrix.setMaximumHeight(100)
        self.layout_custom.addWidget(self.label_matrix)
        self.layout_custom.addWidget(self.input_matrix)
        
        self.control_layout.addWidget(self.group_custom, 4, 0, 1, 2)
        
        # 6. 动态参数区域
        self.widget_params = QWidget(self.control_group)
        self.layout_params = QVBoxLayout(self.widget_params)
        self.layout_params.setContentsMargins(0,0,0,0)
        
        # 轨道选择
        self.widget_orbital_sel = QWidget()
        self.layout_orb_sel = QHBoxLayout(self.widget_orbital_sel)
        self.layout_orb_sel.setContentsMargins(0,0,0,0)
        self.label_orb_sel = QLabel(u"选择轨道:")
        self.combo_orbital_selection = QComboBox()
        self.layout_orb_sel.addWidget(self.label_orb_sel)
        self.layout_orb_sel.addWidget(self.combo_orbital_selection)
        self.layout_params.addWidget(self.widget_orbital_sel)
        
        # 阈值
        self.widget_thresh = QWidget()
        self.layout_thresh = QHBoxLayout(self.widget_thresh)
        self.layout_thresh.setContentsMargins(0,0,0,0)
        self.label_threshold = QLabel(u"显示阈值:")
        self.spin_threshold = QDoubleSpinBox()
        self.spin_threshold.setRange(0.0001, 0.5)
        self.spin_threshold.setValue(0.01) # 默认阈值降低
        self.spin_threshold.setSingleStep(0.005)
        self.spin_threshold.setDecimals(4)
        self.layout_thresh.addWidget(self.label_threshold)
        self.layout_thresh.addWidget(self.spin_threshold)
        self.layout_params.addWidget(self.widget_thresh)
        
        # 电子云点数
        self.widget_points = QWidget()
        self.layout_points = QHBoxLayout(self.widget_points)
        self.layout_points.setContentsMargins(0,0,0,0)
        self.label_total_points = QLabel(u"采样点数:")
        self.spin_total_points = QSpinBox()
        self.spin_total_points.setRange(1000, 500000)
        self.spin_total_points.setValue(30000)
        self.layout_points.addWidget(self.label_total_points)
        self.layout_points.addWidget(self.spin_total_points)
        self.layout_params.addWidget(self.widget_points)
        
        self.control_layout.addWidget(self.widget_params, 5, 0, 1, 2)
        
        # 7. 信息显示
        self.label_info = QLabel(u"就绪", self.control_group)
        self.control_layout.addWidget(self.label_info, 6, 0, 1, 2)
        
        # 8. 计算按钮
        self.button_calculate = QPushButton(u"计算并可视化", self.control_group)
        self.button_calculate.setMinimumHeight(45)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.button_calculate.setFont(font)
        self.control_layout.addWidget(self.button_calculate, 7, 0, 1, 2)
        
        self.verticalLayout.addWidget(self.control_group)
        
        #绘图区域
        self.plot_layout = QVBoxLayout()
        self.verticalLayout.addLayout(self.plot_layout)

class hybrid_orbital_frame(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.hybrid_orbitals = []
        self.prob_densities = []
        self.X, self.Y, self.Z_grid = None, None, None
        
        # 预定义颜色
        self.colors = [
            (1, 0.2, 0.2), (0.2, 1, 0.2), (0.2, 0.4, 1), 
            (1, 1, 0), (0, 1, 1), (1, 0, 1), 
            (1, 0.6, 0), (0.6, 0, 0.6)
        ]

        self.init_canvas()
        
        self.combo_hybrid_type.currentTextChanged.connect(self.on_hybrid_type_changed)
        self.combo_viz_type.currentTextChanged.connect(self.update_ui_visibility)
        self.button_calculate.clicked.connect(self.calculate_and_plot)
        
        # 初始化状态
        self.on_hybrid_type_changed(self.combo_hybrid_type.currentText())
        self.update_ui_visibility()

    def init_canvas(self):
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot_layout.addWidget(self.toolbar)
        self.plot_layout.addWidget(self.canvas)

  
    def on_hybrid_type_changed(self, text):
        # 判定当前是否为自定义模式
        is_custom = ("自定义" in text)

        self.group_custom.setVisible(True)
        self.group_custom.setEnabled(is_custom)
        
        # 交互优化：非自定义模式下显示提示
        if not is_custom:
            self.input_matrix.setPlainText(f"当前为【{text}】模式，使用内置矩阵。\n\n如需输入自定义矩阵，请在上方下拉框选择\n'自定义杂化'。")
            self.input_matrix.setStyleSheet("background-color: #f0f0f0; color: #555;")
        else:
            current_text = self.input_matrix.toPlainText()
            if "当前为" in current_text and "使用内置矩阵" in current_text:
                self.input_matrix.clear()
            self.input_matrix.setStyleSheet("background-color: #ffffff; color: #000;")

    def update_ui_visibility(self):
        viz_type = self.combo_viz_type.currentText()
        is_cloud = "电子云" in viz_type
        is_section = "截面图" in viz_type
        
        self.widget_orbital_sel.setVisible(is_cloud or is_section)
        self.widget_points.setVisible(is_cloud)
        self.widget_thresh.setVisible(not is_section)

    def radial_wavefunction(self, n, l, r, Z=1):
        """计算径向部分 R(r)"""
        # rho = 2Zr / n
        rho = 2.0 * Z * r / n
        # Laguerre 多项式
        L = genlaguerre(n - l - 1, 2 * l + 1)(rho)
        return np.exp(-rho / 2.0) * (rho ** l) * L

    def real_spherical_harmonic(self, l, m, theta, phi):
        """
        计算实数球谐函数 

        """
        Y_complex = sph_harm(abs(m), l, phi, theta)
        
        if m == 0:
            return Y_complex.real
        elif m > 0:
            
            return np.sqrt(2) * ((-1)**m) * Y_complex.real
        else:
            
            return np.sqrt(2) * ((-1)**m) * Y_complex.imag

    def compute_atomic_orbital(self, Z, n, l, m, X, Y, Z_grid):
        """计算完整的原子轨道波函数"""
        r = np.sqrt(X**2 + Y**2 + Z_grid**2)
        # 防止除零
        with np.errstate(divide='ignore', invalid='ignore'):
            theta = np.arccos(Z_grid / (r + 1e-12))
            phi = np.arctan2(Y, X)
        
        R = self.radial_wavefunction(n, l, r, Z)
        Y_lm = self.real_spherical_harmonic(l, m, theta, phi)
        
        psi = R * Y_lm
        psi = np.nan_to_num(psi) # 处理原点奇点
        return psi

    def parse_custom_matrix(self):
        """
        支持: 
        [[1,0],[0,1]] 
        1 0; 0 1
        1,0
        0,1
        """
        text = self.input_matrix.toPlainText().strip()
        if not text:
            raise ValueError("矩阵输入为空")
        
        # 将 [ ] , 替换为空格
        clean_text = text.replace('[', ' ').replace(']', ' ').replace(',', ' ')
        
        rows_str = re.split(r'[;\n]', clean_text)
        
        matrix_data = []
        for r in rows_str:
            if not r.strip(): continue
            # 提取该行中的所有浮点数
            cols = [float(x) for x in r.split()]
            if cols:
                matrix_data.append(cols)
                
        if not matrix_data:
            raise ValueError("无法解析出有效数值")
            
        # 3. 检查列数一致性
        cols_len = len(matrix_data[0])
        for r in matrix_data:
            if len(r) != cols_len:
                raise ValueError(f"矩阵行列不齐：检测到 {len(r)} 列，预期 {cols_len} 列")
                
        return np.array(matrix_data)

    def get_parameters(self, name):
        """返回 (Z, Basis_Config, Matrix)"""
        

        if name == "sp杂化":
            # Basis: 2s, 2pz
            config = [
                [1, 2, 0, 0], # 2s
                [1, 2, 1, 0]  # 2pz
            ]
            matrix = np.array([
                [1/np.sqrt(2),  1/np.sqrt(2)],
                [1/np.sqrt(2), -1/np.sqrt(2)]
            ])
            return config, matrix

        elif name == "sp2杂化":
            # Basis: 2s, 2px, 2py
            config = [
                [1, 2, 0, 0],  # 2s
                [1, 2, 1, 1],  # 2px
                [1, 2, 1, -1]  # 2py
            ]
            matrix = np.array([
                [1/np.sqrt(3), np.sqrt(2/3), 0],
                [1/np.sqrt(3), -1/np.sqrt(6), 1/np.sqrt(2)],
                [1/np.sqrt(3), -1/np.sqrt(6), -1/np.sqrt(2)]
            ])
            return config, matrix

        elif name == "sp3杂化 (等性)":
            # Basis: 2s, 2px, 2py, 2pz
            config = [
                [1, 2, 0, 0],  # 2s
                [1, 2, 1, 1],  # 2px
                [1, 2, 1, -1], # 2py
                [1, 2, 1, 0]   # 2pz
            ]
            matrix = np.array([
                [0.5, 0.5, 0.5, 0.5],
                [0.5, 0.5, -0.5, -0.5],
                [0.5, -0.5, 0.5, -0.5],
                [0.5, -0.5, -0.5, 0.5]
            ])
            return config, matrix
            
        elif name == "sp3杂化 (水/不等性)":
            config = [
                [1, 2, 0, 0], [1, 2, 1, 1], [1, 2, 1, -1], [1, 2, 1, 0]
            ]
            matrix = np.array([
                [0.61, 0.00, 0.52, 0.60],
                [0.61, 0.00, -0.52, 0.60],
                [0.51, 0.77, 0.00, -0.38],
                [0.51, -0.77, 0.00, -0.38]
            ])
            return config, matrix

        elif name == "sp3d2杂化":
            # Config Ref: s, px, py, pz, dx2-y2, dz2
            # m map: px(1), py(-1), pz(0), dx2-y2(2), dz2(0)
            config = [
                [1, 3, 0, 0],  # 3s
                [1, 3, 1, 1],  # 3px
                [1, 3, 1, -1], # 3py
                [1, 3, 1, 0],  # 3pz
                [1, 3, 2, 2],  # 3dx2-y2
                [1, 3, 2, 0]   # 3dz2
            ]
            
            s = 1 / np.sqrt(6)
            p = 1 / np.sqrt(2)
            dz2_z = 2 / np.sqrt(12) 
            dz2_xy = -1 / np.sqrt(12)
            d_x2y2 = 0.5

            matrix = np.array([   
                [s,  0,   0,   p,   0,       dz2_z],
                [s,  0,   0,  -p,   0,       dz2_z],
                [s,  p,   0,   0,   d_x2y2,  dz2_xy],
                [s, -p,   0,   0,   d_x2y2,  dz2_xy],
                [s,  0,   p,   0,  -d_x2y2,  dz2_xy],
                [s,  0,  -p,   0,  -d_x2y2,  dz2_xy]
            ])
            return config, matrix

        elif name == "sp3d3杂化":
            config = [
                [1, 4, 0, 0],   # 4s
                [1, 4, 1, 1],   # 4px
                [1, 4, 1, -1],  # 4py
                [1, 4, 1, 0],   # 4pz
                [1, 4, 2, 0],   # 4dz2
                [1, 4, 2, 2],   # 4dx2-y2
                [1, 4, 2, -2]   # 4dxy (m=-2)
            ]
            matrix = np.array([
                [ 0.411, -0. ,    0. ,    0.707,  0.575, -0. ,   -0.   ],
                [ 0.411,  0.    ,-0.   , -0.707, 0.575 , 0.  ,  -0.   ],
                [ 0.364,  0.632 , 0.  ,  -0.  ,  -0.26 ,  0.632 ,-0.   ],
                [ 0.364,  0.195 , 0.602 , 0.  ,  -0.26 , -0.512 , 0.372],
                [ 0.364, -0.512,  0.372, -0.  ,  -0.26 ,  0.195 ,-0.602],
                [ 0.364, -0.512, -0.372,  0.   , -0.26  , 0.195 , 0.602], 
                [ 0.364,  0.195, -0.602,  0.   , -0.26 , -0.512 ,-0.372]
            ])
            return config, matrix
            
        return [], None

    def get_custom_basis_config(self):
        """为自定义模式生成基组列表"""
        idx = self.combo_basis_set.currentIndex()
        # "sp基组: s, pz",
        if idx == 0: return [[1,2,0,0], [1,2,1,0]]
        # "sp2基组: s, px, py",
        if idx == 1: return [[1,2,0,0], [1,2,1,1], [1,2,1,-1]]
        # "sp3基组: s, px, py, pz",
        if idx == 2: return [[1,2,0,0], [1,2,1,1], [1,2,1,-1], [1,2,1,0]]
        # "sp3d2基组: s, px, py, pz, dx2-y2, dz2",
        if idx == 3: return [[1,3,0,0], [1,3,1,1], [1,3,1,-1], [1,3,1,0], [1,3,2,2], [1,3,2,0]]
        # "sp3d3基组: s, px, py, pz, dz2, dx2-y2, dxy"
        if idx == 4: return [[1,4,0,0], [1,4,1,1], [1,4,1,-1], [1,4,1,0], [1,4,2,0], [1,4,2,2], [1,4,2,-2]]
        return []

    def calculate_and_plot(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            # 1. 准备参数
            h_type = self.combo_hybrid_type.currentText()
            space = self.spin_space.value()
            N = self.spin_num_points.value()
            
            # 2. 获取配置
            if h_type == "自定义杂化":
                config = self.get_custom_basis_config()
                matrix = self.parse_custom_matrix()
            else:
                config, matrix = self.get_parameters(h_type)
            
            # 校验
            if matrix is None or len(config) == 0:
                raise ValueError("配置加载失败")
            if matrix.shape[1] > len(config):
                raise ValueError(f"矩阵列数({matrix.shape[1]}) 超过基组数量({len(config)})")
                
            # 3. 补全矩阵 (如果输入的矩阵列数少于基组数，补0)
            full_matrix = np.zeros((matrix.shape[0], len(config)))
            full_matrix[:, :matrix.shape[1]] = matrix
            
            # 4. 生成网格
            x = np.linspace(-space, space, N, dtype=np.float32)
            y = np.linspace(-space, space, N, dtype=np.float32)
            z = np.linspace(-space, space, N, dtype=np.float32)
            self.X, self.Y, self.Z_grid = np.meshgrid(x, y, z, indexing='ij')
            
            # 5. 计算基组轨道 (Vectorized)
            # shape: (n_basis, N, N, N)
            basis_orbitals = np.zeros((len(config), N, N, N), dtype=np.float32)
            
            for i, (Z, n, l, m) in enumerate(config):
                # 优化: 仅当该列系数不全为0时计算
                if np.any(full_matrix[:, i] != 0):
                    basis_orbitals[i] = self.compute_atomic_orbital(Z, n, l, m, self.X, self.Y, self.Z_grid)
            
            # 6. 线性组合 (Matrix Multiplication)
            # (n_hybrid, n_basis) dot (n_basis, N,N,N) -> (n_hybrid, N,N,N)
            self.hybrid_orbitals = np.tensordot(full_matrix, basis_orbitals, axes=(1, 0))
            
            # 7. 计算概率密度
            self.prob_densities = self.hybrid_orbitals ** 2
            
            # 归一化 (相对值，用于绘图)
            global_max = np.max(self.prob_densities)
            if global_max > 1e-12:
                self.prob_densities /= global_max
                
            # 8. 更新UI下拉框
            curr_idx = self.combo_orbital_selection.currentIndex()
            self.combo_orbital_selection.clear()
            for i in range(len(self.prob_densities)):
                self.combo_orbital_selection.addItem(f"杂化轨道 {i+1}")
            if curr_idx >= 0 and curr_idx < len(self.prob_densities):
                self.combo_orbital_selection.setCurrentIndex(curr_idx)
                
            self.label_info.setText(f"计算完成: {len(config)}个原子轨道 -> {len(self.hybrid_orbitals)}个杂化轨道")
            self.refresh_plot()
            
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))
        finally:
            QApplication.restoreOverrideCursor()

    # 绘图逻辑
    

    def refresh_plot(self):
        if self.X is None: return
        self.fig.clear()
        
        viz_type = self.combo_viz_type.currentText()
        
        if "3D等值面" in viz_type:
            self.plot_isosurfaces()
        elif "电子云" in viz_type:
            self.plot_electron_cloud()
        elif "截面图" in viz_type:
            self.plot_cross_sections()
            
        self.canvas.draw()

    def plot_isosurfaces(self):
        ax = self.fig.add_subplot(111, projection='3d')
        threshold = self.spin_threshold.value()
        space = self.spin_space.value()
        
        for i, prob in enumerate(self.prob_densities):
            # 高斯平滑使表面更光滑
            smoothed = gaussian_filter(prob, sigma=0.8)
            try:
                verts, faces, _, _ = marching_cubes(smoothed, level=threshold)
                # 转换坐标
                scale = (2*space) / (prob.shape[0]-1)
                verts = verts * scale - space
                
                color = self.colors[i % len(self.colors)]
                ax.plot_trisurf(verts[:,0], verts[:,1], faces, verts[:,2], 
                                color=color, alpha=0.35, shade=True)
            except:
                pass
                
        ax.set_xlim(-space, space); ax.set_ylim(-space, space); ax.set_zlim(-space, space)
        ax.set_title(f"3D等值面 (Iso={threshold})")

    def plot_electron_cloud(self):
        idx = self.combo_orbital_selection.currentIndex()
        if idx < 0: return
        
        ax = self.fig.add_subplot(111, projection='3d')
        wf = self.hybrid_orbitals[idx]
        prob = self.prob_densities[idx]
        
        target_points = self.spin_total_points.value()
        threshold = self.spin_threshold.value() * 0.1 # 电子云需要更低阈值
        
        # 快速向量化采样
        N = prob.shape[0]
        batch = int(target_points * 10)
        
        ix = np.random.randint(0, N, batch)
        iy = np.random.randint(0, N, batch)
        iz = np.random.randint(0, N, batch)
        
        p_val = prob[ix, iy, iz]
        rand = np.random.random(batch)
        
        # 蒙特卡洛接受
        mask = (rand < p_val) & (p_val > threshold)
        
        vx, vy, vz = ix[mask], iy[mask], iz[mask]
        
        # 截取数量
        if len(vx) > target_points:
            vx, vy, vz = vx[:target_points], vy[:target_points], vz[:target_points]
            
        # 坐标转换
        space = self.spin_space.value()
        step = (2*space)/(N-1)
        px = -space + vx*step
        py = -space + vy*step
        pz = -space + vz*step
        
        # 相位着色
        phase = wf[vx, vy, vz]
        c = np.where(phase > 0, 'r', 'b')
        
        ax.scatter(px, py, pz, c=c, s=0.2, alpha=0.6)
        ax.set_xlim(-space, space); ax.set_ylim(-space, space); ax.set_zlim(-space, space)
        ax.set_title(f"电子云 (红+, 蓝-)")

    def plot_cross_sections(self):
        idx = self.combo_orbital_selection.currentIndex()
        if idx < 0: return
        
        prob = self.prob_densities[idx]
        N = prob.shape[0]
        mid = N // 2
        space = self.spin_space.value()
        extent = [-space, space, -space, space]
        
        cmap = LinearSegmentedColormap.from_list("custom", ["#000000", "#1a0040", "#8000ff", "#ffffff"])
        
        axes = self.fig.subplots(1, 3)
        
        # YZ (X=0)
        axes[0].imshow(prob[mid,:,:].T, origin='lower', extent=extent, cmap=cmap)
        axes[0].set_title("YZ平面 (x=0)")
        axes[0].set_xlabel("Y"); axes[0].set_ylabel("Z")
        
        # XZ (Y=0)
        axes[1].imshow(prob[:,mid,:].T, origin='lower', extent=extent, cmap=cmap)
        axes[1].set_title("XZ平面 (y=0)")
        axes[1].set_xlabel("X"); axes[1].set_ylabel("Z")
        
        # XY (Z=0)
        axes[2].imshow(prob[:,:,mid].T, origin='lower', extent=extent, cmap=cmap)
        axes[2].set_title("XY平面 (z=0)")
        axes[2].set_xlabel("X"); axes[2].set_ylabel("Y")


if __name__ == "__main__":
    # 高分屏适配
    os_scale = getattr(Qt, 'AA_EnableHighDpiScaling', None)
    if os_scale: QCoreApplication.setAttribute(os_scale)
    
    app = QApplication(sys.argv)
    win = hybrid_orbital_frame()
    win.setWindowTitle("杂化轨道可视化 (Pro Fix)")
    win.show()
    sys.exit(app.exec())