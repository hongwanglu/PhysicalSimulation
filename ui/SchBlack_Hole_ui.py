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
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class schblack_hole_frame(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()

        # 设置窗口
        self.setWindowTitle('Gravitational Lensing Simulation')
        self.setGeometry(100, 100, 800, 600)

        # 创建 QWidget 和布局
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        # 创建 matplotlib 图表
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # 设置点击事件
        self.canvas.mpl_connect('button_press_event', self.on_click)

        # 绘制初始的事件视界
        self.ax.add_patch(plt.Circle((0, 0), 2, fill=True, color='black'))
        self.ax.set_xlim(-30, 30)
        self.ax.set_ylim(-15, 15)
        self.ax.set_aspect(1)
        self.ax.grid(True)

    def on_click(self, event):
        if event.button == 1:  # 左键点击
            self.ax.cla()  # 清除之前的结果
            self.ax.add_patch(plt.Circle((0, 0), 2, fill=True, color='black'))  # 重新绘制黑洞

            # 获取点击位置
            x0 = event.xdata
            y0 = event.ydata
            print(f"Clicked at: ({x0}, {y0})")

            # 动态导入 gravitational_lensing 函数
            from SchBlack_Hole import gravitational_lensing

            # 调用计算函数获取光线路径
            trajectories = gravitational_lensing(x0, y0)

            # 绘制光线路径
            for trajectory in trajectories:
                self.ax.plot(trajectory[:, 0], trajectory[:, 1], 'b', linewidth=1)

            self.ax.set_xlim(-30, 30)
            self.ax.set_ylim(-15, 15)
            self.ax.set_aspect(1)
            self.ax.grid(True)

            # 更新绘图
            self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = schblack_hole_frame()
    window.show()
    sys.exit(app.exec())
