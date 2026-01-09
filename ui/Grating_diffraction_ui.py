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

# Grating_diffraction_ui.py
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PySide6 import QtCore

class MplWidget(QtWidgets.QWidget):
    def __init__(self, status_bar, parent=None):
        super(MplWidget, self).__init__(parent)
        self.status_bar = status_bar
        self.lines = []
        self.y_coords = []  # 用于保存 y 坐标
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas.mpl_connect('button_press_event', self.on_mouse_click)
        
    def on_mouse_move(self, event):
        if event.inaxes:
            xdata, ydata = event.xdata, event.ydata
            # 更新状态栏或其他部分
            self.status_bar.showMessage(f"X: {xdata:.5f}m, Y: {ydata:.5f}m")
            
    def on_mouse_click(self, event):
        if event.inaxes:
            # 获取鼠标点击的 y 坐标
            y = event.ydata
            self.y_coords.append(y)
            # 对 y 坐标数组进行排序
            self.y_coords.sort(reverse=True)  # 从大到小排序

            # 绘制一条红色直线
            line = event.inaxes.axhline(y=y, color='red', linewidth=1.0)
            self.lines.append(line)
            # 刷新图表
            self.canvas.draw()
            
    def clear_lines(self):
        for line in self.lines:
            line.remove()
        self.lines.clear()
        self.y_coords = []
        self.canvas.draw()
            
    def plot(self, data, x_min, x_max):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.imshow(data, cmap='gray', extent=[x_min, x_max, -0.01, 0.01])
        self.canvas.draw()


class GratingDiffractionFrame(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 75, 67, 17))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 67, 17))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 185, 67, 17))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 67, 17))
        self.label_5.setObjectName("label_5")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 91, 31))
        self.textEdit.setObjectName("textEdit")
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 95, 91, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 150, 91, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 205, 91, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 260, 91, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 91, 31))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 340, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 380, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 10, 451, 411))
        self.groupBox.setObjectName("Plot")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 28))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plotLayout = QtWidgets.QVBoxLayout(self.groupBox)  # 将布局添加到 GroupBox
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grating Diffraction Simulator"))
        self.label.setText(_translate("MainWindow", "光波频率"))
        self.label_2.setText(_translate("MainWindow", "光栅频率"))
        self.label_3.setText(_translate("MainWindow", "光波波长"))
        self.label_4.setText(_translate("MainWindow", "空间起点"))
        self.label_5.setText(_translate("MainWindow", "空间终点"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "Result"))
        self.groupBox.setTitle(_translate("MainWindow", "Plot"))
