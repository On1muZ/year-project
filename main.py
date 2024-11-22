from re import U
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui_main import Ui_MainWindow
from utils import Number
from ui_settings import Ui_Dialog

accuracy = 10
max_symbols = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7,
    9: 8,
    10: 9,
    11: 'A',
    12: 'B',
    13: 'C',
    14: 'D',
    15: 'E',
    16: 'F',
    17: 'G',
    18: 'H',
    19: 'I',
    20: 'J',
    21: 'K',
    22: 'L',
    23: 'M',
    24: 'N',
    25: 'O',
    26: 'P',
    27: 'Q',
    28: 'R',
    29: 'S',
    30: 'T',
    31: 'U',
    32: 'V',
    33: 'W',
    34: 'X',
    35: 'Y',
    36: 'Z'
}

letters_number = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35
}

ALPHA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,."


class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.le_accuracy.setText(str(accuracy))
        self.ui.le_accuracy.textChanged.connect(self._on_le_accuracy_text_changed)
        self.ui.pushButton.clicked.connect(self._on_pushButton_clicked)

    def _on_pushButton_clicked(self):
        global accuracy
        if not self.ui.le_accuracy.text() in ('0', ''):
            accuracy = int(self.ui.le_accuracy.text())
            self.close()

    def _on_le_accuracy_text_changed(self, text):
        for i in text:
            if i not in "0123456789":
                self.ui.le_accuracy.setText(text[:len(text) - 1])
        if int(text) > 100:
            self.ui.le_accuracy.setText("100")
            


class BaseCalculator(QMainWindow):
    def __init__(self):
        super(BaseCalculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.setFixedSize(459, 607)
        self.ui.setupUi(self)

        self.ui.le_src_number.textChanged.connect(self._on_src_number_text_changed)
        self.ui.le_convert_base.textChanged.connect(self._on_convert_base_text_changed)
        self.ui.le_src_base.textChanged.connect(self._on_src_base_text_changed)
        self.ui.btn_settings.clicked.connect(self._on_btn_settings_clicked)

    def _on_src_number_text_changed(self, text):
        if text == '':
            self.ui.le_convert_bin.setText("")
            self.ui.le_convert_oct.setText("")
            self.ui.le_convert_dec.setText("")
            self.ui.le_convert_hex.setText("")
            self.ui.le_convert_number.setText("")
        elif text[len(text) - 1] in ALPHA or text[len(text) - 1] in ALPHA.lower():
            try:
                print(text)
                print(int(self.ui.le_src_base.text()))
                print(accuracy)
                
                number = Number(text.lower(), int(self.ui.le_src_base.text()), accuracy=accuracy)
                self.ui.le_convert_bin.setText(number.convert(2))
                self.ui.le_convert_oct.setText(number.convert(8))
                self.ui.le_convert_dec.setText(number.convert(10))
                self.ui.le_convert_hex.setText(number.convert(16))
                if self.ui.le_convert_base.text() != "":
                    self.ui.le_convert_number.setText(number.convert(int(self.ui.le_convert_base.text())))
            except ValueError:
                self.ui.le_convert_bin.setText("")
                self.ui.le_convert_oct.setText("")
                self.ui.le_convert_dec.setText("")
                self.ui.le_convert_hex.setText("")
                self.ui.le_convert_number.setText("")
                self.ui.le_src_number.setText(text[:len(text) - 1])
                return
        elif text[len(text) - 1] not in ALPHA:
            self.ui.le_src_number.setText(text[:len(text) - 1])
    
    def _on_convert_base_text_changed(self, text):
        if text == "1":
            return
        if text == '' or text == "0":
            self.ui.le_convert_number.setText("")
            self.ui.le_convert_base.setText("")
        elif text[len(text) - 1] not in "1234567890":
            self.ui.le_convert_base.setText(text[:len(text) - 1])
        elif int(text) > 36:
            self.ui.le_convert_base.setText("36")
        elif text[len(text) - 1] in "1234567890":
            try:
                number = Number(self.ui.le_src_number.text(), int(self.ui.le_src_base.text()), accuracy=accuracy)
                self.ui.le_convert_number.setText(number.convert(int(self.ui.le_convert_base.text())))
            except ValueError:
                return
    
    def _on_src_base_text_changed(self, text):
        if text == '' or text == "0":
            self.ui.le_convert_number.setText("")
            self.ui.le_src_base.setText("")
        elif text[len(text) - 1] not in "1234567890":
            self.ui.le_src_base.setText(text[:len(text) - 1])
        elif int(text) > 36:
            self.ui.le_src_base.setText("36")
        elif text[len(text) - 1] in "1234567890":
            try:
                number = Number(self.ui.le_src_number.text(), int(self.ui.le_src_base.text()), accuracy=accuracy)
                self.ui.le_convert_bin.setText(number.convert(2))
                self.ui.le_convert_oct.setText(number.convert(8))
                self.ui.le_convert_dec.setText(number.convert(10))
                self.ui.le_convert_hex.setText(number.convert(16))
                if self.ui.le_convert_base.text() != "":
                    self.ui.le_convert_number.setText(number.convert(int(self.ui.le_convert_base.text())))
            except ValueError:
                self.ui.le_convert_bin.setText("")
                self.ui.le_convert_oct.setText("")
                self.ui.le_convert_dec.setText("")
                self.ui.le_convert_hex.setText("")
                self.ui.le_convert_number.setText("")
    

    def _on_btn_settings_clicked(self):
        dialog = Dialog()
        dialog.exec()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BaseCalculator()
    window.show()
    sys.exit(app.exec())