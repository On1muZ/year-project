import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from utils import Number


ALPHA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class BaseCalculator(QMainWindow):
    def __init__(self):
        super(BaseCalculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.setFixedSize(459, 607)
        self.ui.setupUi(self)

        self.ui.le_src_number.textChanged.connect(self._on_src_number_text_changed)
        self.ui.le_convert_base.textChanged.connect(self._on_convert_base_text_changed)
        self.ui.le_src_base.textChanged.connect(self._on_src_base_text_changed)

    def _on_src_number_text_changed(self, text):
        if text == '':
            self.ui.lbl_convert_bin.setText("")
            self.ui.lbl_convert_oct.setText("")
            self.ui.lbl_convert_dec.setText("")
            self.ui.lbl_convert_hex.setText("")
            self.ui.lbl_convert_number.setText("")
        elif text[len(text) - 1] in ALPHA:
            try:
                number = Number(text, int(self.ui.le_src_base.text()))
                self.ui.lbl_convert_bin.setText(number.convert(2))
                self.ui.lbl_convert_oct.setText(number.convert(8))
                self.ui.lbl_convert_dec.setText(number.convert(10))
                self.ui.lbl_convert_hex.setText(number.convert(16))
                if self.ui.le_convert_base.text() != "":
                    self.ui.lbl_convert_number.setText(number.convert(int(self.ui.le_convert_base.text())))
            except ValueError:
                self.ui.lbl_convert_bin.setText("")
                self.ui.lbl_convert_oct.setText("")
                self.ui.lbl_convert_dec.setText("")
                self.ui.lbl_convert_hex.setText("")
                self.ui.lbl_convert_number.setText("")
                return
        elif text[len(text) - 1] not in ALPHA:
            self.ui.le_src_number.setText(text[:len(text) - 1])
    
    def _on_convert_base_text_changed(self, text):
        if text == "1":
            return
        if text == '' or text == "0":
            self.ui.lbl_convert_number.setText("")
            self.ui.le_convert_base.setText("")
        elif text[len(text) - 1] not in "1234567890":
            self.ui.le_convert_base.setText(text[:len(text) - 1])
        elif int(text) > 32:
            self.ui.le_convert_base.setText("32")
        elif text[len(text) - 1] in "1234567890":
            try:
                number = Number(self.ui.le_src_number.text(), int(self.ui.le_src_base.text()))
                self.ui.lbl_convert_number.setText(number.convert(int(self.ui.le_convert_base.text())))
            except ValueError:
                return
    
    def _on_src_base_text_changed(self, text):
        if text == '' or text == "0":
            self.ui.lbl_convert_number.setText("")
            self.ui.le_src_base.setText("")
        elif text[len(text) - 1] not in "1234567890":
            self.ui.le_src_base.setText(text[:len(text) - 1])
        elif int(text) > 32:
            self.ui.le_src_base.setText("32")
        elif text[len(text) - 1] in "1234567890":
            try:
                number = Number(self.ui.le_src_number.text(), int(self.ui.le_src_base.text()))
                self.ui.lbl_convert_bin.setText(number.convert(2))
                self.ui.lbl_convert_oct.setText(number.convert(8))
                self.ui.lbl_convert_dec.setText(number.convert(10))
                self.ui.lbl_convert_hex.setText(number.convert(16))
                if self.ui.le_convert_base.text() != "":
                    self.ui.lbl_convert_number.setText(number.convert(int(self.ui.le_convert_base.text())))
            except ValueError:
                self.ui.lbl_convert_bin.setText("")
                self.ui.lbl_convert_oct.setText("")
                self.ui.lbl_convert_dec.setText("")
                self.ui.lbl_convert_hex.setText("")
                self.ui.lbl_convert_number.setText("")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BaseCalculator()
    window.show()
    sys.exit(app.exec())