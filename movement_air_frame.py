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

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFrame
from ui.movement_air_frame_ui import Ui_Frame
from movement_data import movement_data
import pyqtgraph as pg


class movement_air_frame(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super(movement_air_frame, self).__init__(parent)
        self.setupUi(self)

        # 初始化参数
        self.movement_data = movement_data()

        self.w = pg.PlotWidget()
        self.verticalLayout.replaceWidget(self.openGLWidget_3, self.w)
        self.openGLWidget_3.setParent(None)

        self.dt = 0.001  # 时间间隔
        self.mass = 5.0
        self.radius = 1.0
        self.vx = 10.0
        self.vy = 10.0

        self.w.setXRange(-10, 10)
        self.w.setYRange(-10, 10)

        # 初始化滑块
        self.Slider_mass_2.setRange(1, 100)
        self.Slider_mass_2.setValue(int(self.mass))
        self.Slider_radius_2.setRange(1, 100)
        self.Slider_radius_2.setValue(int(self.radius*10))
        self.Slider_vx_2.setRange(-100, 100)
        self.Slider_vx_2.setValue(int(self.vx))
        self.Slider_vy_2.setRange(-100, 100)
        self.Slider_vy_2.setValue(int(self.vy))

        # 初始化标签
        self.mass_changed(self.mass)
        self.radius_changed(self.radius*10)
        self.vx_changed(self.vx)
        self.vy_changed(self.vy)

        # 设置滑块信号槽
        self.Slider_mass_2.valueChanged.connect(self.mass_changed)
        self.Slider_radius_2.valueChanged.connect(self.radius_changed)
        self.Slider_vx_2.valueChanged.connect(self.vx_changed)
        self.Slider_vy_2.valueChanged.connect(self.vy_changed)
        self.pushButton.clicked.connect(self.movement_data_show)
        self.Updated()

        self.show()
        # self.movement_data.show()

    def mass_changed(self, value):
        self.mass = float(value)
        self.label_mass_2.setText('mass: ' + str(self.mass))
        self.Updated()

    def radius_changed(self, value):
        self.radius = float(value) / 10
        self.label_radius_2.setText('radius: ' + str(self.radius))
        self.Updated()

    def vx_changed(self, value):
        self.vx = float(value)
        self.label_vx_2.setText('vx: ' + str(self.vx))
        self.Updated()

    def vy_changed(self, value):
        self.vy = float(value)
        self.label_vy_2.setText('vy: ' + str(self.vy))
        self.Updated()

    def movement_data_show(self):
        if self.movement_data.isVisible():
            self.movement_data.close()
        else:
            self.movement_data.show()
            self.Updated()

    def Updated(self):
        def f(y, t):
            g = -9.8
            x, y, vx, vy = y
            v = np.sqrt(vx ** 2 + vy ** 2)
            return [vx, vy, -0.5 * 1.225 * np.pi * self.radius ** 2 * v * vx / self.mass,
                    g - 0.5 * 1.225 * np.pi * self.radius ** 2 * v * vy / self.mass]

        tspan = arange(0, 30, self.dt)
        sol = odeint(f, array([0.0, 0.0, self.vx, self.vy]), tspan)
        self.w.clear()
        self.w.plot(sol[:, 0:2], pen=pg.mkPen(width=5))
        if self.movement_data.isVisible():
            self.movement_data.openGLWidget.clear()
            self.movement_data.openGLWidget_2.clear()
            self.movement_data.openGLWidget_3.clear()
            self.movement_data.openGLWidget_4.clear()
            self.movement_data.openGLWidget_5.clear()
            self.movement_data.openGLWidget.plot(np.concatenate((tspan[:, None], sol[:, 2:3]), axis=1), pen=pg.mkPen(width=5))
            self.movement_data.openGLWidget_2.plot(np.concatenate((tspan[:, None], sol[:, 3:4]), axis=1), pen=pg.mkPen(width=5))
            self.movement_data.openGLWidget_3.plot(np.concatenate((tspan[:, None], sol[:, 0:1]), axis=1), pen=pg.mkPen(width=5))
            self.movement_data.openGLWidget_4.plot(np.concatenate((tspan[:, None], sol[:, 1:2]), axis=1), pen=pg.mkPen(width=5))
            v = np.sqrt(sol[:,2:3]**2+sol[:,3:4]**2)
            self.movement_data.openGLWidget_5.plot(np.concatenate((tspan[:,None],v),axis=1), pen=pg.mkPen(width=5))

    def closeEvent(self, event):
        # 关闭主窗口时关闭其他窗口
        self.movement_data.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mytest = movement_air_frame()
    app.exec()
