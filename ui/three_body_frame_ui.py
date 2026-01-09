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
## Form generated from reading UI file 'three_body_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, three_body_frame):
        if not three_body_frame.objectName():
            three_body_frame.setObjectName(u"three_body_frame")
        three_body_frame.resize(971, 720)
        self.verticalLayout = QVBoxLayout(three_body_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openGLWidget = QOpenGLWidget(three_body_frame)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.verticalLayout.addWidget(self.openGLWidget)

        self.control_area_1 = QGridLayout()
        self.control_area_1.setObjectName(u"control_area_1")
        self.control_area_1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_1.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.button_settings = QPushButton(three_body_frame)
        self.button_settings.setObjectName(u"button_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(sizePolicy)
        self.button_settings.setMinimumSize(QSize(0, 35))
        self.button_settings.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.control_area_1.addWidget(self.button_settings, 1, 0, 1, 1)

        self.button_pause = QPushButton(three_body_frame)
        self.button_pause.setObjectName(u"button_pause")
        sizePolicy.setHeightForWidth(self.button_pause.sizePolicy().hasHeightForWidth())
        self.button_pause.setSizePolicy(sizePolicy)
        self.button_pause.setMinimumSize(QSize(0, 35))

        self.control_area_1.addWidget(self.button_pause, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_1.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.control_area_1.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.button_play = QPushButton(three_body_frame)
        self.button_play.setObjectName(u"button_play")
        sizePolicy.setHeightForWidth(self.button_play.sizePolicy().hasHeightForWidth())
        self.button_play.setSizePolicy(sizePolicy)
        self.button_play.setMinimumSize(QSize(0, 35))

        self.control_area_1.addWidget(self.button_play, 3, 0, 1, 1)

        self.button_reset = QPushButton(three_body_frame)
        self.button_reset.setObjectName(u"button_reset")
        sizePolicy.setHeightForWidth(self.button_reset.sizePolicy().hasHeightForWidth())
        self.button_reset.setSizePolicy(sizePolicy)
        self.button_reset.setMinimumSize(QSize(0, 35))

        self.control_area_1.addWidget(self.button_reset, 1, 1, 1, 1)

        self.button_clear = QPushButton(three_body_frame)
        self.button_clear.setObjectName(u"button_clear")
        sizePolicy.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy)
        self.button_clear.setMinimumSize(QSize(0, 35))

        self.control_area_1.addWidget(self.button_clear, 1, 2, 1, 1)

        self.button_more = QPushButton(three_body_frame)
        self.button_more.setObjectName(u"button_more")
        sizePolicy.setHeightForWidth(self.button_more.sizePolicy().hasHeightForWidth())
        self.button_more.setSizePolicy(sizePolicy)
        self.button_more.setMinimumSize(QSize(0, 35))

        self.control_area_1.addWidget(self.button_more, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.control_area_1)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 3)
        QWidget.setTabOrder(self.button_settings, self.button_reset)
        QWidget.setTabOrder(self.button_reset, self.button_clear)
        QWidget.setTabOrder(self.button_clear, self.button_play)
        QWidget.setTabOrder(self.button_play, self.button_pause)
        QWidget.setTabOrder(self.button_pause, self.button_more)

        self.retranslateUi(three_body_frame)

        QMetaObject.connectSlotsByName(three_body_frame)
    # setupUi

    def retranslateUi(self, three_body_frame):
        three_body_frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.button_settings.setText(QCoreApplication.translate("Frame", u"Settings", None))
        self.button_pause.setText(QCoreApplication.translate("Frame", u"Pause", None))
        self.button_play.setText(QCoreApplication.translate("Frame", u"Play", None))
        self.button_reset.setText(QCoreApplication.translate("Frame", u"Reset", None))
        self.button_clear.setText(QCoreApplication.translate("Frame", u"Clear", None))
        self.button_more.setText(QCoreApplication.translate("Frame", u"More", None))
    # retranslateUi

