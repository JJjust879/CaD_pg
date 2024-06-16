import sys
import os
import folium
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

class MapHomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Generate the map with folium
        self.generate_map()

        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Main layout
        main_layout = QVBoxLayout()

        # Top layout for the logout button
        top_layout = QHBoxLayout()
        top_layout.addStretch()  # This makes the button move to the right
        logout_button = QPushButton('Logout')
        logout_button.clicked.connect(self.logout)  # Connect logout button to logout method
        top_layout.addWidget(logout_button)
        main_layout.addLayout(top_layout)

        # Web view for folium map
        self.map_view = QWebEngineView()
        map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "map.html")
        self.map_view.setUrl(QUrl.fromLocalFile(map_path))
        self.map_view.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.map_view.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.map_view.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.map_view.loadFinished.connect(self.on_load_finished)

        map_layout = QVBoxLayout()
        map_layout.setContentsMargins(0, 0, 0, 0)
        map_layout.addWidget(self.map_view)

        map_widget = QWidget()
        map_widget.setLayout(map_layout)

        # Search bar and search button container
        search_container = QWidget(map_widget)
        search_container.setObjectName("search_container")
        search_container_layout = QHBoxLayout()
        search_container_layout.setContentsMargins(0, 0, 0, 0)
        search_container.setLayout(search_container_layout)

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        search_bar.setFixedHeight(100)  # Increase the height of the search bar
        search_bar.setStyleSheet("font-size: 16px;")  # Increase the font size

        search_button = QPushButton("🔍")
        search_button.setFixedHeight(100)  # Increase the height of the button
        search_button.setFixedWidth(100)  # Increase the width of the button
        search_button.setStyleSheet("font-size: 16px;")  # Increase the font size

        search_container_layout.addStretch()  # Push the search bar and button to the right
        search_container_layout.addWidget(search_bar)
        search_container_layout.addWidget(search_button)

        # Position search container inside map_widget
        search_container.setGeometry(self.map_view.width() - 500, 10, 300, 60)  # Adjust position and size as needed

        main_layout.addWidget(map_widget)

        # Bottom layout for the 3 buttons
        bottom_layout = QHBoxLayout()

        profile_button = QPushButton('Profile/Home')
        health_record_button = QPushButton('Health Record')
        appointment_button = QPushButton('Appointment')

        profile_button.setFixedHeight(100)
        health_record_button.setFixedHeight(100)
        appointment_button.setFixedHeight(100)

        profile_button.setStyleSheet("font-size: 30px; background-color: #FF0000;")  # Red background
        health_record_button.setStyleSheet("font-size: 30px; background-color: #FF0000;")  # Red background
        appointment_button.setStyleSheet("font-size: 30px; background-color: #FF0000;")  # Red background

        bottom_layout.addWidget(profile_button)
        bottom_layout.addWidget(health_record_button)
        bottom_layout.addWidget(appointment_button)

        main_layout.addLayout(bottom_layout)

        main_widget.setLayout(main_layout)

        # Window properties
        self.setWindowTitle('Call a Doctor - Homepage')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #ADD8E6;")  # Set background color to light blue
        self.show()

        # Make sure the search container stays in the correct position when resized
        self.map_view.resizeEvent = self.resize_search_container

    def resize_search_container(self, event):
        self.findChild(QWidget, 'search_container').setGeometry(
            self.findChild(QWebEngineView).width() - 300, 10, 280, 40)

    def on_load_finished(self, ok):
        if ok:
            print("Map loaded successfully.")
        else:
            print("Failed to load the page. Please check the URL or your internet connection.")

    def generate_map(self):
        map_center = [5.4164, 100.3327]
        map_zoom = 12
        folium_map = folium.Map(location=map_center, zoom_start=map_zoom)

        # List of marker locations
        marker_locations = [
            (5.4177714, 100.3414535),
            (5.4119546, 100.3327547),
            (5.4034401, 100.3087052),
            (5.4245510, 100.3196080),
            (5.4300548, 100.3128159),
            (5.3904299, 100.2841750),
            (5.2997739, 100.2619749),
            (5.2884594, 100.2813290),
            (5.3503266, 100.2973872),
            (5.3503266, 100.2973872)
        ]

        # Add markers to the map
        for location in marker_locations:
            folium.Marker(location=location, popup=f"Marker at {location}").add_to(folium_map)

        # Save the map to an HTML file in the same directory as the script
        map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "map.html")
        folium_map.save(map_path)

    def logout(self):
        # Method to handle logout action
        print("Logout button clicked.")
        self.close()  # Close the main window
        sys.exit()   # Exit the application

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapHomePage()
    sys.exit(app.exec_())
