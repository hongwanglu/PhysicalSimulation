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
## Form generated from reading UI file 'movement_data.ui'
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
    QSizePolicy, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1056, 547)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.openGLWidget = QOpenGLWidget(Frame)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout.addWidget(self.openGLWidget, 0, 0, 1, 1)

        self.label_x_t = QLabel(Frame)
        self.label_x_t.setObjectName(u"label_x_t")

        self.gridLayout.addWidget(self.label_x_t, 3, 0, 1, 1)

        self.label_vx_t = QLabel(Frame)
        self.label_vx_t.setObjectName(u"label_vx_t")

        self.gridLayout.addWidget(self.label_vx_t, 1, 0, 1, 1)

        self.openGLWidget_2 = QOpenGLWidget(Frame)
        self.openGLWidget_2.setObjectName(u"openGLWidget_2")

        self.gridLayout.addWidget(self.openGLWidget_2, 0, 1, 1, 1)

        self.openGLWidget_3 = QOpenGLWidget(Frame)
        self.openGLWidget_3.setObjectName(u"openGLWidget_3")

        self.gridLayout.addWidget(self.openGLWidget_3, 2, 0, 1, 1)

        self.label_vy_t = QLabel(Frame)
        self.label_vy_t.setObjectName(u"label_vy_t")

        self.gridLayout.addWidget(self.label_vy_t, 1, 1, 1, 1)

        self.label_y_t = QLabel(Frame)
        self.label_y_t.setObjectName(u"label_y_t")

        self.gridLayout.addWidget(self.label_y_t, 3, 1, 1, 1)

        self.openGLWidget_4 = QOpenGLWidget(Frame)
        self.openGLWidget_4.setObjectName(u"openGLWidget_4")

        self.gridLayout.addWidget(self.openGLWidget_4, 2, 1, 1, 1)

        self.openGLWidget_5 = QOpenGLWidget(Frame)
        self.openGLWidget_5.setObjectName(u"openGLWidget_5")

        self.gridLayout.addWidget(self.openGLWidget_5, 0, 2, 3, 1)

        self.label_v_t = QLabel(Frame)
        self.label_v_t.setObjectName(u"label_v_t")

        self.gridLayout.addWidget(self.label_v_t, 3, 2, 1, 1)

        self.gridLayout.setRowStretch(0, 8)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 8)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 8)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_x_t.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p align=\"center\">x-t</p></body></html>", None))
        self.label_vx_t.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p align=\"center\">vx-t</p></body></html>", None))
        self.label_vy_t.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p align=\"center\">vy-t</p></body></html>", None))
        self.label_y_t.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p align=\"center\">y-t</p></body></html>", None))
        self.label_v_t.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p align=\"center\">v-t</p></body></html>", None))
    # retranslateUi

