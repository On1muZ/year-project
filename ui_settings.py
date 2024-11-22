# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogDeTdpD.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 188)
        Dialog.setStyleSheet(u"background-color: #1f1f1f;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 401, 51))
        self.label.setStyleSheet(u"font-size: 23px;\n"
"background-color: rgb(75, 75, 75);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 70, 191, 40))
        self.label_10.setStyleSheet(u"font-size: 15px;\n"
"background-color: rgb(49, 49, 49);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_accuracy = QLineEdit(Dialog)
        self.le_accuracy.setObjectName(u"le_accuracy")
        self.le_accuracy.setGeometry(QRect(220, 70, 191, 41))
        self.le_accuracy.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(57, 57, 57);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 121, 51))
        self.pushButton.setStyleSheet(u"border: 1px solid rgb(61, 61, 61);\n"
"background-color: rgb(57, 57, 57);\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: white;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439:", None))
        self.le_accuracy.setText(QCoreApplication.translate("Dialog", u"10", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi
