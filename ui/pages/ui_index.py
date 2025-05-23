# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexaEAuJL.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QTimeEdit, QWidget)

class Ui_Index(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.timeDateInput = QDateEdit(Form)
        self.timeDateInput.setObjectName(u"timeDateInput")
        self.timeDateInput.setDateTime(QDateTime(QDate(2025, 5, 22), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.timeDateInput, 1, 0, 1, 1)

        self.timeTimeInput = QTimeEdit(Form)
        self.timeTimeInput.setObjectName(u"timeTimeInput")
        self.timeTimeInput.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(9, 0, 0)))

        self.gridLayout.addWidget(self.timeTimeInput, 1, 1, 1, 1)

        self.timeTitleInput = QLineEdit(Form)
        self.timeTitleInput.setObjectName(u"timeTitleInput")

        self.gridLayout.addWidget(self.timeTitleInput, 1, 2, 1, 1)

        self.timeDescriptionInput = QLineEdit(Form)
        self.timeDescriptionInput.setObjectName(u"timeDescriptionInput")

        self.gridLayout.addWidget(self.timeDescriptionInput, 1, 3, 1, 1)

        self.timeAddButton = QPushButton(Form)
        self.timeAddButton.setObjectName(u"timeAddButton")

        self.gridLayout.addWidget(self.timeAddButton, 1, 4, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)

        self.waitTimeInput = QSpinBox(Form)
        self.waitTimeInput.setObjectName(u"waitTimeInput")

        self.gridLayout.addWidget(self.waitTimeInput, 3, 0, 1, 2)

        self.waitTitleInput = QLineEdit(Form)
        self.waitTitleInput.setObjectName(u"waitTitleInput")

        self.gridLayout.addWidget(self.waitTitleInput, 3, 2, 1, 1)

        self.waitDescriptionInput = QLineEdit(Form)
        self.waitDescriptionInput.setObjectName(u"waitDescriptionInput")

        self.gridLayout.addWidget(self.waitDescriptionInput, 3, 3, 1, 1)

        self.waitAddButton = QPushButton(Form)
        self.waitAddButton.setObjectName(u"waitAddButton")

        self.gridLayout.addWidget(self.waitAddButton, 3, 4, 1, 1)

        self.notificationsListButton = QPushButton(Form)
        self.notificationsListButton.setObjectName(u"notificationsListButton")

        self.gridLayout.addWidget(self.notificationsListButton, 4, 4, 1, 1)

        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 4, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435 \u0441 \u043f\u0440\u0438\u0432\u044f\u0437\u043a\u043e\u0439 \u043a \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.timeTitleInput.setPlaceholderText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.timeDescriptionInput.setPlaceholderText(QCoreApplication.translate("Form", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.timeAddButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435 \u0441 \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u043e\u0439 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445", None))
        self.waitTitleInput.setPlaceholderText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.waitDescriptionInput.setPlaceholderText(QCoreApplication.translate("Form", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.waitAddButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.notificationsListButton.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0441\u043f\u0438\u0441\u043a\u0430 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
    # retranslateUi

