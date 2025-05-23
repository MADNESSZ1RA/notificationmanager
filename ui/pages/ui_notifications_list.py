# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notifications_listgempLr.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_notificationLayout(object):
    def setupUi(self, notificationLayout):
        if not notificationLayout.objectName():
            notificationLayout.setObjectName(u"notificationLayout")
        notificationLayout.resize(550, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(notificationLayout.sizePolicy().hasHeightForWidth())
        notificationLayout.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(notificationLayout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(notificationLayout)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 530, 200))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.exitButton = QPushButton(notificationLayout)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout.addWidget(self.exitButton)


        self.retranslateUi(notificationLayout)

        QMetaObject.connectSlotsByName(notificationLayout)
    # setupUi

    def retranslateUi(self, notificationLayout):
        notificationLayout.setWindowTitle(QCoreApplication.translate("notificationLayout", u"Form", None))
        self.exitButton.setText(QCoreApplication.translate("notificationLayout", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

