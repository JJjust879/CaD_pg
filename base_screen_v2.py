from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
                             QPushButton, QListWidget, QLabel, QFrame, QComboBox)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

class CustomListItem(QFrame):
    def __init__(self, id, main_text, sub_text, parent=None):
        super().__init__(parent)
        self.id = id
        layout = QVBoxLayout(self)
        
        main_label = QLabel(main_text)
        main_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(main_label)
        
        sub_label = QLabel(sub_text)
        layout.addWidget(sub_label)
        
        self.setFrameShape(QFrame.StyledPanel)
        self.setLineWidth(1)

class BaseScreen(QWidget):
    item_selected = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Search and Sort
        top_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.filter_items)
        top_layout.addWidget(self.search_input)

        self.sort_combo = QComboBox()
        self.sort_combo.currentIndexChanged.connect(self.on_sort_changed)
        top_layout.addWidget(self.sort_combo)

        self.sort_order_button = QPushButton()
        self.sort_order_button.setIcon(QIcon("C:/Users/nmubu/Desktop/CaD/icon/sort-up-solid.svg"))  
        self.sort_order_button.clicked.connect(self.toggle_sort_order)
        top_layout.addWidget(self.sort_order_button)

        self.layout.addLayout(top_layout)

        # List widget
        self.list_widget = QListWidget()
        self.list_widget.setSpacing(5)
        self.list_widget.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.layout.addWidget(self.list_widget)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        self.edit_button.setEnabled(False)
        self.delete_button.setEnabled(False)
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        self.layout.addLayout(button_layout)

    def filter_items(self, text):
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            widget = self.list_widget.itemWidget(item)
            if text.lower() in widget.findChild(QLabel).text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def on_item_double_clicked(self, item):
        self.item_selected.emit(self.list_widget.itemWidget(item).id)

    def toggle_sort_order(self):
        # This method will be implemented in child classes
        pass

    def load_data(self):
        # This method will be implemented in child classes
        pass