from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QSlider, QSpacerItem
)
from PySide6.QtGui import QPainter, QColor, QConicalGradient, QMouseEvent
from PySide6.QtCore import Qt, QPointF
from math import atan2, degrees, radians, sqrt, cos, sin
from ui_main import Ui_MainWindow


color_is_changed = [False]

class ColorWheel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(250, 250)  # Устанавливаем размер виджета
        self.selected_color = QColor(255, 255, 255)  # Начальный выбранный цвет — белый
        self.cursor_position = QPointF(self.width() / 2, self.height() / 2)  # Курсор в центре круга
        self.default_color = QColor(200, 200, 200)  # Стандартный цвет программы
        self.color_is_changed = False
    def paintEvent(self, event):
        painter = QPainter(self)  # Создаем объект для рисования
        painter.setRenderHint(QPainter.Antialiasing)  # Включаем сглаживание

        # Создаем градиент для цветового круга
        gradient = QConicalGradient(self.width() / 2, self.height() / 2, 0)
        for i in range(361):  # Добавляем цвета для каждого угла
            hue = i / 360.0
            gradient.setColorAt(hue, QColor.fromHsvF(hue, 1, 1))
        painter.setBrush(gradient)
        painter.drawEllipse(0, 0, self.width(), self.height())  # Рисуем цветовой круг

        # Рисуем белый круг внутри цветового круга
        painter.setBrush(Qt.white)
        inner_offset = 80
        painter.drawEllipse(
            inner_offset,
            inner_offset,
            self.width() - 2 * inner_offset,
            self.height() - 2 * inner_offset,
        )

        # Рисуем индикатор выбора цвета
        painter.setBrush(Qt.white)  # Белый цвет индикатора
        painter.setPen(Qt.black)  # Черная рамка индикатора
        cursor_radius = 10
        center = QPointF(self.width() / 2, self.height() / 2)
        dist = sqrt((self.cursor_position.x() - center.x()) ** 2 + (self.cursor_position.y() - center.y()) ** 2)
        outer_radius = self.width() / 2 - cursor_radius

        # Корректируем позицию индикатора, если он выходит за границы
        if dist > outer_radius:
            dx = self.cursor_position.x() - center.x()
            dy = self.cursor_position.y() - center.y()
            scale = outer_radius / dist
            self.cursor_position = QPointF(center.x() + dx * scale, center.y() + dy * scale)

        # Рисуем индикатор
        painter.drawEllipse(
            self.cursor_position.x() - cursor_radius,
            self.cursor_position.y() - cursor_radius,
            cursor_radius * 2,
            cursor_radius * 2,
        )

    def mousePressEvent(self, event: QMouseEvent):
        self.update_color(event.pos())  # Обновляем цвет при нажатии

    def mouseMoveEvent(self, event: QMouseEvent):
        self.update_color(event.pos())  # Обновляем цвет при движении

    def update_color(self, pos):
        center = QPointF(self.width() / 2, self.height() / 2)
        dist = sqrt((pos.x() - center.x()) ** 2 + (pos.y() - center.y()) ** 2)

        outer_radius = self.width() / 2
        inner_radius = 50

        # Если курсор внутри белого круга — ставим стандартный цвет
        if dist <= inner_radius:
            self.selected_color = self.default_color
            self.parent().update_background(self.default_color)
        elif inner_radius < dist < outer_radius:
            self.cursor_position = pos
            dx = pos.x() - center.x()
            dy = pos.y() - center.y()
            angle = (degrees(atan2(-dy, dx)) + 360) % 360

            hue = angle / 360.0
            self.selected_color = QColor.fromHsvF(hue, 1, 1)
            self.parent().update_background(self.selected_color)
        else:
            # Корректируем положение курсора
            if dist >= outer_radius:
                dx = pos.x() - center.x()
                dy = pos.y() - center.y()
                scale = outer_radius / dist
                self.cursor_position = QPointF(center.x() + dx * scale, center.y() + dy * scale)
            elif dist <= inner_radius:
                dx = pos.x() - center.x()
                dy = pos.y() - center.y()
                scale = inner_radius / dist
                self.cursor_position = QPointF(center.x() + dx * scale, center.y() + dy * scale)

        self.update()  # Перерисовываем виджет
        self.color_is_changed = True

    def set_brightness(self, brightness):
        self.brightness = brightness
        self.update()

    def set_color_by_rgb(self, r, g, b):
        # Устанавливаем цвет по RGB
        self.selected_color = QColor(r, g, b)
        hsv = self.selected_color.toHsv()
        center = QPointF(self.width() / 2, self.height() / 2)
        radius = self.width() / 2
        angle = radians(hsv.hue())
        saturation = hsv.saturation() / 255.0
        x = center.x() + cos(angle) * saturation * radius
        y = center.y() + sin(angle) * saturation * radius
        self.selector_pos = QPointF(x, y)
        self.update()

