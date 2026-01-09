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
from numpy import array
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from ui.star_data_ui import Ui_star_data


class star_data(QMainWindow, Ui_star_data):
    def __init__(self, parent=None):
        super(star_data, self).__init__(parent)
        self.setupUi(self)

        # 设定初始数据
        self.G = 6.67 * (10 ** -11)
        G = 6.67 * (10 ** -11)

        self.mass1 = 250.0*10**18
        self.x1 = 500.0
        self.y1 = 0.0
        self.z1 = 0.0
        self.vx1 = 0.0
        self.vy1 = 6.0*10**3
        self.vz1 = 0.0

        self.mass2 = 250.0*10**18
        self.x2 = -500.0
        self.y2 = 0.0
        self.z2 = 0.0
        self.vx2 = 0.0
        self.vy2 = -6.0*10**3
        self.vz2 = 0.0

        self.mass3 = 500.0*10**18
        self.x3 = 0.0
        self.y3 = 0.0
        self.z3 = 0.0
        self.vx3 = 0.0
        self.vy3 = 0.0
        self.vz3 = 0.0

        # 连接槽函数
        self.Slider_m1.valueChanged.connect(self.mass1_changed)
        self.Slider_x1.valueChanged.connect(self.x1_changed)
        self.Slider_y1.valueChanged.connect(self.y1_changed)
        self.Slider_z1.valueChanged.connect(self.z1_changed)
        self.Slider_vx1.valueChanged.connect(self.vx1_changed)
        self.Slider_vy1.valueChanged.connect(self.vy1_changed)
        self.Slider_vz1.valueChanged.connect(self.vz1_changed)

        self.Slider_m2.valueChanged.connect(self.mass2_changed)
        self.Slider_x2.valueChanged.connect(self.x2_changed)
        self.Slider_y2.valueChanged.connect(self.y2_changed)
        self.Slider_z2.valueChanged.connect(self.z2_changed)
        self.Slider_vx2.valueChanged.connect(self.vx2_changed)
        self.Slider_vy2.valueChanged.connect(self.vy2_changed)
        self.Slider_vz2.valueChanged.connect(self.vz2_changed)

        self.Slider_m3.valueChanged.connect(self.mass3_changed)
        self.Slider_x3.valueChanged.connect(self.x3_changed)
        self.Slider_y3.valueChanged.connect(self.y3_changed)
        self.Slider_z3.valueChanged.connect(self.z3_changed)
        self.Slider_vx3.valueChanged.connect(self.vx3_changed)
        self.Slider_vy3.valueChanged.connect(self.vy3_changed)
        self.Slider_vz3.valueChanged.connect(self.vz3_changed)

        self.Setdata()

    def Setdata(self):
        self.Slider_m1.setValue(int(self.mass1/10**18))
        self.mass1_changed(self.mass1/10**18)
        self.Slider_x1.setValue(int(self.x1))
        self.x1_changed(self.x1)
        self.Slider_y1.setValue(int(self.y1))
        self.y1_changed(self.y1)
        self.Slider_z1.setValue(int(self.z1))
        self.z1_changed(self.z1)
        self.Slider_vx1.setValue(int(self.vx1/1000))
        self.vx1_changed(self.vx1/1000)
        self.Slider_vy1.setValue(int(self.vy1 / 1000))
        self.vy1_changed(self.vy1 / 1000)
        self.Slider_vz1.setValue(int(self.vz1 / 1000))
        self.vz1_changed(self.vz1 / 1000)

        self.Slider_m2.setValue(int(self.mass2 / 10 ** 18))
        self.mass2_changed(self.mass2 / 10 ** 18)
        self.Slider_x2.setValue(int(self.x2))
        self.x2_changed(self.x2)
        self.Slider_y2.setValue(int(self.y2))
        self.y2_changed(self.y2)
        self.Slider_z2.setValue(int(self.z2))
        self.z2_changed(self.z2)
        self.Slider_vx2.setValue(int(self.vx2 / 1000))
        self.vx2_changed(self.vx2 / 1000)
        self.Slider_vy2.setValue(int(self.vy2 / 1000))
        self.vy2_changed(self.vy2 / 1000)
        self.Slider_vz2.setValue(int(self.vz2 / 1000))
        self.vz2_changed(self.vz2 / 1000)

        self.Slider_m3.setValue(int(self.mass3 / 10 ** 18))
        self.mass3_changed(self.mass3 / 10 ** 18)
        self.Slider_x3.setValue(int(self.x3))
        self.x3_changed(self.x3)
        self.Slider_y3.setValue(int(self.y3))
        self.y3_changed(self.y3)
        self.Slider_z3.setValue(int(self.z3))
        self.z3_changed(self.z3)
        self.Slider_vx3.setValue(int(self.vx3 / 1000))
        self.vx3_changed(self.vx3 / 1000)
        self.Slider_vy3.setValue(int(self.vy3 / 1000))
        self.vy3_changed(self.vy3 / 1000)
        self.Slider_vz3.setValue(int(self.vz3 / 1000))
        self.vz3_changed(self.vz3 / 1000)

    def mass1_changed(self, value):
        self.mass1 = float(value)*10**18
        self.label_m1.setText('mass(*10^18): {0}'.format(float(value)))

    def x1_changed(self, value):
        self.x1 = float(value)
        self.label_x1.setText('x: ' + str(self.x1))

    def y1_changed(self, value):
        self.y1 = float(value)
        self.label_y1.setText('y: ' + str(self.y1))

    def z1_changed(self, value):
        self.z1 = float(value)
        self.label_z1.setText('z: ' + str(self.z1))

    def vx1_changed(self, value):
        self.vx1 = float(value)*10**3
        self.label_vx1.setText('vx(*10^3): {0}'.format(float(value)))

    def vy1_changed(self, value):
        self.vy1 = float(value)*10**3
        self.label_vy1.setText('vy(*10^3): {0}'.format(float(value)))

    def vz1_changed(self, value):
        self.vz1 = float(value)*10**3
        self.label_vz1.setText('vz(10^3): {0}'.format(float(value)))

    def mass2_changed(self, value):
        self.mass2 = float(value) * 10 ** 18
        self.label_m2.setText('mass(*10^18): {0}'.format(float(value)))

    def x2_changed(self, value):
        self.x2 = float(value)
        self.label_x2.setText('x: ' + str(self.x2))

    def y2_changed(self, value):
        self.y2 = float(value)
        self.label_y2.setText('y: ' + str(self.y2))

    def z2_changed(self, value):
        self.z2 = float(value)
        self.label_z2.setText('z: ' + str(self.z2))

    def vx2_changed(self, value):
        self.vx2 = float(value) * 10 ** 3
        self.label_vx2.setText('vx(*10^3): {0}'.format(float(value)))

    def vy2_changed(self, value):
        self.vy2 = float(value) * 10 ** 3
        self.label_vy2.setText('vy(*10^3): {0}'.format(float(value)))

    def vz2_changed(self, value):
        self.vz2 = float(value) * 10 ** 3
        self.label_vz2.setText('vz(10^3): {0}'.format(float(value)))

    def mass3_changed(self, value):
        self.mass3 = float(value) * 10 ** 18
        self.label_m3.setText('mass(*10^18): {0}'.format(float(value)))

    def x3_changed(self, value):
        self.x3 = float(value)
        self.label_x3.setText('x: ' + str(self.x3))

    def y3_changed(self, value):
        self.y3 = float(value)
        self.label_y3.setText('y: ' + str(self.y3))

    def z3_changed(self, value):
        self.z3 = float(value)
        self.label_z3.setText('z: ' + str(self.z3))

    def vx3_changed(self, value):
        self.vx3 = float(value) * 10 ** 3
        self.label_vx3.setText('vx(*10^3): {0}'.format(float(value)))

    def vy3_changed(self, value):
        self.vy3 = float(value) * 10 ** 3
        self.label_vy3.setText('vy(*10^3): {0}'.format(float(value)))

    def vz3_changed(self, value):
        self.vz3 = float(value) * 10 ** 3
        self.label_vz3.setText('vz(10^3): {0}'.format(float(value)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    star_data_win = star_data()
    star_data_win.show()
    app.exec()
