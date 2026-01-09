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

import sys
from PySide6 import QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
import numpy as np
from ui.wavefunction_superposition_ui import WaveFunction

class wavefunction_superposition_frame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(wavefunction_superposition_frame, self).__init__(parent)
        self.setWindowTitle("叠加态波函数演示")
        self.resize(970, 770)

        # 初始化波函数计算类
        self.wave_function = WaveFunction()
        self.x = np.linspace(0, self.wave_function.a, 100)
        self.t_values = np.linspace(0, 10000, 7000)

        # 创建UI组件
        self.layout = QtWidgets.QVBoxLayout(self)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # 控制区
        control_layout = QtWidgets.QVBoxLayout()
        coefficient_grid = QtWidgets.QGridLayout()
        self.coefficient_inputs = [QtWidgets.QDoubleSpinBox() for _ in range(10)]
        
        for i, input_box in enumerate(self.coefficient_inputs):
            input_box.setRange(0.0, 1.0)
            input_box.setSingleStep(0.1)
            input_box.setValue(self.wave_function.coefficient[i])
            input_box.valueChanged.connect(self.update_coefficients)
            label = QtWidgets.QLabel(f"n为{i+1}的系数c:")
            coefficient_grid.addWidget(label, i // 5, (i % 5) * 2)
            coefficient_grid.addWidget(input_box, i // 5, (i % 5) * 2 + 1)
        
        control_layout.addLayout(coefficient_grid)

        # 播放和暂停按钮
        button_layout = QtWidgets.QHBoxLayout()
        self.play_button = QtWidgets.QPushButton("播放")
        self.pause_button = QtWidgets.QPushButton("暂停")
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.pause_button)
        control_layout.addLayout(button_layout)

        self.layout.addLayout(control_layout)

        # 初始化动画
        self.line_real, = self.ax.plot(self.x, np.real(self.wave_function.desirable_psi(self.x, 0)), label='Real Part')
        self.line_imag, = self.ax.plot(self.x, np.imag(self.wave_function.desirable_psi(self.x, 0)), label='Imaginary Part')
        self.ax.set_xlim(0, self.wave_function.a)
        self.ax.set_ylim(-2.5, 2.5)
        self.ax.legend()

        # 创建动画并停止它
        self.anim = FuncAnimation(self.figure, self.update_plot, frames=self.t_values, interval=10, blit=True,repeat=True)
        
        # 绑定信号
        self.play_button.clicked.connect(self.play_animation)
        self.pause_button.clicked.connect(self.pause_animation)
        
        

    def update_coefficients(self):
        # 更新系数值
        for i, input_box in enumerate(self.coefficient_inputs):
            self.wave_function.coefficient[i] = input_box.value()
        self.update_plot(0)  # 更新图形

    def play_animation(self):
        self.anim.event_source.start()  # 开始动画

    def pause_animation(self):
        self.anim.event_source.stop()   # 停止动画

    def update_plot(self, t):
        # 计算波函数的实部和虚部
        y_real = np.real(self.wave_function.desirable_psi(self.x, t))
        y_imag = np.imag(self.wave_function.desirable_psi(self.x, t))
        
        # 更新图形数据
        self.line_real.set_ydata(y_real)
        self.line_imag.set_ydata(y_imag)
        
        # 返回需要更新的对象
        return self.line_real, self.line_imag


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = wavefunction_superposition_frame()
    window.show()
    sys.exit(app.exec())
