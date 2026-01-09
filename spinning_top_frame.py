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
import numpy as np
from numpy import sin, cos
from scipy.integrate import odeint
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFrame
import pyqtgraph.opengl as gl
from ui.spinning_top_frame_ui import Ui_Frame


class spinning_top_frame(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super(spinning_top_frame, self).__init__(parent)

        self.setupUi(self)
        self.gz = gl.GLGridItem(color=(0,0,0,100))
        self.gz.setSpacing(1, 1, 1)
        self.gz.setSize(100, 100, 100)
        self.w.setBackgroundColor('w')
        self.w.setCameraPosition(distance=20)
        ax = gl.GLAxisItem()
        ax.setSize(100, 100, 100)
        self.w.addItem(ax)

        I1 = 3 / 4
        I3 = 3 / 10
        M = 1
        g = 9.8
        l = 1

        self.theta0 = np.pi / 12
        self.phi0 = -np.pi / 2
        self.p_phi0 = 10
        self.psi0 = 0
        self.p_theta0 = 0

        self.p_psi0 = 0.5 * (2 * self.p_phi0 * np.cos(self.theta0) + self.p_phi0 * np.sin(self.theta0) * np.tan(
            self.theta0) + np.sqrt(
            -4 * g * I1 * l * M * np.tan(self.theta0) ** -1 * np.sin(self.theta0) ** -1 + self.p_phi0 ** 2 * np.sin(
                self.theta0) ** -2) * np.sin(
            self.theta0) ** 2 * np.tan(self.theta0))
        # print(self.p_psi0)
        self.y = None
        self.euler = None
        self.rotation = None
        self.angle = None

        self.radioButton_1.setChecked(True)
        self.radioButton_1.clicked.connect(self.example)
        self.radioButton_2.clicked.connect(self.example)
        self.radioButton_3.clicked.connect(self.example)
        self.button_play.clicked.connect(self.play)
        self.button_pause.clicked.connect(self.pause)

        spin_top = gl.MeshData.cylinder(rows=1, cols=100, radius=[0., 2.], length=5., offset=False)
        colors = np.ones((spin_top.faceCount(), 4), dtype=float)
        colors[:, 1] = np.linspace(0, 1, colors.shape[0])
        spin_top.setFaceColors(colors)
        self.spin_top = gl.GLMeshItem(meshdata=spin_top, smooth=True, drawEdges=False, shader='balloon')
        self.line = gl.GLLinePlotItem(color=[1, 0, 0, 25], width=3, antialias=True)
        self.w.addItem(self.line)
        self.line.setGLOptions('translucent')
        self.center = gl.GLLinePlotItem(width=3, pos=np.array([[0, 0, 0], [0, 0, 5]]))
        self.center.setGLOptions('translucent')
        self.w.addItem(self.center)
        self.w.addItem(self.spin_top)
        self.w.addItem(self.gz)

        self.Init()

        self.frame = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.angle_update)

    def Init(self):
        self.frame = 0
        rotation = QtGui.QMatrix4x4(
            cos(self.phi0) * cos(self.theta0) * cos(self.psi0) - sin(self.phi0) * sin(self.psi0),
            -cos(self.psi0) * sin(self.phi0) - cos(self.phi0) * cos(self.theta0) * sin(self.psi0),
            cos(self.phi0) * sin(self.theta0), 0,
            cos(self.phi0) * sin(self.psi0) + cos(self.theta0) * cos(self.psi0) * sin(self.phi0),
            cos(self.phi0) * cos(self.psi0) - cos(self.theta0) * sin(self.phi0) * sin(self.psi0),
            sin(self.phi0) * sin(self.theta0), 0,
            -cos(self.psi0) * sin(self.theta0), sin(self.theta0) * sin(self.psi0), cos(self.theta0), 0,
            0, 0, 0, 1)
        self.spin_top.setTransform(rotation)
        self.center.setTransform(rotation)
        self.line.setData(pos=np.array([[0, 0, 0], [0, 0, 0]]))

    def calculate(self):
        I1 = 3 / 4
        I3 = 3 / 10
        M = 1
        g = 9.8
        l = 1
        Y0 = np.array([self.theta0, self.p_theta0, self.phi0, self.p_phi0, self.psi0, self.p_psi0])
        dt = 0.005
        T = 6.2
        tspan = np.arange(0, T, dt)
        self.y = odeint(self.Dfunc, Y0, tspan, args=(I1, I3, M, g, l))
        theta = self.y[:, 0]
        phi = self.y[:, 2]
        psi = self.y[:, 4]
        self.rotation = np.array([[cos(phi) * cos(theta) * cos(psi) - sin(phi) * sin(psi),
                                   -cos(psi) * sin(phi) - cos(phi) * cos(theta) * sin(psi), cos(phi) * sin(theta)],
                                  [cos(phi) * sin(psi) + cos(theta) * cos(psi) * sin(phi),
                                   cos(phi) * cos(psi) - cos(theta) * sin(phi) * sin(psi), sin(phi) * sin(theta)],
                                  [-cos(psi) * sin(theta), sin(theta) * sin(psi), cos(theta)]])
        self.euler = 5 * np.array([np.cos(phi) * np.sin(theta),
                                   np.sin(theta) * np.sin(phi),
                                   np.cos(theta)]).T
        self.line.setData(pos=self.euler)

    def example(self):
        self.pause()
        self.Init()
        self.frame = 0
        if self.radioButton_1.isChecked():
            self.p_theta0 = 0
        elif self.radioButton_2.isChecked():
            self.p_theta0 = 1
        elif self.radioButton_3.isChecked():
            self.p_theta0 = 0.2

    def play(self):
        self.calculate()
        self.timer.start()

    def pause(self):
        self.timer.stop()

    def angle_update(self):
        self.angle = QtGui.QMatrix4x4(self.rotation[0][0][self.frame], self.rotation[0][1][self.frame],
                                      self.rotation[0][2][self.frame], 0,
                                      self.rotation[1][0][self.frame], self.rotation[1][1][self.frame],
                                      self.rotation[1][2][self.frame], 0,
                                      self.rotation[2][0][self.frame], self.rotation[2][1][self.frame],
                                      self.rotation[2][2][self.frame], 0,
                                      0, 0, 0, 1)
        self.spin_top.setTransform(self.angle)
        self.center.setTransform(self.angle)
        if self.frame == 6.1 / 0.005 - 1:
            self.frame = 0
        else:
            self.frame = self.frame + 1

    @staticmethod
    def Dfunc(Y, t, I1, I3, M, g, l):
        theta = Y[0]
        p_theta = Y[1]
        phi = Y[2]
        p_phi = Y[3]
        psi = Y[4]
        p_psi = Y[5]

        y = np.zeros(6)

        y[0] = p_theta / I1
        y[1] = (p_phi - p_psi * np.cos(theta)) ** 2 * np.cos(theta) / (I1 * np.sin(theta) ** 3) - p_psi * (
                p_phi - p_psi * np.cos(theta)) / (I1 * np.sin(theta)) + M * g * l * np.sin(theta)
        y[2] = (p_phi - p_psi * np.cos(theta)) / (I1 * np.sin(theta) ** 2)
        y[3] = 0
        y[4] = p_psi / I3 - (p_phi - p_phi * np.cos(theta)) * np.cos(theta) / (I1 * np.sin(theta) ** 2)
        y[5] = 0
        return y


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mytest = spinning_top_frame()
    mytest.show()
    app.exec()
