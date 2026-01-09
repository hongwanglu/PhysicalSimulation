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
## Form generated from reading UI file 'spinning_top_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(648, 453)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.openGLWidget = QOpenGLWidget(Frame)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout.addWidget(self.openGLWidget, 0, 0, 1, 3)

        self.radioButton_1 = QRadioButton(Frame)
        self.radioButton_1.setObjectName(u"radioButton_1")

        self.gridLayout.addWidget(self.radioButton_1, 1, 0, 1, 1)

        self.radioButton_2 = QRadioButton(Frame)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.radioButton_3 = QRadioButton(Frame)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 1, 2, 1, 1)

        self.button_play = QPushButton(Frame)
        self.button_play.setObjectName(u"button_play")

        self.gridLayout.addWidget(self.button_play, 2, 0, 1, 1)

        self.button_pause = QPushButton(Frame)
        self.button_pause.setObjectName(u"button_pause")

        self.gridLayout.addWidget(self.button_pause, 2, 1, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.radioButton_1.setText(QCoreApplication.translate("Frame", u"\u8fdb\u52a8", None))
        self.radioButton_2.setText(QCoreApplication.translate("Frame", u"\u8fdb\u52a8\u4e0e\u7ae0\u52a8\u2160", None))
        self.radioButton_3.setText(QCoreApplication.translate("Frame", u"\u8fdb\u52a8\u4e0e\u7ae0\u52a8\u2161", None))
        self.button_play.setText(QCoreApplication.translate("Frame", u"play", None))
        self.button_pause.setText(QCoreApplication.translate("Frame", u"pause", None))
    # retranslateUi

