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

# Grating_diffraction.py
import sys
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtWidgets import QInputDialog, QMessageBox
import ui.Grating_diffraction_ui as ui_module

GratingDiffractionFrame = ui_module.GratingDiffractionFrame
MplWidget = ui_module.MplWidget

c = 3.000 * (10 ** 8)

def source(t, x, y, x0, y0, w):
    r = ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
    wave = np.cos(w * (t - r / c))
    return wave

def wavefront(t, y, A, ks, ws):
    x = A * np.cos(ks * y) * np.cos(ws * t)
    return x

def f(t, x, y, x0, y0, w):
    sum_wave = source(t, x, y, x0[0], y0[0], w)
    for i in range(1, len(y0)):
        sum_wave = np.add(source(t, x, y, x0[i], y0[i], w), sum_wave)
    return sum_wave ** 2

def calculate_result(y_coords, ws):
    if len(y_coords) < 4:
        return 0  # 如果数组元素不足以进行计算，则返回 0 

    sum_diff = 0
    for i in range(len(y_coords) // 2):
        sum_diff += (y_coords[i] - y_coords[i + 3]) * 2

    result = sum_diff / (3 * (len(y_coords) // 2)) * ws / (2 * np.pi)
    return result

def generate_and_display_data(w, ws, l, x_min, x_max):
    dn = 3.014 * (10 ** (-6))
    ks = ws / 1500.0
    A = dn * l

    x = np.linspace(x_min, x_max, 1000)
    y = np.linspace(-0.01, 0.01, 1000)
    xs, ys = np.meshgrid(x, y)
    y0 = np.arange(-0.008, 0.008, 0.00001)
    x0 = wavefront(0, y0, A, ks, ws)
    i2 = f(0, xs, ys, x0, y0, w)
    
    for i in range(1, 51):
        x0 = wavefront(i * (2 * np.pi) / (50 * ws), y0, A, ks, ws)
        i2 = np.add(f(i * (2 * np.pi) / (50 * ws), xs, ys, x0, y0, w), i2)

    return i2

class MainApp(QtWidgets.QMainWindow, GratingDiffractionFrame):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)

        # 创建 Matplotlib Widget
        self.mplWidget = MplWidget(self.statusbar)
        self.plotLayout.addWidget(self.mplWidget)
        
        # 连接按钮事件
        self.pushButton.clicked.connect(self.on_start_clicked)
        self.pushButton_3.clicked.connect(self.mplWidget.clear_lines)
        self.pushButton_4.clicked.connect(self.on_result_clicked)

    def on_start_clicked(self):
        # 从文本框获取用户输入
        w = float(self.textEdit.toPlainText())
        ws = float(self.textEdit_2.toPlainText())
        l = float(self.textEdit_3.toPlainText())
        x_min = float(self.textEdit_4.toPlainText())
        x_max = float(self.textEdit_5.toPlainText())

        # 生成并显示数据
        data = generate_and_display_data(w, ws, l, x_min, x_max)
        self.mplWidget.plot(data, x_min, x_max)

    def on_result_clicked(self):
        # 调用计算函数
        ws = float(self.textEdit_2.toPlainText())
        calculated_result = calculate_result(self.mplWidget.y_coords, ws)

        # 显示计算结果
        msg_box = QMessageBox()
        msg_box.setText(f"Calculated Result: {calculated_result:.2f}m/s")
        msg_box.setWindowTitle("Result")
        msg_box.exec()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainApp()
    main.show()
    sys.exit(app.exec())
