from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class ViewDialog(QDialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumSize(500, 400)
        self.layout = QVBoxLayout(self)

        scroll = QScrollArea()
        content = QWidget()
        self.content_layout = QVBoxLayout(content)
        scroll.setWidget(content)
        scroll.setWidgetResizable(True)
        self.layout.addWidget(scroll)

    def add_field(self, label, value):
        field_layout = QHBoxLayout()
        label_widget = QLabel(f"{label}:")
        label_widget.setFont(QFont("Arial", 10, QFont.Bold))
        value_widget = QLabel(value)
        value_widget.setWordWrap(True)
        field_layout.addWidget(label_widget)
        field_layout.addWidget(value_widget, 1)
        self.content_layout.addLayout(field_layout)

    def add_image(self, pixmap):
        image_label = QLabel()
        image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(image_label)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'image_label'):
            self.image_label.setPixmap(self.original_pixmap.scaled(
                self.image_label.width(), self.image_label.height(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))