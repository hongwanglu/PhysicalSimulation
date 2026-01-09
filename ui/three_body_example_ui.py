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
## Form generated from reading UI file 'three_body_example.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Frame(object):
    def setupUi(self, three_body_example):
        if not three_body_example.objectName():
            three_body_example.setObjectName(u"three_body_example")
        three_body_example.resize(400, 300)
        self.gridLayout = QGridLayout(three_body_example)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_2 = QRadioButton(three_body_example)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)

        self.radioButton_5 = QRadioButton(three_body_example)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout.addWidget(self.radioButton_5, 2, 1, 1, 1)

        self.radioButton_3 = QRadioButton(three_body_example)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 3, 0, 1, 1)

        self.radioButton_6 = QRadioButton(three_body_example)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout.addWidget(self.radioButton_6, 3, 1, 1, 1)

        self.radioButton_1 = QRadioButton(three_body_example)
        self.radioButton_1.setObjectName(u"radioButton_1")

        self.gridLayout.addWidget(self.radioButton_1, 0, 0, 1, 1)

        self.radioButton_4 = QRadioButton(three_body_example)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout.addWidget(self.radioButton_4, 0, 1, 1, 1)

        QWidget.setTabOrder(self.radioButton_1, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.radioButton_4)
        QWidget.setTabOrder(self.radioButton_4, self.radioButton_5)
        QWidget.setTabOrder(self.radioButton_5, self.radioButton_6)

        self.retranslateUi(three_body_example)

        QMetaObject.connectSlotsByName(three_body_example)
    # setupUi

    def retranslateUi(self, three_body_example):
        three_body_example.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.radioButton_2.setText(QCoreApplication.translate("Frame", u"\u53cc\u6052\u661f\u5355\u884c\u661f", None))
        self.radioButton_5.setText(QCoreApplication.translate("Frame", u"\u884c\u8fdb\u7684\u87ba\u65cb\u7ebf", None))
        self.radioButton_3.setText(QCoreApplication.translate("Frame", u"\u7b49\u8fb9\u4e09\u89d2\u5f62", None))
        self.radioButton_6.setText(QCoreApplication.translate("Frame", u"\u81ea\u5b9a\u4e49", None))
        self.radioButton_1.setText(QCoreApplication.translate("Frame", u"\u5355\u6052\u661f\u53cc\u884c\u661f", None))
        self.radioButton_4.setText(QCoreApplication.translate("Frame", u"8\u5b57\u8fd0\u52a8\u7279\u89e3", None))
    # retranslateUi

