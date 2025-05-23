# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notificationsNSPoG.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_notificationWidget(object):
    def setupUi(self, notificationWidget):
        if not notificationWidget.objectName():
            notificationWidget.setObjectName(u"notificationWidget")
        notificationWidget.resize(414, 98)
        self.gridLayoutWidget = QWidget(notificationWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 341, 81))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.type = QLabel(self.gridLayoutWidget)
        self.type.setObjectName(u"type")

        self.gridLayout.addWidget(self.type, 0, 0, 1, 1)

        self.time = QLabel(self.gridLayoutWidget)
        self.time.setObjectName(u"time")

        self.gridLayout.addWidget(self.time, 1, 0, 1, 1)

        self.title = QLabel(self.gridLayoutWidget)
        self.title.setObjectName(u"title")

        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)

        self.description = QLabel(self.gridLayoutWidget)
        self.description.setObjectName(u"description")

        self.gridLayout.addWidget(self.description, 1, 1, 1, 1)

        self.deleteButton = QPushButton(notificationWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(340, 40, 75, 24))

        self.retranslateUi(notificationWidget)

        QMetaObject.connectSlotsByName(notificationWidget)
    # setupUi

    def retranslateUi(self, notificationWidget):
        notificationWidget.setWindowTitle(QCoreApplication.translate("notificationWidget", u"Form", None))
        self.type.setText(QCoreApplication.translate("notificationWidget", u"\u0422\u0438\u043f:", None))
        self.time.setText(QCoreApplication.translate("notificationWidget", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.title.setText(QCoreApplication.translate("notificationWidget", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.description.setText(QCoreApplication.translate("notificationWidget", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.deleteButton.setText(QCoreApplication.translate("notificationWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

