import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapHomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Main layout
        main_layout = QVBoxLayout()
        
        # Top layout for the logout button
        top_layout = QHBoxLayout()
        top_layout.addStretch()  # This makes the button move to the right
        logout_button = QPushButton('Logout')
        top_layout.addWidget(logout_button)
        main_layout.addLayout(top_layout)
        
        # Web view for Healthsites.io map
        map_view = QWebEngineView()
        map_view.setUrl(QUrl("https://healthsites.io/map"))
        map_layout = QVBoxLayout()
        map_layout.setContentsMargins(0, 0, 0, 0)
        map_layout.addWidget(map_view)
        
        map_widget = QWidget()
        map_widget.setLayout(map_layout)

        # Search bar and search button container
        search_container = QWidget(map_widget)
        search_container_layout = QHBoxLayout()
        search_container_layout.setContentsMargins(0, 0, 0, 0)
        search_container.setLayout(search_container_layout)
        
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        search_button = QPushButton("🔍")
        
        search_container_layout.addStretch()  # Push the search bar and button to the right
        search_container_layout.addWidget(search_bar)
        search_container_layout.addWidget(search_button)

        # Position search container inside map_widget
        search_container.setGeometry(map_view.width() - 250, 10, 240, 30)  # Adjust position and size as needed

        main_layout.addWidget(map_widget)

        # Bottom layout for the 4 buttons
        bottom_layout = QHBoxLayout()
        
        profile_button = QPushButton('Profile/Home')
        health_record_button = QPushButton('Health Record')
        payment_button = QPushButton('Payment')
        appointment_button = QPushButton('Appointment')

        bottom_layout.addWidget(profile_button)
        bottom_layout.addWidget(health_record_button)
        bottom_layout.addWidget(payment_button)
        bottom_layout.addWidget(appointment_button)

        main_layout.addLayout(bottom_layout)

        main_widget.setLayout(main_layout)

        # Window properties
        self.setWindowTitle('Call a Doctor - Homepage')
        self.setGeometry(100, 100, 800, 600)
        self.show()

        # Make sure the search container stays in the correct position when resized
        map_view.resizeEvent = self.resize_search_container

    def resize_search_container(self, event):
        self.findChild(QWidget, 'search_container').setGeometry(
            self.findChild(QWebEngineView).width() - 250, 10, 240, 30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapHomePage()
    sys.exit(app.exec_())
