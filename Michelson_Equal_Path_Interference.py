# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2026 HongwangLu

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import sys
import platform

class michelson_equal_path_interference_frame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(michelson_equal_path_interference_frame, self).__init__(parent)

        # 设置 PyQt5 窗口
        self.setWindowTitle('迈克尔逊干涉仪模拟')
        self.setGeometry(100, 100, 800, 600)

        # 创建Matplotlib图像
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvas(self.fig)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # 设置参数
        # 检查操作系统 
        os_name = platform.system() 
        if os_name == 'Darwin': # MacOS 
            plt.rcParams['font.sans-serif'] = ['Hei']
        elif os_name == 'Linux': # Linux 
            plt.rcParams['font.sans-serif'] = ['SimHei']
        elif os_name == 'Windows': # Windows 
            plt.rcParams['font.sans-serif'] = ['SimHei'] # 或者 'Microsoft YaHei' 
        else: 
            print("Unsupported operating system")
        
        plt.rcParams['axes.unicode_minus'] = False

        self.f = 0.2  # 透镜的焦距（单位：m）
        self.lambda_ = 550e-9  # 入射光波长（单位：m）
        self.d = 0.4e-3  # 空气薄膜的初始厚度 (单位：m)

        # 根据公式求出光强分布
        self.xMax = 20000 * self.lambda_  # x取值范围约为[-11mm,11mm]
        self.yMax = 20000 * self.lambda_  # y取值范围约为[-11mm,11mm]
        self.step = 200 * self.lambda_

        self.x, self.y = np.meshgrid(np.arange(-self.xMax, self.xMax, self.step), 
                                     np.arange(-self.yMax, self.yMax, self.step))  # 建立坐标网格
        self.r = np.sqrt(self.x**2 + self.y**2)

        # 初始光强分布
        self.Ir = self.calculate_intensity(self.d)

        # 绘制光强分布
        self.H = self.ax.pcolormesh(self.x, self.y, self.Ir, shading='auto')
        self.ax.set_xlabel('x (m)', fontsize=15)
        self.ax.set_ylabel('y (m)', fontsize=15)
        self.ax.set_title('迈克尔逊干涉仪', fontsize=12)
        self.fig.colorbar(self.H)

        # 创建按钮
        self.button_increase = QtWidgets.QPushButton('增加 d', self)
        self.button_increase.clicked.connect(self.increase_d)

        self.button_decrease = QtWidgets.QPushButton('减少 d', self)
        self.button_decrease.clicked.connect(self.decrease_d)

        # 布局
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_increase)
        button_layout.addWidget(self.button_decrease)

        layout.addLayout(button_layout)

    def calculate_intensity(self, d):
        """根据给定的 d 计算光强分布"""
        return 4 * (np.cos(2 * np.pi * d / self.lambda_ * np.cos(np.arctan(self.r / self.f))))**2

    def increase_d(self):
        """增加 d 的值并更新光强分布图"""
        self.d += 0.00005e-3  # 增加 d
        self.Ir = self.calculate_intensity(self.d)  # 计算新的光强分布
        self.H.set_array(self.Ir.T.ravel())  # 更新图像数据
        self.canvas.draw_idle()  # 更新绘图

    def decrease_d(self):
        """减少 d 的值并更新光强分布图"""
        self.d -= 0.00005e-3  # 减少 d
        self.Ir = self.calculate_intensity(self.d)  # 计算新的光强分布
        self.H.set_array(self.Ir.T.ravel())  # 更新图像数据
        self.canvas.draw_idle()  # 更新绘图

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = michelson_equal_path_interference_frame()
    window.show()
    sys.exit(app.exec())
