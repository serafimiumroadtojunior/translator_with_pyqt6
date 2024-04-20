# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uimain.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(661, 309)
        icon = QIcon()
        icon.addFile(u"icons/main_app_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"    border: 1px solid rgba(255, 246, 246,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"    background-color: rgb(62, 75, 75)\n"
"}\n"
"\n"
"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 16px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} \n"
"\n"
"QWidget{\n"
"    background-color: rgb(22, 54, 56);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    opacity: 0.2;\n"
"    transition: all 0.5s;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(62, 75, 75);\n"
"    border-radius: 10"
                        "px;\n"
"    border: none;\n"
"} \n"
"\n"
"QComboBox{\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    background-color:rgb(86, 83, 90);\n"
"    border-radius: 10px;\n"
"    border:1px solid rgb(113, 111, 117);\n"
"	color:white;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"    background-color:rgb(86, 83, 90)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 641, 291))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(13, 40, 271, 181))
        self.plainTextEdit_2 = QPlainTextEdit(self.frame)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(360, 40, 271, 181))
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 271, 22))
        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(360, 10, 271, 22))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 240, 41, 31))
        icon1 = QIcon()
        icon1.addFile(u"icons/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 240, 41, 31))
        icon2 = QIcon()
        icon2.addFile(u"icons/voice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(440, 240, 41, 31))
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(32, 32))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(530, 240, 41, 31))
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(32, 32))
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(254, 232, 141, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.plainTextEdit_2.setReadOnly(True)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.languages = {"Russian": "ru", "English": "en", "Ukrainian": "uk", "Germany": "de", "France": "fr", "Spanish": "es", "Italian":"it", "Polish": "pl"} 
        self.comboBox.addItems(self.languages.keys())
        self.comboBox_2.addItems(self.languages.keys())
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Result", None))
    # retranslateUi