from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtWidgets import QSpinBox, QComboBox, QGroupBox, QGridLayout, QScrollArea, QCheckBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm, genlaguerre, gammaln
from skimage.measure import marching_cubes
from scipy.ndimage import gaussian_filter
from matplotlib.colors import LinearSegmentedColormap

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class hydrogen_orbital_frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_initial_params()
        # 初始化后触发一次参数更新以同步Space
        self.on_parameters_changed()
        self.update_visualization()
        
    def setup_ui(self):
        # 主布局
        main_layout = QVBoxLayout(self)
        
        # 创建滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QtWidgets.QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # 控制面板
        control_group = QGroupBox("轨道参数设置")
        control_layout = QGridLayout()
        
        # 主量子数 n
        control_layout.addWidget(QLabel("主量子数 n:"), 0, 0)
        self.n_spinbox = QSpinBox()
        self.n_spinbox.setRange(1, 20)
        self.n_spinbox.setValue(3) # 默认值
        self.n_spinbox.valueChanged.connect(self.on_parameters_changed)
        control_layout.addWidget(self.n_spinbox, 0, 1)
        
        # 角量子数 l
        control_layout.addWidget(QLabel("角量子数 l:"), 1, 0)
        self.l_spinbox = QSpinBox()
        self.l_spinbox.setRange(0, 19)
        self.l_spinbox.setValue(2) # 默认值
        self.l_spinbox.valueChanged.connect(self.on_parameters_changed)
        control_layout.addWidget(self.l_spinbox, 1, 1)
        
        # 磁量子数 m
        control_layout.addWidget(QLabel("磁量子数 m:"), 2, 0)
        self.m_spinbox = QSpinBox()
        self.m_spinbox.setRange(-19, 19)
        self.m_spinbox.setValue(0)
        self.m_spinbox.valueChanged.connect(self.on_parameters_changed)
        control_layout.addWidget(self.m_spinbox, 2, 1)
        
        # 核电荷数 Z
        control_layout.addWidget(QLabel("核电荷数 Z:"), 3, 0)
        self.z_spinbox = QSpinBox()
        self.z_spinbox.setRange(1, 100)
        self.z_spinbox.setValue(1)
        self.z_spinbox.valueChanged.connect(self.on_parameters_changed)
        control_layout.addWidget(self.z_spinbox, 3, 1)
        
        # 空间范围 space
        control_layout.addWidget(QLabel("空间范围 (a0):"), 4, 0)
        self.space_spinbox = QSpinBox()
        self.space_spinbox.setRange(1, 5000)
        self.space_spinbox.setValue(40)
        self.space_spinbox.setSingleStep(5)
        self.space_spinbox.valueChanged.connect(self.on_advanced_parameters_changed)
        control_layout.addWidget(self.space_spinbox, 4, 1)

        # 自动缩放开关
        self.auto_scale_check = QCheckBox("随 n 自动调整空间范围")
        self.auto_scale_check.setChecked(True)
        control_layout.addWidget(self.auto_scale_check, 5, 0, 1, 2)
        
        # 网格点数 num_points
        control_layout.addWidget(QLabel("网格点数:"), 6, 0)
        self.num_points_spinbox = QSpinBox()
        self.num_points_spinbox.setRange(50, 400)
        self.num_points_spinbox.setValue(100) 
        self.num_points_spinbox.setSingleStep(10)
        self.num_points_spinbox.valueChanged.connect(self.on_advanced_parameters_changed)
        control_layout.addWidget(self.num_points_spinbox, 6, 1)
        
        # 电子云总点数
        control_layout.addWidget(QLabel("电子云采样点数:"), 7, 0)
        self.total_points_spinbox = QSpinBox()
        self.total_points_spinbox.setRange(1000, 1000000)
        self.total_points_spinbox.setValue(50000)
        self.total_points_spinbox.setSingleStep(10000)
        self.total_points_spinbox.valueChanged.connect(self.on_advanced_parameters_changed)
        control_layout.addWidget(self.total_points_spinbox, 7, 1)
        
        # 等值面阈值系数
        control_layout.addWidget(QLabel("等值面阈值系数 (0-1):"), 8, 0)
        self.threshold_spinbox = QtWidgets.QDoubleSpinBox()
        self.threshold_spinbox.setRange(0.001, 0.5)
        self.threshold_spinbox.setValue(0.03) # 默认0.03
        self.threshold_spinbox.setSingleStep(0.01)
        self.threshold_spinbox.setDecimals(3)
        self.threshold_spinbox.valueChanged.connect(self.on_advanced_parameters_changed)
        control_layout.addWidget(self.threshold_spinbox, 8, 1)
        
        # 可视化类型
        control_layout.addWidget(QLabel("可视化类型:"), 9, 0)
        self.viz_combo = QComboBox()
        self.viz_combo.addItems(["3D等值面可视化", "3D电子云可视化", "截面图", "全部"])
        self.viz_combo.currentIndexChanged.connect(self.on_visualization_changed)
        control_layout.addWidget(self.viz_combo, 9, 1)
        
        # 按钮
        self.update_btn = QPushButton("更新可视化")
        self.update_btn.clicked.connect(self.update_visualization)
        control_layout.addWidget(self.update_btn, 10, 0, 1, 2)
        
        self.reset_btn = QPushButton("重置为默认参数")
        self.reset_btn.clicked.connect(self.reset_to_defaults)
        control_layout.addWidget(self.reset_btn, 11, 0, 1, 2)
        
        control_group.setLayout(control_layout)
        scroll_layout.addWidget(control_group)
        
        scroll.setWidget(scroll_widget)
        main_layout.addWidget(scroll, 1)
        
        # Matplotlib
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas, 3)
        
        self.status_label = QLabel("就绪")
        main_layout.addWidget(self.status_label)
        
    def setup_initial_params(self):
        self.Zn = 1
        self.n = 4
        self.l = 2
        self.m = 0
        self.num_points = 100
        self.space = 40
        self.total_points = 50000
        self.threshold_ratio = 0.03
        self.viz_type = 0
        
    def on_parameters_changed(self):
        self.n = self.n_spinbox.value()
        self.l = self.l_spinbox.value()
        self.m = self.m_spinbox.value()
        self.Zn = self.z_spinbox.value()
        
        # 限制逻辑
        if self.l >= self.n:
            self.l_spinbox.setValue(self.n - 1)
            self.l = self.n - 1
            return
        
        # 即使 m 是负数，范围也是有效的，只要绝对值 <= l
        if abs(self.m) > self.l:
            self.m_spinbox.setValue(0)
            self.m = 0
            return

        # 自动调整空间
        if self.auto_scale_check.isChecked():
            #  3 * n^2 / Z
            suggested_space = int(3.0 * (self.n ** 2) / self.Zn)
            if abs(self.space_spinbox.value() - suggested_space) > 5:
                self.space_spinbox.blockSignals(True)
                self.space_spinbox.setValue(suggested_space)
                self.space = suggested_space
                self.space_spinbox.blockSignals(False)
            
        self.status_label.setText(f"参数: n={self.n}, l={self.l}, m={self.m}, Z={self.Zn}")
    
    def on_advanced_parameters_changed(self):
        self.space = self.space_spinbox.value()
        self.num_points = self.num_points_spinbox.value()
        self.total_points = self.total_points_spinbox.value()
        self.threshold_ratio = self.threshold_spinbox.value()
        self.status_label.setText("参数已更新")
        
    def on_visualization_changed(self, index):
        self.viz_type = index
        self.update_visualization()
    
    def reset_to_defaults(self):
        self.n_spinbox.setValue(4)
        self.l_spinbox.setValue(2)
        self.m_spinbox.setValue(0)
        self.z_spinbox.setValue(1)
        self.auto_scale_check.setChecked(True)
        self.num_points_spinbox.setValue(100)
        self.total_points_spinbox.setValue(50000)
        self.threshold_spinbox.setValue(0.03)
        self.viz_combo.setCurrentIndex(0)
        self.on_parameters_changed()
        self.update_visualization()
    
    def calculate_wavefunction_and_prob(self):
        """
        计算波函数和概率密度。
        """
        # 生成网格
        x = np.linspace(-self.space, self.space, self.num_points)
        y = np.linspace(-self.space, self.space, self.num_points)
        z = np.linspace(-self.space, self.space, self.num_points)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
        
        # 坐标转换
        r = np.sqrt(X**2 + Y**2 + Z**2)
        # 防止除零
        theta = np.arccos(Z / (r + 1e-12))
        phi = np.arctan2(Y, X)
        
        Zn = self.Zn
        n = self.n
        l = self.l
        m = self.m
        a0 = 1.0 # 简化单位
        
        rho = 2.0 * Zn * r / (n * a0)
        
        # 归一化系数 N
        term1 = 3 * np.log(2.0 * Zn / n)
        term2 = gammaln(n - l)
        term3 = np.log(2.0 * n)
        term4 = gammaln(n + l + 1)
        normalization_r = np.exp(0.5 * (term1 + term2 - term3 - term4))
        
        # 拉盖尔多项式
        L_vals = genlaguerre(n - l - 1, 2 * l + 1)(rho)
        
        R = normalization_r * np.exp(-rho / 2.0) * (rho**l) * L_vals
        
        # 2. 角向部分 Y(theta, phi) 

        Y_complex = sph_harm(abs(m), l, phi, theta)
        
        if m == 0:
            Y_real = Y_complex.real
        elif m > 0:
            # Re组合: (Y + (-1)^m Y*)/sqrt(2) -> proportional to cos(m*phi)
            Y_real = np.sqrt(2) * ((-1)**m) * Y_complex.real
        else:
            # Im组合: (Y - (-1)^m Y*)/i*sqrt(2) -> proportional to sin(|m|*phi)
            Y_real = np.sqrt(2) * ((-1)**abs(m)) * Y_complex.imag
            
        psi = R * Y_real
        
        probability = psi**2
        # 归一化概率密度用于绘图
        max_val = np.max(probability)
        if max_val > 0:
            probability /= max_val
            
        return X, Y, Z, probability, psi

    def imagine3D(self, X, Y, Z, probability, psi):
        self.figure.clear()
        ax = self.figure.add_subplot(111, projection='3d')
        
        try:
            # --- 关键优化：高斯滤波 ---
            # 这使得等值面平滑，不会出现破碎的碎片
            prob_smooth = gaussian_filter(probability, sigma=1.0)
            
       
            threshold = self.threshold_ratio * np.max(prob_smooth)
            
            # marching_cubes
            try:
                verts, faces, _, _ = marching_cubes(prob_smooth, level=threshold)
            except (ValueError, RuntimeError):
                # 如果失败，尝试降低阈值
                threshold = 0.5 * threshold
                verts, faces, _, _ = marching_cubes(prob_smooth, level=threshold)


            scale_factor = 2 * self.space / (self.num_points - 1)
            verts = verts * scale_factor - self.space
            
            #颜色处理：

            
            mesh = ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], 
                           cmap='coolwarm', alpha=0.6, linewidth=0.1)
            
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_xlim(-self.space, self.space)
            ax.set_ylim(-self.space, self.space)
            ax.set_zlim(-self.space, self.space)
            ax.set_title(f'轨道 ({self.n}, {self.l}, {self.m}) 等值面\nSpace={self.space}, Thresh={self.threshold_ratio}')
            
            ax.view_init(elev=30, azim=45)
            
            self.canvas.draw()
            
        except Exception as e:
            self.status_label.setText(f"3D绘制错误: {str(e)}")
            ax.text(0, 0, 0, "无法生成等值面\n请尝试调整阈值或Space", transform=ax.transAxes)
            self.canvas.draw()

    def point_visualization(self, X, Y, Z, probability, psi):
        """
        电子云可视化 (蒙特卡洛采样)
        """
        self.figure.clear()
        ax = self.figure.add_subplot(111, projection='3d')
        
        flat_prob = probability.flatten()
        flat_psi = psi.flatten()
        
        # 阈值过滤
        mask = flat_prob > 0.0001
        valid_indices = np.where(mask)[0]
        
        if len(valid_indices) == 0:
            ax.text(0.5, 0.5, 0.5, "概率密度过低", ha='center')
            self.canvas.draw()
            return
            
        valid_probs = flat_prob[valid_indices]
        
        # 采样数量
        n_samples = min(self.total_points, len(valid_indices))
        
        # 归一化用于 random.choice
        p_norm = valid_probs / np.sum(valid_probs)
        
        # 随机采样索引
        chosen_indices_local = np.random.choice(len(valid_indices), n_samples, p=p_norm)
        chosen_indices = valid_indices[chosen_indices_local]
        
        # 获取坐标
        x_p = X.flatten()[chosen_indices]
        y_p = Y.flatten()[chosen_indices]
        z_p = Z.flatten()[chosen_indices]
        psi_p = flat_psi[chosen_indices]
        
        # 分离正负相位
        pos_mask = psi_p > 0
        neg_mask = ~pos_mask
        
        if np.any(pos_mask):
            ax.scatter(x_p[pos_mask], y_p[pos_mask], z_p[pos_mask], c='red', s=1, alpha=0.3, label='Positive')
        if np.any(neg_mask):
            ax.scatter(x_p[neg_mask], y_p[neg_mask], z_p[neg_mask], c='blue', s=1, alpha=0.3, label='Negative')
            
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim(-self.space, self.space)
        ax.set_ylim(-self.space, self.space)
        ax.set_zlim(-self.space, self.space)
        ax.legend()
        ax.set_title(f'电子云 ({self.n}, {self.l}, {self.m})')
        
        self.canvas.draw()

    def plot_cross_sections(self, X, Y, Z, probability):
        self.figure.clear()
        
        mid = self.num_points // 2
        
        # 截取中心切片
        slices = [
            probability[mid, :, :],  # YZ (X=0)
            probability[:, mid, :],  # XZ (Y=0)
            probability[:, :, mid]   # XY (Z=0)
        ]
        
        titles = ['YZ平面 (X=0)', 'XZ平面 (Y=0)', 'XY平面 (Z=0)']
        
        # 颜色映射
        white_to_purple = LinearSegmentedColormap.from_list(
            "white_purple",
            [(0, 0, 0), (0.1, 0.1, 0.1), (0.29, 0.0, 0.51), 
             (1.0, 0.0, 0.0), (1.0, 1.0, 0.0),
             (0.8, 0.8, 0.8), (0.9, 0.9, 0.9), (1.0, 1.0, 1.0)]
        )
        
        axes = self.figure.subplots(1, 3)
        extent = [-self.space, self.space, -self.space, self.space]
        
        for ax, slc, title in zip(axes, slices, titles):
            im = ax.imshow(slc.T, extent=extent, origin='lower', cmap=white_to_purple, aspect='auto')
            ax.set_title(title)
            plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        
        self.figure.tight_layout()
        self.canvas.draw()

    def plot_all(self, X, Y, Z, probability, psi):
        self.figure.clear()
        
        # 3D
        ax1 = self.figure.add_subplot(121, projection='3d')
        prob_smooth = gaussian_filter(probability, sigma=1.0)
        threshold = self.threshold_ratio * np.max(prob_smooth)
        try:
            verts, faces, _, _ = marching_cubes(prob_smooth, level=threshold)
            scale_factor = 2 * self.space / (self.num_points - 1)
            verts = verts * scale_factor - self.space
            ax1.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], 
                           cmap='coolwarm', alpha=0.6)
            ax1.set_title("3D等值面")
        except:
            pass
            
        # XY截面
        ax2 = self.figure.add_subplot(122)
        mid = self.num_points // 2
        im = ax2.imshow(probability[:, :, mid].T, 
                       extent=[-self.space, self.space, -self.space, self.space],
                       origin='lower', cmap='magma')
        ax2.set_title("XY截面")
        plt.colorbar(im, ax=ax2)
        
        self.figure.tight_layout()
        self.canvas.draw()

    def update_visualization(self):
        try:
            self.status_label.setText("正在计算...")
            QtWidgets.QApplication.processEvents()
            
            X, Y, Z, probability, psi = self.calculate_wavefunction_and_prob()
            
            self.status_label.setText("正在渲染...")
            QtWidgets.QApplication.processEvents()
            
            if self.viz_type == 0:
                self.imagine3D(X, Y, Z, probability, psi)
            elif self.viz_type == 1:
                self.point_visualization(X, Y, Z, probability, psi)
            elif self.viz_type == 2:
                self.plot_cross_sections(X, Y, Z, probability)
            elif self.viz_type == 3:
                self.plot_all(X, Y, Z, probability, psi)
                
            self.status_label.setText(f"完成: n={self.n}, l={self.l}, m={self.m}")
            
        except Exception as e:
            self.status_label.setText(f"错误: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = hydrogen_orbital_frame()
    window.setWindowTitle("氢原子轨道可视化")
    window.resize(1200, 800)
    window.show()
    sys.exit(app.exec())