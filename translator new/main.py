import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow
from uimain_ui import Ui_MainWindow
import pyttsx3
from googletrans import Translator


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.translator = Translator()
        self.engine = pyttsx3.init() 
        self.ui.pushButton_5.clicked.connect(self.trans) 
        self.ui.pushButton.clicked.connect(self.copy_text1) 
        self.ui.pushButton_2.clicked.connect(self.voice1) 
        self.ui.pushButton_3.clicked.connect(self.voice2) 
        self.ui.pushButton_4.clicked.connect(self.copy_text2) 

    def trans(self):
        language = self.ui.comboBox_2.currentText() 
        suffix = self.ui.languages[language]
        text = self.ui.plainTextEdit.toPlainText() 
        translation = self.translator.translate(text, dest=suffix)
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_2.setPlainText(translation.text) 

    def copy_text1(self):
            text_to_copy = self.ui.plainTextEdit.toPlainText()
            QApplication.clipboard().clear()
            QApplication.clipboard().setText(text_to_copy)

    def copy_text2(self):
            text_to_copy = self.ui.plainTextEdit_2.toPlainText()
            QApplication.clipboard().clear()
            QApplication.clipboard().setText(text_to_copy)

    def voice1(self):
        get_language1 = self.ui.comboBox.currentText() 
        text1 = self.ui.plainTextEdit.toPlainText().strip()
        if text1:
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('voice', get_language1)
            self.engine.say(text1)
            self.engine.runAndWait()

    def voice2(self):
        get_language1 = self.ui.comboBox_2.currentText() 
        text1 = self.ui.plainTextEdit_2.toPlainText().strip()
        if text1:
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('voice', get_language1)
            self.engine.say(text1)
            self.engine.runAndWait()

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())
