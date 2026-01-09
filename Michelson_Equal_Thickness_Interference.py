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
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import sys
import platform

class michelson_equal_thickness_interference_frame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(michelson_equal_thickness_interference_frame, self).__init__(parent)
        
        # 设置中文字体
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
        
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        
        self.d = -5  # 初始化d的值
        
        # 初始化网格
        self.x = np.arange(0, 10, 0.01)  # x轴范围
        self.y = np.arange(0, 10, 0.01)  # y轴范围
        self.X, self.Y = np.meshgrid(self.x, self.y)  # 创建网格
        
        # 创建图形
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        # 创建 Matplotlib Canvas
        self.canvas = FigureCanvas(self.fig)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

        # 初始化干涉图像
        self.I = self.calculate_interference(self.d)
        self.im = self.ax2.imshow(self.I * 100, cmap=plt.get_cmap('gray'), extent=(0, 10, 0, 10), origin='lower')
        plt.colorbar(self.im, ax=self.ax2)  # 显示颜色条
        self.ax2.axis('off')  # 隐藏坐标轴

        # 绘制干涉仪结构
        self.ax1.set_title('Michelson interferometer setup', fontsize=13)
        self.ax1.set_xlim([-28, 28])
        self.ax1.set_ylim([-28, 28])
        self.ax1.set_xticks([])  # 隐藏x轴刻度
        self.ax1.set_yticks([])  # 隐藏y轴刻度
        self.ax1.set_facecolor('black')

        # 绘制M1和M2
        self.ax1.plot([-6, 6], [18.5, 21.5], linestyle='-', color='cyan', linewidth=1)  # M1
        self.ax1.plot([20, 20], [-6, 6], linestyle='-', color='cyan', linewidth=1)  # M2
        self.m2_prime_line, = self.ax1.plot([-6, 6], [20 + self.d, 20 + self.d], linestyle='--', color='cyan', linewidth=1)  # M2'
        self.ax1.text(10, 20, 'M1', fontsize=12, color='lime')
        self.m2_prime_text = self.ax1.text(10, 20 + self.d, 'M2\'', fontsize=12, color='lime')
        self.ax1.text(18, 9, 'M2', fontsize=12, color='lime')

        # 绘制辅助线
        self.ax1.plot([-4, 4], [-4, 4], linestyle='-', color='cyan', linewidth=1)  # Beam splitter
        self.ax1.plot([4, 12], [-4, 4], linestyle='-', color='cyan', linewidth=1)  # Beam splitter
        self.ax1.plot([0, 0], [-20, 20], linestyle='-', color='white', linewidth=1)  # Horizontal beam 1
        self.ax1.plot([-20, 20], [0, 0], linestyle='-', color='white', linewidth=1)  # Vertical beam 2

        # 创建 PyQt5 按钮
        self.button_increase = QtWidgets.QPushButton('增加 d', self)
        self.button_increase.clicked.connect(self.increase_d)

        self.button_decrease = QtWidgets.QPushButton('减少 d', self)
        self.button_decrease.clicked.connect(self.decrease_d)

        # 布局
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_increase)
        button_layout.addWidget(self.button_decrease)

        self.layout.addLayout(button_layout)

    def calculate_interference(self, d):
        """根据给定的 d 计算干涉图样"""
        theta1 = np.pi / 4  # 入射角
        return np.cos(np.pi * (self.X * np.tan(theta1) + np.abs(d))) ** 2

    def update_plot(self):
        """更新图像"""
        self.m2_prime_line.set_ydata([20 + self.d, 20 + self.d])  # 更新M2'的位置
        self.m2_prime_text.set_position([10, 20 + self.d])  # 更新M2'文本的位置
        self.I = self.calculate_interference(self.d)  # 重新计算干涉图样
        self.im.set_data(self.I * 100)  # 更新干涉图样
        self.canvas.draw_idle()  # 更新图像

    def increase_d(self):
        """增加 d 的值并更新干涉图样"""
        self.d += 0.05  # 增加d
        self.update_plot()

    def decrease_d(self):
        """减少 d 的值并更新干涉图样"""
        self.d -= 0.05  # 减少d
        self.update_plot()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = michelson_equal_thickness_interference_frame()
    window.show()
    sys.exit(app.exec())