# Класс ColorPicker — главное окно
class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Picker")
        self.setGeometry(100, 100, 300, 400)

        self.color_wheel = ColorWheel(self)
        self.brightness_slider = QSlider(Qt.Horizontal, self)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(255)
        self.brightness_slider.setValue(255)
        self.brightness_slider.valueChanged.connect(self.update_background)
        self.color_is_changed = False
        layout = QVBoxLayout(self)
        layout.addWidget(self.color_wheel)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)
        layout.addWidget(self.brightness_slider)
        self.setLayout(layout)


    def update_background(self, color=None):
        color = self.color_wheel.selected_color
        color = color.toRgb()
        r = color.red()
        g = color.green()
        b = color.blue()
        self.color_is_changed = True
        brightness = self.brightness_slider.value() / 255.0
        adjusted_color = QColor.fromHsvF(color.hueF(), color.saturationF(), brightness)
        self.setStyleSheet(f"background-color: {adjusted_color.name()};")
        self.parent().setStyleSheet(f"background-color: {adjusted_color.name()};")
        self.parent().findChild(QLabel, "label").setStyleSheet(
            u"font-size: 23px;\n"
            f"background-color: rgb({r*brightness*0.9}, {g*brightness*0.9}, {b*brightness*0.9});\n"
            "color: white;\n"
            "font-weight: bold;\n"
            "border: 1px solid rgb(61, 61, 61);\n"
            "border-radius: 10px;"
        )
        self.parent().findChild(QLabel, "label_10").setStyleSheet(
            u"font-size: 15px;\n"
            f"background-color: rgb({r*brightness*0.6}, {g*brightness*0.6}, {b*brightness*0.6});\n"
            "border: 1px solid rgb(61, 61, 61);\n"
            "border-radius: 10px;\n"
            "color: white;")
        self.parent().findChild(QLineEdit, "le_accuracy").setStyleSheet(
            u"font-size: 24px;\n"
            f"background-color: rgb({r*brightness*0.6}, {g*brightness*0.6}, {b*brightness*0.6});\n"
            "border: 1px solid rgb(61, 61, 61);\n"
            "border-radius: 10px;\n"
            "color: white;")
        self.parent().findChild(QPushButton, "pushButton").setStyleSheet(
            u"border: 1px solid rgb(61, 61, 61);\n"
            f"background-color: rgb({r*brightness*0.6}, {g*brightness*0.6}, {b*brightness*0.6});\n"
            "border-radius: 10px;\n"
            "font-size: 20px;\n"
            "font-weight: bold;\n"
            "color: white;")        


class Ui_Dialog(object):
    def get_current_color(self):
        pass
    def setupUi(self, Dialog, r = None, g = None, b = None, brightness = None):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 552)
        self.r = r
        self.g = g
        self.b = b
        Dialog.setMinimumSize(QSize(418, 552))
        Dialog.setMaximumSize(QSize(418, 552))
        if r is not None:
            Dialog.setStyleSheet(f"background-color: rgb({r*brightness}, {g*brightness}, {b*brightness});")
        else:
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
        
        self.color_picker = ColorPicker()  # Assuming ColorPicker is already defined as in the original code
        self.color_picker.setParent(Dialog)
        self.color_picker.setGeometry(QRect(10, 120, 400, 300))

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 490, 121, 51))
        self.pushButton.setStyleSheet(u"border: 1px solid rgb(61, 61, 61);\n"
            "background-color: rgb(57, 57, 57);\n"
            "border-radius: 10px;\n"
            "font-size: 20px;\n"
            "font-weight: bold;\n"
            "color: white;")
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439:", None))
        self.le_accuracy.setText(QCoreApplication.translate("Dialog", u"10", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi
