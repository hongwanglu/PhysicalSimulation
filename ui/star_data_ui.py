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

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'star_data.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSlider, QStatusBar,
    QTabWidget, QWidget)

class Ui_star_data(object):
    def setupUi(self, star_data):
        if not star_data.objectName():
            star_data.setObjectName(u"star_data")
        star_data.resize(773, 476)
        self.centralwidget = QWidget(star_data)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(773, 451))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Slider_y1 = QSlider(self.tab_1)
        self.Slider_y1.setObjectName(u"Slider_y1")
        self.Slider_y1.setMinimum(-1000)
        self.Slider_y1.setMaximum(1000)
        self.Slider_y1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider_y1, 2, 1, 1, 1)

        self.label_vy1 = QLabel(self.tab_1)
        self.label_vy1.setObjectName(u"label_vy1")

        self.gridLayout.addWidget(self.label_vy1, 5, 0, 1, 1)

        self.Slider_vz1 = QSlider(self.tab_1)
        self.Slider_vz1.setObjectName(u"Slider_vz1")
        self.Slider_vz1.setMinimum(-100)
        self.Slider_vz1.setMaximum(100)
        self.Slider_vz1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider_vz1, 6, 1, 1, 1)

        self.Slider_x1 = QSlider(self.tab_1)
        self.Slider_x1.setObjectName(u"Slider_x1")
        self.Slider_x1.setMinimum(-1000)
        self.Slider_x1.setMaximum(1000)
        self.Slider_x1.setValue(500)
        self.Slider_x1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider_x1, 1, 1, 1, 1)

        self.Slider_vy1 = QSlider(self.tab_1)
        self.Slider_vy1.setObjectName(u"Slider_vy1")
        self.Slider_vy1.setMinimum(-100)
        self.Slider_vy1.setMaximum(100)
        self.Slider_vy1.setValue(6)
        self.Slider_vy1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider_vy1, 5, 1, 1, 1)

        self.label_x1 = QLabel(self.tab_1)
        self.label_x1.setObjectName(u"label_x1")

        self.gridLayout.addWidget(self.label_x1, 1, 0, 1, 1)

        self.label_vz1 = QLabel(self.tab_1)
        self.label_vz1.setObjectName(u"label_vz1")

        self.gridLayout.addWidget(self.label_vz1, 6, 0, 1, 1)

        self.label_y1 = QLabel(self.tab_1)
        self.label_y1.setObjectName(u"label_y1")

        self.gridLayout.addWidget(self.label_y1, 2, 0, 1, 1)

        self.label_vx1 = QLabel(self.tab_1)
        self.label_vx1.setObjectName(u"label_vx1")

        self.gridLayout.addWidget(self.label_vx1, 4, 0, 1, 1)

        self.Slider_z1 = QSlider(self.tab_1)
        self.Slider_z1.setObjectName(u"Slider_z1")
        self.Slider_z1.setMinimum(-1000)
        self.Slider_z1.setMaximum(1000)
        self.Slider_z1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider_z1, 3, 1, 1, 1)

        self.Slider_vx1 = QSlider(self.tab_1)
        self.Slider_vx1.setObjectName(u"Slider_vx1")
        self.Slider_vx1.setMinimum(-100)
        self.Slider_vx1.setMaximum(100)
        self.Slider_vx1.setValue(0)
        self.Slider_vx1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider_vx1, 4, 1, 1, 1)

        self.label_z1 = QLabel(self.tab_1)
        self.label_z1.setObjectName(u"label_z1")

        self.gridLayout.addWidget(self.label_z1, 3, 0, 1, 1)

        self.label_m1 = QLabel(self.tab_1)
        self.label_m1.setObjectName(u"label_m1")

        self.gridLayout.addWidget(self.label_m1, 0, 0, 1, 1)

        self.Slider_m1 = QSlider(self.tab_1)
        self.Slider_m1.setObjectName(u"Slider_m1")
        self.Slider_m1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Slider_m1.setMinimum(1)
        self.Slider_m1.setMaximum(1000)
        self.Slider_m1.setSingleStep(1)
        self.Slider_m1.setValue(25)
        self.Slider_m1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Slider_m1, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 17)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Slider_vx2 = QSlider(self.tab_2)
        self.Slider_vx2.setObjectName(u"Slider_vx2")
        self.Slider_vx2.setMinimum(-100)
        self.Slider_vx2.setMaximum(100)
        self.Slider_vx2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_vx2, 4, 1, 1, 1)

        self.Slider_vz2 = QSlider(self.tab_2)
        self.Slider_vz2.setObjectName(u"Slider_vz2")
        self.Slider_vz2.setMinimum(-100)
        self.Slider_vz2.setMaximum(100)
        self.Slider_vz2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_vz2, 6, 1, 1, 1)

        self.label_z2 = QLabel(self.tab_2)
        self.label_z2.setObjectName(u"label_z2")

        self.gridLayout_2.addWidget(self.label_z2, 3, 0, 1, 1)

        self.label_vz2 = QLabel(self.tab_2)
        self.label_vz2.setObjectName(u"label_vz2")

        self.gridLayout_2.addWidget(self.label_vz2, 6, 0, 1, 1)

        self.Slider_vy2 = QSlider(self.tab_2)
        self.Slider_vy2.setObjectName(u"Slider_vy2")
        self.Slider_vy2.setMinimum(-100)
        self.Slider_vy2.setMaximum(100)
        self.Slider_vy2.setValue(-6)
        self.Slider_vy2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_vy2, 5, 1, 1, 1)

        self.Slider_x2 = QSlider(self.tab_2)
        self.Slider_x2.setObjectName(u"Slider_x2")
        self.Slider_x2.setMinimum(-1000)
        self.Slider_x2.setMaximum(1000)
        self.Slider_x2.setValue(-500)
        self.Slider_x2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_x2, 1, 1, 1, 1)

        self.label_vx2 = QLabel(self.tab_2)
        self.label_vx2.setObjectName(u"label_vx2")

        self.gridLayout_2.addWidget(self.label_vx2, 4, 0, 1, 1)

        self.Slider_z2 = QSlider(self.tab_2)
        self.Slider_z2.setObjectName(u"Slider_z2")
        self.Slider_z2.setMinimum(-1000)
        self.Slider_z2.setMaximum(1000)
        self.Slider_z2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_z2, 3, 1, 1, 1)

        self.label_y2 = QLabel(self.tab_2)
        self.label_y2.setObjectName(u"label_y2")

        self.gridLayout_2.addWidget(self.label_y2, 2, 0, 1, 1)

        self.label_x2 = QLabel(self.tab_2)
        self.label_x2.setObjectName(u"label_x2")

        self.gridLayout_2.addWidget(self.label_x2, 1, 0, 1, 1)

        self.Slider_y2 = QSlider(self.tab_2)
        self.Slider_y2.setObjectName(u"Slider_y2")
        self.Slider_y2.setMinimum(-1000)
        self.Slider_y2.setMaximum(1000)
        self.Slider_y2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_y2, 2, 1, 1, 1)

        self.label_vy2 = QLabel(self.tab_2)
        self.label_vy2.setObjectName(u"label_vy2")

        self.gridLayout_2.addWidget(self.label_vy2, 5, 0, 1, 1)

        self.label_m2 = QLabel(self.tab_2)
        self.label_m2.setObjectName(u"label_m2")

        self.gridLayout_2.addWidget(self.label_m2, 0, 0, 1, 1)

        self.Slider_m2 = QSlider(self.tab_2)
        self.Slider_m2.setObjectName(u"Slider_m2")
        self.Slider_m2.setMinimum(1)
        self.Slider_m2.setMaximum(1000)
        self.Slider_m2.setValue(25)
        self.Slider_m2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_m2, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 5)
        self.gridLayout_2.setColumnStretch(1, 17)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Slider_y3 = QSlider(self.tab_3)
        self.Slider_y3.setObjectName(u"Slider_y3")
        self.Slider_y3.setMinimum(-1000)
        self.Slider_y3.setMaximum(1000)
        self.Slider_y3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.Slider_y3, 3, 1, 1, 1)

        self.Slider_m3 = QSlider(self.tab_3)
        self.Slider_m3.setObjectName(u"Slider_m3")
        self.Slider_m3.setMinimum(1)
        self.Slider_m3.setMaximum(1000)
        self.Slider_m3.setValue(25)
        self.Slider_m3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.Slider_m3, 1, 1, 1, 1)

        self.Slider_vy3 = QSlider(self.tab_3)
        self.Slider_vy3.setObjectName(u"Slider_vy3")
        self.Slider_vy3.setMinimum(-100)
        self.Slider_vy3.setMaximum(100)
        self.Slider_vy3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.Slider_vy3, 6, 1, 1, 1)

        self.Slider_x3 = QSlider(self.tab_3)
        self.Slider_x3.setObjectName(u"Slider_x3")
        self.Slider_x3.setMinimum(-1000)
        self.Slider_x3.setMaximum(1000)
        self.Slider_x3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.Slider_x3, 2, 1, 1, 1)

        self.Slider_z3 = QSlider(self.tab_3)
        self.Slider_z3.setObjectName(u"Slider_z3")
        self.Slider_z3.setMinimum(-1000)
        self.Slider_z3.setMaximum(1000)
        self.Slider_z3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.Slider_z3, 4, 1, 1, 1)

        self.Slider_vx3 = QSlider(self.tab_3)
        self.Slider_vx3.setObjectName(u"Slider_vx3")
        self.Slider_vx3.setMinimum(-100)
        self.Slider_vx3.setMaximum(100)
        self.Slider_vx3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.Slider_vx3, 5, 1, 1, 1)

        self.label_m3 = QLabel(self.tab_3)
        self.label_m3.setObjectName(u"label_m3")

        self.gridLayout_3.addWidget(self.label_m3, 1, 0, 1, 1)

        self.Slider_vz3 = QSlider(self.tab_3)
        self.Slider_vz3.setObjectName(u"Slider_vz3")
        self.Slider_vz3.setMinimum(-100)
        self.Slider_vz3.setMaximum(100)
        self.Slider_vz3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.Slider_vz3, 7, 1, 1, 1)

        self.label_x3 = QLabel(self.tab_3)
        self.label_x3.setObjectName(u"label_x3")

        self.gridLayout_3.addWidget(self.label_x3, 2, 0, 1, 1)

        self.label_y3 = QLabel(self.tab_3)
        self.label_y3.setObjectName(u"label_y3")

        self.gridLayout_3.addWidget(self.label_y3, 3, 0, 1, 1)

        self.label_z3 = QLabel(self.tab_3)
        self.label_z3.setObjectName(u"label_z3")

        self.gridLayout_3.addWidget(self.label_z3, 4, 0, 1, 1)

        self.label_vx3 = QLabel(self.tab_3)
        self.label_vx3.setObjectName(u"label_vx3")

        self.gridLayout_3.addWidget(self.label_vx3, 5, 0, 1, 1)

        self.label_vy3 = QLabel(self.tab_3)
        self.label_vy3.setObjectName(u"label_vy3")

        self.gridLayout_3.addWidget(self.label_vy3, 6, 0, 1, 1)

        self.label_vz3 = QLabel(self.tab_3)
        self.label_vz3.setObjectName(u"label_vz3")

        self.gridLayout_3.addWidget(self.label_vz3, 7, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 5)
        self.gridLayout_3.setColumnStretch(1, 17)
        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        star_data.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(star_data)
        self.statusbar.setObjectName(u"statusbar")
        star_data.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.Slider_m1, self.Slider_x1)
        QWidget.setTabOrder(self.Slider_x1, self.Slider_y1)
        QWidget.setTabOrder(self.Slider_y1, self.Slider_z1)
        QWidget.setTabOrder(self.Slider_z1, self.Slider_vx1)
        QWidget.setTabOrder(self.Slider_vx1, self.Slider_vy1)
        QWidget.setTabOrder(self.Slider_vy1, self.Slider_vz1)
        QWidget.setTabOrder(self.Slider_vz1, self.Slider_m2)
        QWidget.setTabOrder(self.Slider_m2, self.Slider_x2)
        QWidget.setTabOrder(self.Slider_x2, self.Slider_y2)
        QWidget.setTabOrder(self.Slider_y2, self.Slider_z2)
        QWidget.setTabOrder(self.Slider_z2, self.Slider_vx2)
        QWidget.setTabOrder(self.Slider_vx2, self.Slider_vy2)
        QWidget.setTabOrder(self.Slider_vy2, self.Slider_vz2)
        QWidget.setTabOrder(self.Slider_vz2, self.Slider_m3)
        QWidget.setTabOrder(self.Slider_m3, self.Slider_x3)
        QWidget.setTabOrder(self.Slider_x3, self.Slider_y3)
        QWidget.setTabOrder(self.Slider_y3, self.Slider_z3)
        QWidget.setTabOrder(self.Slider_z3, self.Slider_vx3)
        QWidget.setTabOrder(self.Slider_vx3, self.Slider_vy3)
        QWidget.setTabOrder(self.Slider_vy3, self.Slider_vz3)
        QWidget.setTabOrder(self.Slider_vz3, self.tabWidget)

        self.retranslateUi(star_data)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(star_data)
    # setupUi

    def retranslateUi(self, star_data):
        star_data.setWindowTitle(QCoreApplication.translate("star_data", u"Star Data", None))
        self.label_vy1.setText(QCoreApplication.translate("star_data", u"vy(*10^3):6.0", None))
        self.label_x1.setText(QCoreApplication.translate("star_data", u"x:500.0", None))
        self.label_vz1.setText(QCoreApplication.translate("star_data", u"vz(*10^3):0.0", None))
        self.label_y1.setText(QCoreApplication.translate("star_data", u"y:0.0", None))
        self.label_vx1.setText(QCoreApplication.translate("star_data", u"vx(*10^3):0.0", None))
        self.label_z1.setText(QCoreApplication.translate("star_data", u"z:0.0", None))
        self.label_m1.setText(QCoreApplication.translate("star_data", u"mass(*10^19):25.0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("star_data", u"Planet 1", None))
        self.label_z2.setText(QCoreApplication.translate("star_data", u"z:0.0", None))
        self.label_vz2.setText(QCoreApplication.translate("star_data", u"vz(*10^3):0.0", None))
        self.label_vx2.setText(QCoreApplication.translate("star_data", u"vx(*10^3):0.0", None))
        self.label_y2.setText(QCoreApplication.translate("star_data", u"y:0.0", None))
        self.label_x2.setText(QCoreApplication.translate("star_data", u"x:-500.0", None))
        self.label_vy2.setText(QCoreApplication.translate("star_data", u"vy(*10^3):-6.0", None))
        self.label_m2.setText(QCoreApplication.translate("star_data", u"mass(*10^19):25.0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("star_data", u"Planet 2", None))
        self.label_m3.setText(QCoreApplication.translate("star_data", u"mass(*10^19):25.0", None))
        self.label_x3.setText(QCoreApplication.translate("star_data", u"x:0.0", None))
        self.label_y3.setText(QCoreApplication.translate("star_data", u"y:0.0", None))
        self.label_z3.setText(QCoreApplication.translate("star_data", u"z:0.0", None))
        self.label_vx3.setText(QCoreApplication.translate("star_data", u"vx(*10^3):0.0", None))
        self.label_vy3.setText(QCoreApplication.translate("star_data", u"vy(*10^3):0.0", None))
        self.label_vz3.setText(QCoreApplication.translate("star_data", u"vz(*10^3):0.0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("star_data", u"Planet 3", None))
    # retranslateUi

