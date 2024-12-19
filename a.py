from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QSlider
)
from PySide6.QtGui import QPainter, QColor, QConicalGradient, QMouseEvent
from PySide6.QtCore import Qt, QPointF
from math import atan2, degrees, sqrt


class ColorWheel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 200)
        self.selected_color = QColor(255, 255, 255)
        self.cursor_position = QPointF(self.width() / 2, self.height() / 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Create color wheel gradient
        gradient = QConicalGradient(self.width() / 2, self.height() / 2, 0)
        for i in range(361):
            hue = i / 360.0
            gradient.setColorAt(hue, QColor.fromHsvF(hue, 1, 1))
        painter.setBrush(gradient)
        painter.drawEllipse(0, 0, self.width(), self.height())

        # Draw smaller inner white circle
        painter.setBrush(Qt.white)
        inner_offset = 50
        painter.drawEllipse(
            inner_offset,
            inner_offset,
            self.width() - 2 * inner_offset,
            self.height() - 2 * inner_offset,
        )

        # Draw selection indicator (white circle at selected position)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.black)
        cursor_radius = 10

        # Ensure the indicator circle doesn't overflow the color wheel
        center = QPointF(self.width() / 2, self.height() / 2)
        dist = sqrt((self.cursor_position.x() - center.x()) ** 2 + (self.cursor_position.y() - center.y()) ** 2)
        outer_radius = self.width() / 2 - cursor_radius  # Reduce radius to account for cursor size
        if dist > outer_radius:
            # Adjust position to stay within bounds
            dx = self.cursor_position.x() - center.x()
            dy = self.cursor_position.y() - center.y()
            scale = outer_radius / dist
            self.cursor_position = QPointF(center.x() + dx * scale, center.y() + dy * scale)

        painter.drawEllipse(
            self.cursor_position.x() - cursor_radius,
            self.cursor_position.y() - cursor_radius,
            cursor_radius * 2,
            cursor_radius * 2,
        )

    def mousePressEvent(self, event: QMouseEvent):
        self.update_color(event.pos())

    def mouseMoveEvent(self, event: QMouseEvent):
        self.update_color(event.pos())

    def update_color(self, pos):
        center = QPointF(self.width() / 2, self.height() / 2)
        dist = sqrt((pos.x() - center.x()) ** 2 + (pos.y() - center.y()) ** 2)

        outer_radius = self.width() / 2
        inner_radius = 60  # Offset for the inner white circle

        if inner_radius < dist < outer_radius:  # Ensure it's within the wheel
            self.cursor_position = pos
            dx = pos.x() - self.width() / 2
            dy = pos.y() - self.height() / 2
            angle = (degrees(atan2(-dy, dx)) + 360) % 360

            hue = angle / 360.0
            self.selected_color = QColor.fromHsvF(hue, 1, 1)
            self.parent().update_background()
        else:
            # Restrict the cursor to stay within valid bounds
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

        self.update()  # Redraw the widget to show changes


class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Picker")
        self.setGeometry(100, 100, 400, 500)

        self.color_wheel = ColorWheel(self)
        self.brightness_slider = QSlider(Qt.Horizontal, self)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(255)
        self.brightness_slider.setValue(255)
        self.brightness_slider.valueChanged.connect(self.update_background)

        layout = QVBoxLayout(self)
        layout.addWidget(self.color_wheel)
        layout.addWidget(self.brightness_slider)
        self.setLayout(layout)

    def update_background(self):
        color = self.color_wheel.selected_color
        brightness = self.brightness_slider.value() / 255.0
        adjusted_color = QColor.fromHsvF(
            color.hueF(), color.saturationF(), brightness
        )
        self.setStyleSheet(f"background-color: {adjusted_color.name()};")


if __name__ == "__main__":
    app = QApplication([])
    picker = ColorPicker()
    picker.show()
    app.exec()
