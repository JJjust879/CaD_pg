import sys
import os
import folium
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
)
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import subprocess

# Import PersonalHealthRecordWindow from health_rec.py
from health_rec import PersonalHealthRecordWindow


class MapHomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.marker_data = []  # Initialize the marker_data attribute
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
        self.map_view.setZoomFactor(1.0)  # Set the zoom factor for responsive map

        map_layout = QVBoxLayout()
        map_layout.setContentsMargins(0, 0, 0, 0)
        map_layout.addWidget(self.map_view)

        map_widget = QWidget()
        map_widget.setLayout(map_layout)
        main_layout.addWidget(map_widget)

        # Bottom layout for the 3 buttons (Profile/Home, Health Record, Appointment)
        bottom_layout = QHBoxLayout()

        profile_button = QPushButton('Profile/Home')
        profile_button.clicked.connect(self.launch_profile_window)
        health_record_button = QPushButton('Health Record')
        health_record_button.clicked.connect(self.launch_health_record_window)
        appointment_button = QPushButton('Appointment')
        appointment_button.clicked.connect(self.open_appointment_system)

        button_style = """
            QPushButton {
                font-size: 30px;
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker Green */
            }
            QPushButton:pressed {
                background-color: #3e8e41; /* Even Darker Green */
            }
        """

        profile_button.setStyleSheet(button_style)
        health_record_button.setStyleSheet(button_style)
        appointment_button.setStyleSheet(button_style)

        bottom_layout.addWidget(profile_button)
        bottom_layout.addWidget(health_record_button)
        bottom_layout.addWidget(appointment_button)

        main_layout.addLayout(bottom_layout)
        main_widget.setLayout(main_layout)

        # Window properties
        self.setWindowTitle('Call a Doctor - Homepage')
        self.setGeometry(100, 100, 1920, 1080)  # Set window size to 1920x1080
        self.setStyleSheet("background-color: #f0f0f0;")  # Light gray background
        self.show()

    def generate_map(self):
        map_center = [5.4164, 100.3327]
        map_zoom = 14
        folium_map = folium.Map(location=map_center, zoom_start=map_zoom)

    # List of marker locations and information
        self.marker_data = [
            (5.4177714, 100.3414535, "Clinic B.S Tan", "21, Lebuh Gereja, George Town, 10450 George Town, Pulau Pinang", "04-261 8345", "MON - FRI 10:00AM - 19:00PM"),
            (5.4119546, 100.3327547, "Clinic Lee", "29, Jalan Magazine, 10300 George Town, Pulau Pinang", "04-262 7831", "DAILY 09:30AM - 16:00PM"),
            (5.4034401, 100.3087052, "Clinic SIngapore", "823-G-03 MK13, Kejora Business Point, 5, Jln Paya Terubung, 11900 Bayan Lepas, Penang", "04-644 8488", "DAILY 09:00AM - 22:00PM"),
            (5.4245510, 100.3196080, "Clinic Tropica", "231 E, Jalan Burma, 10050 George Town, Pulau Pinang", "04-226 6196", "MON - FRI, SUN 08:30AM - 12:00PM"),
            (5.4300548, 100.3128159, "Clinic Koe", "289, Jalan Burma, Pulau Tikus, 10350 George Town, Pulau Pinang", "04-227 0404", "MON - SAT 08:30AM - 17:00PM"),
            (5.3904299, 100.2841750, "Clinic Medivirion", "12, Medan Angsana 1, Bandar Baru, 11500 Ayer Itam, Pulau Pinang", "04-829 7295", "MON - SAT 09:00AM - 21:00PM"),
            (5.2997739, 100.2619749, "Clinic Kesihatan Bayan Lepas", "Jalan Dato Ismail Hashim, 11900 Bayan Lepas, Pulau Pinang", "04-643 5434", "MON - FRI 08:00AM - 17:00PM"),
            (5.2884594, 100.2813290, "Clinic Kare", "No. 25, 1, Lintang Batu Maung 1, 11960 Batu Maung, Penang", "04-611 7205", "DAILY 08:30AM - 20:00PM"),
            (5.3503266, 100.2973872, "Clinic Health Plus", "725-U, Jalan Sungai Dua, Desa Permai Indah, 11700 Gelugor, Pulau Pinang", "04-657 7750", "DAILY 08:00AM - 20:00PM"),
            (5.3503266, 100.2973872, "Clinic Bayan Baru", "Jalan Tengah, 11950 Bayan Lepas, Pulau Pinang", "04-642 5102", "MON - SAT 08:00AM - 21:00PM")
    ]

    # Add markers to the map
        for lat, lon, name, address, phone, hours in self.marker_data:
            html = f"""
                <style>
                    h3, p {{ font-size: 30px; }}  /* Adjust the font size as desired */
                </style>
                <h3>{name}</h3>
                <p><b>Address:</b> {address}</p>
                <p><b>Phone:</b> {phone}</p>
                <p><b>Opening Hours:</b> {hours}</p>
            """
            iframe = folium.IFrame(html=html, width=500, height=300)
            popup = folium.Popup(iframe, max_width=500)
            folium.Marker(location=[lat, lon], popup=popup, icon=folium.Icon(color='red', icon='info-sign', prefix='fa', icon_color='white', icon_weight=1), radius=20).add_to(folium_map)

    # Save the map to an HTML file in the same directory as the script
        map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "map.html")
        folium_map.save(map_path)

    def launch_profile_window(self):
        subprocess.Popen(["python", "Profile_v1.py"])  # Adjust path as needed

    def launch_health_record_window(self):
        self.health_record_window = PersonalHealthRecordWindow()
        self.health_record_window.show()

    def open_appointment_system(self):
        from Appoint_v1 import AppointmentSystem
        self.appointment_system = AppointmentSystem()
        self.appointment_system.show()

    def logout(self):
        print("Logout button clicked.")
        self.close()  # Close the main window

    def on_load_finished(self, ok):
        if ok:
            print("Map loaded successfully.")
        else:
            print("Failed to load the page. Please check the URL or your internet connection.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapHomePage()
    sys.exit(app.exec_())
