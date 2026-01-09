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
## Form generated from reading UI file 'movement_air_frame.ui'
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(796, 669)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openGLWidget_3 = QOpenGLWidget(Frame)
        self.openGLWidget_3.setObjectName(u"openGLWidget_3")

        self.verticalLayout.addWidget(self.openGLWidget_3)

        self.control_area_3 = QGridLayout()
        self.control_area_3.setObjectName(u"control_area_3")
        self.Slider_vy_2 = QSlider(Frame)
        self.Slider_vy_2.setObjectName(u"Slider_vy_2")
        self.Slider_vy_2.setOrientation(Qt.Horizontal)

        self.control_area_3.addWidget(self.Slider_vy_2, 7, 1, 1, 1)

        self.Slider_radius_2 = QSlider(Frame)
        self.Slider_radius_2.setObjectName(u"Slider_radius_2")
        self.Slider_radius_2.setOrientation(Qt.Horizontal)

        self.control_area_3.addWidget(self.Slider_radius_2, 3, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_3.addItem(self.verticalSpacer_13, 6, 1, 1, 1)

        self.label_radius_2 = QLabel(Frame)
        self.label_radius_2.setObjectName(u"label_radius_2")

        self.control_area_3.addWidget(self.label_radius_2, 3, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_3.addItem(self.verticalSpacer_9, 4, 1, 1, 1)

        self.Slider_mass_2 = QSlider(Frame)
        self.Slider_mass_2.setObjectName(u"Slider_mass_2")
        self.Slider_mass_2.setOrientation(Qt.Horizontal)

        self.control_area_3.addWidget(self.Slider_mass_2, 1, 1, 1, 1)

        self.label_vy_2 = QLabel(Frame)
        self.label_vy_2.setObjectName(u"label_vy_2")

        self.control_area_3.addWidget(self.label_vy_2, 7, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_3.addItem(self.verticalSpacer_11, 8, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_3.addItem(self.verticalSpacer_10, 2, 1, 1, 1)

        self.label_mass_2 = QLabel(Frame)
        self.label_mass_2.setObjectName(u"label_mass_2")

        self.control_area_3.addWidget(self.label_mass_2, 1, 0, 1, 1)

        self.label_vx_2 = QLabel(Frame)
        self.label_vx_2.setObjectName(u"label_vx_2")

        self.control_area_3.addWidget(self.label_vx_2, 5, 0, 1, 1)

        self.Slider_vx_2 = QSlider(Frame)
        self.Slider_vx_2.setObjectName(u"Slider_vx_2")
        self.Slider_vx_2.setOrientation(Qt.Horizontal)

        self.control_area_3.addWidget(self.Slider_vx_2, 5, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_3.addItem(self.verticalSpacer_12, 0, 1, 1, 1)

        self.pushButton = QPushButton(Frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.control_area_3.addWidget(self.pushButton, 0, 2, 9, 1)

        self.control_area_3.setColumnStretch(0, 15)
        self.control_area_3.setColumnStretch(1, 85)
        self.control_area_3.setColumnStretch(2, 10)

        self.verticalLayout.addLayout(self.control_area_3)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_radius_2.setText(QCoreApplication.translate("Frame", u"radius:", None))
        self.label_vy_2.setText(QCoreApplication.translate("Frame", u"vy:", None))
        self.label_mass_2.setText(QCoreApplication.translate("Frame", u"mass:", None))
        self.label_vx_2.setText(QCoreApplication.translate("Frame", u"vx:", None))
        self.pushButton.setText(QCoreApplication.translate("Frame", u"\u8be6\u7ec6\u4fe1\u606f", None))
    # retranslateUi

