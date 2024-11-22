# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowtFALXN.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(459, 607)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        MainWindow.setToolTipDuration(1)
        MainWindow.setStyleSheet(u"background-color: #1f1f1f;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #1f1f1f\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 371, 51))
        self.label.setStyleSheet(u"font-size: 23px;\n"
"background-color: rgb(75, 75, 75);\n"
"font-weight: bold;\n"
"color: white;\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.le_src_base = QLineEdit(self.centralwidget)
        self.le_src_base.setObjectName(u"le_src_base")
        self.le_src_base.setGeometry(QRect(10, 140, 91, 61))
        self.le_src_base.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(57, 57, 57);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 101, 16))
        self.label_3.setStyleSheet(u"font-size: 17px;\n"
"font-weight: bold;\n"
"color: white;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 260, 91, 61))
        self.label_6.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 330, 91, 61))
        self.label_7.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 400, 91, 61))
        self.label_8.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 470, 91, 61))
        self.label_9.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_convert_base = QLineEdit(self.centralwidget)
        self.le_convert_base.setObjectName(u"le_convert_base")
        self.le_convert_base.setGeometry(QRect(10, 540, 91, 61))
        self.le_convert_base.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(57, 57, 57);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 171, 41))
        self.label_5.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;\n"
"background-color: rgb(49, 49, 49);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 210, 251, 41))
        self.label_10.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;\n"
"background-color: rgb(49, 49, 49);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(390, 10, 61, 51))
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_settings.setStyleSheet(u"border: 1px solid rgb(61, 61, 61);\n"
"background-color: rgb(57, 57, 57);\n"
"border-radius: 10px")
        icon = QIcon()
        icon.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QSize(40, 40))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 120, 311, 20))
        self.label_4.setStyleSheet(u"font-size: 17px;\n"
"font-weight: bold;\n"
"color: white;")
        self.le_src_number = QLineEdit(self.centralwidget)
        self.le_src_number.setObjectName(u"le_src_number")
        self.le_src_number.setGeometry(QRect(120, 140, 331, 61))
        self.le_src_number.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(57, 57, 57);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_convert_bin = QLineEdit(self.centralwidget)
        self.le_convert_bin.setObjectName(u"le_convert_bin")
        self.le_convert_bin.setGeometry(QRect(120, 260, 331, 61))
        self.le_convert_bin.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_convert_bin.setReadOnly(True)
        self.le_convert_oct = QLineEdit(self.centralwidget)
        self.le_convert_oct.setObjectName(u"le_convert_oct")
        self.le_convert_oct.setGeometry(QRect(120, 330, 331, 61))
        self.le_convert_oct.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_convert_oct.setReadOnly(True)
        self.le_convert_dec = QLineEdit(self.centralwidget)
        self.le_convert_dec.setObjectName(u"le_convert_dec")
        self.le_convert_dec.setGeometry(QRect(120, 400, 331, 61))
        self.le_convert_dec.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_convert_dec.setReadOnly(True)
        self.le_convert_hex = QLineEdit(self.centralwidget)
        self.le_convert_hex.setObjectName(u"le_convert_hex")
        self.le_convert_hex.setGeometry(QRect(120, 470, 331, 61))
        self.le_convert_hex.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_convert_hex.setReadOnly(True)
        self.le_convert_number = QLineEdit(self.centralwidget)
        self.le_convert_number.setObjectName(u"le_convert_number")
        self.le_convert_number.setGeometry(QRect(120, 540, 331, 61))
        self.le_convert_number.setStyleSheet(u"font-size: 24px;\n"
"background-color: rgb(40, 40, 40);\n"
"border: 1px solid rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"color: white;")
        self.le_convert_number.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 \u0441\u0438\u0441\u0442\u0435\u043c \u0441\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f", None))
        self.le_src_base.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.btn_settings.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e ", None))
        self.le_convert_number.setText("")
    # retranslateUi

