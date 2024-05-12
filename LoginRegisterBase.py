import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap

class LoginRegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Call A Doctor (CaD)")
        self.setFixedSize(850, 500)
        self.setStyleSheet("background-color: white;")

        layout = QHBoxLayout()

        # Add QLabel with scaled down image
        image_label = QLabel()
        pixmap = QPixmap("MainPic.jpg")  # Change "your_image_path.jpg" to the path of your image
        pixmap = pixmap.scaled(500, 500)  # Scale down the pixmap to desired size
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        button_layout = QVBoxLayout()

        # Add login button
        login_button = QPushButton("Login")
        login_button.setFixedSize(300, 100)
        login_button.setStyleSheet("background-color: lightgreen; color: black; font-size: 20px;")
        login_button.clicked.connect(self.open_login_page)
        button_layout.addWidget(login_button)

        # Add register button
        register_button = QPushButton("Register")
        register_button.setFixedSize(300, 100)
        register_button.clicked.connect(self.open_register_page)
        register_button.setStyleSheet("background-color: lightgreen; color: vblack; font-size: 20px;")
        button_layout.addWidget(register_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def open_login_page(self):
        self.hide()
        login_page = LoginPage()
        login_page.show()

    def open_register_page(self):
        self.hide()
        register_page = RegisterPage()
        register_page.show()

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()

        # Add login widgets here

        self.setLayout(layout)

class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register Page")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()

        # Add registration widgets here

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginRegistrationWindow()
    window.show()
    sys.exit(app.exec())
