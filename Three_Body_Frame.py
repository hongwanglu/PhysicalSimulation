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
from scipy.integrate import odeint
import numpy as np
from numpy import array, arange
from numpy.linalg import norm
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFrame

from ui.three_body_frame_ui import Ui_Frame
from Star_Data import star_data
from three_body_example import three_body_example


class three_body_frame(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super(three_body_frame, self).__init__(parent)

        self.setupUi(self)

        self.w = gl.GLViewWidget()
        self.verticalLayout.replaceWidget(self.openGLWidget, self.w)
        self.openGLWidget.setParent(None)

        self.star_data = star_data()
        self.example = three_body_example()

        self.frame = 0  # 用于作图计数
        self.dt = 0.0005  # 时间间隔
        self.N = 0.1  # 计算长度

        # 按钮连接槽函数
        self.button_play.clicked.connect(self.play)
        self.button_settings.clicked.connect(self.settings)
        self.button_clear.clicked.connect(self.clear)
        self.button_pause.clicked.connect(self.pause)
        self.button_reset.clicked.connect(self.reset)
        self.button_more.clicked.connect(self.more)
        self.example.radioButton_1.clicked.connect(self.func_example)
        self.example.radioButton_2.clicked.connect(self.func_example)
        self.example.radioButton_3.clicked.connect(self.func_example)
        self.example.radioButton_4.clicked.connect(self.func_example)
        self.example.radioButton_5.clicked.connect(self.func_example)
        self.example.radioButton_6.clicked.connect(self.func_example)
        # self.button_calculate.clicked.connect(self.calculate)
        # self.button_pause.setEnabled(False)
        # self.button_play.setEnabled(False)
        # self.button_reset.setEnabled(False)
        # self.button_clear.setEnabled(False)

        # 设置摄像机
        # self.w.setCameraPosition(distance=1200)
        self.w.setBackgroundColor('w')

        # 设置坐标系
        # gx = gl.GLGridItem()
        # gx.setSpacing(0.05,0.05,0.05)
        # gx.rotate(90, 0, 1, 0)
        # # gx.translate(-10, 0, 0)
        # self.w.addItem(gx)
        # gy = gl.GLGridItem()
        # gy.setSpacing(0.05, 0.05, 0.05)
        # gy.rotate(90, 1, 0, 0)
        # # gy.translate(0, -10, 0)
        # self.w.addItem(gy)
        self.gz = gl.GLGridItem(color=(0,0,0,100))
        self.gz.setSpacing(200, 200, 200)
        self.gz.setSize(10000, 10000, 10000)
        # gz.translate(0, 0, -10)
        # self.gz.setGLOptions('translucent')

        ax = gl.GLAxisItem()
        ax.setSize(10000, 10000, 10000)


        # 设置数据
        G = 6.67 * (10 ** -11)
        self.u1 = None
        self.u2 = None
        self.u3 = None
        self.u4 = None
        self.u5 = None
        self.u6 = None
        self.x0 = None
        self.line_pos1 = None
        self.line_pos2 = None
        self.line_pos3 = None
        self.pos1 = None
        self.pos2 = None
        self.pos3 = None
        self.result = None

        # 添加点对象和线对象
        self.dot1 = gl.GLScatterPlotItem(color=[1, 0, 0, 255], size=20, pxMode=True,glOptions='translucent')
        self.dot2 = gl.GLScatterPlotItem(color=[0, 1, 0, 255], size=20, pxMode=True,glOptions='translucent')
        self.dot3 = gl.GLScatterPlotItem(color=[0, 0, 1, 255], size=20, pxMode=True,glOptions='translucent')
        self.line1 = gl.GLLinePlotItem(color=[1, 0, 0, 25], width=3,glOptions='translucent')
        self.line2 = gl.GLLinePlotItem(color=[0, 1, 0, 25], width=3,glOptions='translucent')
        self.line3 = gl.GLLinePlotItem(color=[0, 0, 1, 25], width=3,glOptions='translucent')
        # self.dot1.setGLOptions('translucent')
        # self.dot2.setGLOptions('translucent')
        # self.dot3.setGLOptions('translucent')
        # self.line1.setGLOptions('translucent')
        # self.line2.setGLOptions('translucent')
        # self.line3.setGLOptions('translucent')
        # self.line1.setData(color=[1, 0, 0, 25], width=3)
        # self.line2.setData(color=[1, 1, 1, 25], width=3)
        # self.line3.setData(color=[0, 0, 1, 25], width=3)
        # self.dot1.setData(color=[1, 0, 0, 255], size=20, pxMode=True)
        # self.dot2.setData(color=[1, 1, 1, 255], size=20, pxMode=True)
        # self.dot3.setData(color=[0, 0, 1, 255], size=20, pxMode=True)
        self.w.addItem(self.dot1)
        self.w.addItem(self.dot2)
        self.w.addItem(self.dot3)
        self.w.addItem(self.line1)
        self.w.addItem(self.line2)
        self.w.addItem(self.line3)
        self.w.addItem(ax)
        self.w.addItem(self.gz)

        self.Initial_update()

        # 添加计时器
        self.t = QtCore.QTimer()
        self.t.timeout.connect(self.animate_update)
        self.t_init = QtCore.QTimer()
        self.t_init.timeout.connect(self.Initial_update)

    # 用于更新初始值
    def Initial_update(self):
        self.u1 = array([self.star_data.x1, self.star_data.y1, self.star_data.z1])
        self.u2 = array([self.star_data.vx1, self.star_data.vy1, self.star_data.vz1])
        self.u3 = array([self.star_data.x2, self.star_data.y2, self.star_data.z2])
        self.u4 = array([self.star_data.vx2, self.star_data.vy2, self.star_data.vz2])
        self.u5 = array([self.star_data.x3, self.star_data.y3, self.star_data.z3])
        self.u6 = array([self.star_data.vx3, self.star_data.vy3, self.star_data.vz3])
        self.x0 = array([self.u1, self.u2, self.u3, self.u4, self.u5, self.u6]).ravel()
        self.pos1 = array([self.x0[0:3]])
        self.pos2 = array([self.x0[6:9]])
        self.pos3 = array([self.x0[12:15]])
        self.line_pos1 = array([self.pos1[0], self.pos1[0]])
        self.line_pos2 = array([self.pos2[0], self.pos2[0]])
        self.line_pos3 = array([self.pos3[0], self.pos3[0]])
        self.line1.setData(pos=self.line_pos1)
        self.line2.setData(pos=self.line_pos2)
        self.line3.setData(pos=self.line_pos3)
        self.dot1.setData(pos=self.pos1)
        self.dot2.setData(pos=self.pos2)
        self.dot3.setData(pos=self.pos3)
        self.camera_update()
        self.result = None
        self.frame = 0

    # 用于动画中更新数据
    def animate_update(self):
        self.frame = self.frame + 1
        self.pos1 = array([self.result[self.frame][0:3]])
        self.pos2 = array([self.result[self.frame][6:9]])
        self.pos3 = array([self.result[self.frame][12:15]])
        self.camera_update()
        self.line_pos1 = np.vstack((self.line_pos1, self.pos1[0]))
        self.line_pos2 = np.vstack((self.line_pos2, self.pos2[0]))
        self.line_pos3 = np.vstack((self.line_pos3, self.pos3[0]))
        self.line1.setData(pos=self.line_pos1)
        self.line2.setData(pos=self.line_pos2)
        self.line3.setData(pos=self.line_pos3)
        self.dot1.setData(pos=self.pos1)
        self.dot2.setData(pos=self.pos2)
        self.dot3.setData(pos=self.pos3)
        if self.frame == len(self.result) - 1:
            self.frame = 0
            self.x0 = self.result[-1]
            self.calculate()

    # 更新相机位置
    def camera_update(self):
        center = (self.pos1[0] + self.pos2[0] + self.pos3[0]) / 3
        distance = max(norm(self.pos1 - self.pos2),
                       norm(self.pos3 - self.pos2),
                       norm(self.pos1 - self.pos3))
        # area = (1+int(max(norm(self.pos1), norm(self.pos2), norm(self.pos3)) / 10000)) * 10000
        # print(center)
        cen = pg.Vector(center[0], center[1], center[2])
        self.w.setCameraPosition(pos=cen, distance=distance + 1000)
        # self.gz.setSize(area, area, area)
        # self.gz.setSpacing((1+int(distance/500))*100,(1+int(distance/500))*100,(1+int(distance/500))*100)
        # print((int(distance/500))*100)

    def play(self):
        self.calculate()
        if self.frame < self.N / self.dt - 1:
            # self.button_play.setEnabled(False)
            self.t.start()

    def pause(self):
        self.t.stop()
        # self.button_play.setEnabled(True)

    def clear(self):
        self.pause()
        self.line_pos1 = array([self.pos1[0], self.pos1[0]])
        self.line_pos2 = array([self.pos2[0], self.pos2[0]])
        self.line_pos3 = array([self.pos3[0], self.pos3[0]])
        self.line1.setData(pos=self.line_pos1)
        self.line2.setData(pos=self.line_pos2)
        self.line3.setData(pos=self.line_pos3)

    def settings(self):
        self.reset()
        self.t_init.start()
        self.star_data.show()
        # self.button_clear.setEnabled(False)
        # self.button_reset.setEnabled(False)
        # self.button_play.setEnabled(False)
        # self.button_pause.setEnabled(False)

    def reset(self):
        self.pause()
        self.Initial_update()

    def more(self):
        self.reset()
        self.example.show()
        self.example.activateWindow()

    def calculate(self):
        self.t_init.stop()
        self.star_data.close()
        # 定步长控制
        tspan = arange(0, self.N, self.dt)
        # print(tspan)
        # 求解微分方程
        self.result = odeint(self.guidao, self.x0, tspan,
                             args=(self.star_data.mass1, self.star_data.mass2, self.star_data.mass3))
        # print(self.result)
        # self.button_play.setEnabled(True)
        # self.button_pause.setEnabled(True)
        # self.button_reset.setEnabled(True)
        # self.button_clear.setEnabled(True)

    def closeEvent(self, event):
        self.star_data.close()
        self.example.close()

    @staticmethod
    def guidao(y, t, m1, m2, m3):
        G = 6.67e-11

        u1 = y[0:3]
        u2 = y[3:6]
        u3 = y[6:9]
        u4 = y[9:12]
        u5 = y[12:15]
        u6 = y[15:18]

        u1x = u2
        u2x = G * (m2 * (u3 - u1) / (norm(u3 - u1)) ** 3 + m3 * (u5 - u1) / (norm(u5 - u1)) ** 3)
        u3x = u4
        u4x = G * (m3 * (u5 - u3) / (norm(u5 - u3)) ** 3 + m1 * (u1 - u3) / (norm(u1 - u3)) ** 3)
        u5x = u6
        u6x = G * (m1 * (u1 - u5) / (norm(u1 - u5)) ** 3 + m2 * (u3 - u5) / (norm(u3 - u5)) ** 3)
        y = array([u1x, u2x, u3x, u4x, u5x, u6x]).ravel()

        return y

    def func_example(self):
        self.reset()
        if self.example.radioButton_1.isChecked():
            self.button_settings.setEnabled(False)
            self.star_data.mass1 = 1.0 * 10 ** 18
            self.star_data.x1 = 500.0
            self.star_data.y1 = 0
            self.star_data.z1 = 0
            self.star_data.vx1 = 0
            self.star_data.vy1 = 7.0 * 10 ** 3
            self.star_data.vz1 = -7.0 * 1000

            self.star_data.mass2 = 1.0 * 10 ** 18
            self.star_data.x2 = -300.0
            self.star_data.y2 = 0
            self.star_data.z2 = 0
            self.star_data.vx2 = 0
            self.star_data.vy2 = -12.0 * 10 ** 3
            self.star_data.vz2 = -7.0 * 1000

            self.star_data.mass3 = 1000.0 * 10 ** 18
            self.star_data.x3 = 0
            self.star_data.y3 = 0
            self.star_data.z3 = 0
            self.star_data.vx3 = 0
            self.star_data.vy3 = 0
            self.star_data.vz3 = 0
            self.Initial_update()
        elif self.example.radioButton_2.isChecked():
            self.button_settings.setEnabled(False)
            self.star_data.mass1 = 500.0 * 10 ** 18
            self.star_data.x1 = 300.0
            self.star_data.y1 = 0
            self.star_data.z1 = 0
            self.star_data.vx1 = 0
            self.star_data.vy1 = 3.0 * 10 ** 3
            self.star_data.vz1 = 0

            self.star_data.mass2 = 250.0 * 10 ** 18
            self.star_data.x2 = -300.0
            self.star_data.y2 = 0
            self.star_data.z2 = 0
            self.star_data.vx2 = 0
            self.star_data.vy2 = -6.0 * 10 ** 3
            self.star_data.vz2 = 0

            self.star_data.mass3 = 1.0 * 10 ** 18
            self.star_data.x3 = 0
            self.star_data.y3 = 0
            self.star_data.z3 = 0
            self.star_data.vx3 = 0
            self.star_data.vy3 = 10000
            self.star_data.vz3 = 0
            self.Initial_update()
        elif self.example.radioButton_3.isChecked():
            self.button_settings.setEnabled(False)
            self.star_data.mass1 = 200.0 * 10 ** 18
            self.star_data.x1 = 0
            self.star_data.y1 = 200
            self.star_data.z1 = 0
            self.star_data.vx1 = -8 * 1000
            self.star_data.vy1 = 0
            self.star_data.vz1 = 0

            self.star_data.mass2 = 200.0 * 10 ** 18
            self.star_data.x2 = -100 * np.sqrt(3)
            self.star_data.y2 = -100
            self.star_data.z2 = 0
            self.star_data.vx2 = -self.star_data.vx1 * np.cos(np.pi / 3)
            self.star_data.vy2 = self.star_data.vx1 * np.sin(np.pi / 3)
            self.star_data.vz2 = 0

            self.star_data.mass3 = 200.0 * 10 ** 18
            self.star_data.x3 = 100 * np.sqrt(3)
            self.star_data.y3 = -100
            self.star_data.z3 = 0
            self.star_data.vx3 = -self.star_data.vx1 * np.cos(np.pi / 3)
            self.star_data.vy3 = -self.star_data.vx1 * np.sin(np.pi / 3)
            self.star_data.vz3 = 0
            self.Initial_update()
        elif self.example.radioButton_4.isChecked():
            self.button_settings.setEnabled(False)
            Q = 1 / 5.5
            self.star_data.mass1 = 160.0 * 10 ** 18
            self.star_data.x1 = 194.00087200
            self.star_data.y1 = -48.61750600
            self.star_data.z1 = 0
            self.star_data.vx1 = 18.64814740 * 1000 * Q
            self.star_data.vy1 = 17.29462920 * 1000 * Q
            self.star_data.vz1 = 0

            self.star_data.mass2 = 160.0 * 10 ** 18
            self.star_data.x2 = -194.00087200
            self.star_data.y2 = 48.61750600
            self.star_data.z2 = 0
            self.star_data.vx2 = 18.64814740 * 1000 * Q
            self.star_data.vy2 = 17.29462920 * 1000 * Q
            self.star_data.vz2 = 0

            self.star_data.mass3 = 160.0 * 10 ** 18
            self.star_data.x3 = 0
            self.star_data.y3 = 0
            self.star_data.z3 = 0
            self.star_data.vx3 = -37.29629480 * 1000 * Q
            self.star_data.vy3 = -34.58925840 * 1000 * Q
            self.star_data.vz3 = 0
            self.Initial_update()
        elif self.example.radioButton_5.isChecked():
            self.button_settings.setEnabled(False)
            self.star_data.mass1 = 250.0 * 10 ** 18
            self.star_data.x1 = 300.0
            self.star_data.y1 = 0
            self.star_data.z1 = 0
            self.star_data.vx1 = 0
            self.star_data.vy1 = 3727
            self.star_data.vz1 = 100

            self.star_data.mass2 = 250.0 * 10 ** 18
            self.star_data.x2 = -300.0
            self.star_data.y2 = 0
            self.star_data.z2 = 0
            self.star_data.vx2 = 0
            self.star_data.vy2 = -3727
            self.star_data.vz2 = 100

            self.star_data.mass3 = 1.0 * 10 ** 18
            self.star_data.x3 = 0
            self.star_data.y3 = 1000
            self.star_data.z3 = 0
            self.star_data.vx3 = 5774
            self.star_data.vy3 = 0
            self.star_data.vz3 = 100
            self.Initial_update()
        elif self.example.radioButton_6.isChecked():
            self.button_settings.setEnabled(True)
            self.star_data.mass1 = 250.0 * 10 ** 18
            self.star_data.x1 = 500.0
            self.star_data.y1 = 0.0
            self.star_data.z1 = 0.0
            self.star_data.vx1 = 0.0
            self.star_data.vy1 = 6.0 * 10 ** 3
            self.star_data.vz1 = 0.0

            self.star_data.mass2 = 250.0 * 10 ** 18
            self.star_data.x2 = -500.0
            self.star_data.y2 = 0.0
            self.star_data.z2 = 0.0
            self.star_data.vx2 = 0.0
            self.star_data.vy2 = -6.0 * 10 ** 3
            self.star_data.vz2 = 0.0

            self.star_data.mass3 = 500.0 * 10 ** 18
            self.star_data.x3 = 0.0
            self.star_data.y3 = 0.0
            self.star_data.z3 = 0.0
            self.star_data.vx3 = 0.0
            self.star_data.vy3 = 0.0
            self.star_data.vz3 = 0.0
            self.star_data.Setdata()
            self.Initial_update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mytest = three_body_frame()
    mytest.show()
    app.exec()