from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QSizePolicy, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from database import fetch_records

class PersonalHealthRecordWindow(QMainWindow):
    def __init__(self, patient_id):
        super().__init__()
        self.patient_id = patient_id
        self.setWindowTitle("Health Record")
        self.resize(1920, 1080)  # Set window size to 1920x1080

        # Initialize the logout_btn here
        self.logout_btn = QPushButton("Logout", clicked=self.logout)
        self.logout_btn.setFont(QFont("Helvetica", 14))
        self.logout_btn.setMinimumHeight(30)  # Increase vertical size

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        scroll_area = QScrollArea()  # Scroll area to make the window scrollable
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setWidget(central_widget)

        self.setCentralWidget(scroll_area)

        main_layout = QVBoxLayout(central_widget)  # Vertical layout for the main content

        # Add the logout button to the top right corner
        top_layout = QHBoxLayout()
        top_spacer = QWidget()
        top_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        top_layout.addWidget(top_spacer)
        top_layout.addWidget(self.logout_btn)
        main_layout.addLayout(top_layout)

        # Panels Layout
        panels_layout = QHBoxLayout()  # Horizontal layout for left panel

        # Left Panel: Past Medical Record
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        past_medical_record_label = QLabel("Past Medical Record")
        past_medical_record_label.setAlignment(Qt.AlignCenter)
        past_medical_record_label.setFont(QFont("Helvetica", 14, QFont.Bold))
        left_layout.addWidget(past_medical_record_label)

        self.past_visits_table = QTableWidget()
        self.past_visits_table.setColumnCount(7)
        self.past_visits_table.setHorizontalHeaderLabels(["Record ID", "Patient ID", "Doctor ID", "Date", "Time", "Description", "Prescription"])
        left_layout.addWidget(self.past_visits_table)

        sort_oldest_button = QPushButton("Sort by Oldest")
        sort_oldest_button.clicked.connect(lambda: self.load_past_visits(order="oldest"))
        sort_oldest_button.setFont(QFont("Helvetica", 14))
        sort_oldest_button.setMinimumHeight(30)  # Increase vertical size
        left_layout.addWidget(sort_oldest_button)

        sort_latest_button = QPushButton("Sort by Latest")
        sort_latest_button.clicked.connect(lambda: self.load_past_visits(order="latest"))
        sort_latest_button.setFont(QFont("Helvetica", 14))
        sort_latest_button.setMinimumHeight(30)  # Increase vertical size
        left_layout.addWidget(sort_latest_button)

        panels_layout.addWidget(left_panel)
        main_layout.addLayout(panels_layout)

        # Bottom Buttons
        bottom_button_layout = QHBoxLayout()
        map_btn = QPushButton("Map")
        map_btn.setStyleSheet("background-color: #3e8e41; color: white;")  # Green button
        map_btn.setFont(QFont("Helvetica", 14))
        map_btn.setMinimumHeight(30)  # Increase vertical size
        map_btn.clicked.connect(self.show_map_window)

        profile_btn = QPushButton("Profile")
        profile_btn.setStyleSheet("background-color: #3e8e41; color: white;")  # Green button
        profile_btn.setFont(QFont("Helvetica", 14))
        profile_btn.setMinimumHeight(30)  # Increase vertical size
        profile_btn.clicked.connect(self.show_profile_window)

        appointment_btn = QPushButton("Appointment")
        appointment_btn.setStyleSheet("background-color: #3e8e41; color: white;")  # Green button
        appointment_btn.setFont(QFont("Helvetica", 14))
        appointment_btn.setMinimumHeight(30)  # Increase vertical size
        appointment_btn.clicked.connect(self.show_appointment_window)

        bottom_button_layout.addWidget(map_btn)
        bottom_button_layout.addWidget(profile_btn)
        bottom_button_layout.addWidget(appointment_btn)

        main_layout.addLayout(bottom_button_layout)

        # Load past visits
        self.load_past_visits()

    def load_past_visits(self, order="oldest"):
        visits = fetch_records(self.patient_id)  # Fetch records from database for the specific patient
        if order == "oldest":
            visits.sort(key=lambda x: x["Date"])
        else:
            visits.sort(key=lambda x: x["Date"], reverse=True)
        
        self.past_visits_table.setRowCount(len(visits))
        for row, visit in enumerate(visits):
            self.past_visits_table.setItem(row, 0, QTableWidgetItem(str(visit["Record ID"])))
            self.past_visits_table.setItem(row, 1, QTableWidgetItem(str(visit["Patient ID"])))
            self.past_visits_table.setItem(row, 2, QTableWidgetItem(str(visit["Doctor ID"])))
            self.past_visits_table.setItem(row, 3, QTableWidgetItem(str(visit["Date"])))
            self.past_visits_table.setItem(row, 4, QTableWidgetItem(str(visit["Time"])))
            self.past_visits_table.setItem(row, 5, QTableWidgetItem(str(visit["Description"])))
            self.past_visits_table.setItem(row, 6, QTableWidgetItem(str(visit["Prescription"])))

    def show_profile_window(self):
        from Profile_v1 import ProfileWindow
        self.profile_window = ProfileWindow(self.patient_id)
        self.profile_window.show()

    def show_map_window(self):
        from Map_v2 import MapHomePage
        self.map_window = MapHomePage(self.patient_id)
        self.map_window.show()

    def show_appointment_window(self):
        from Appoint_v1 import AppointmentSystem
        self.appointment_window = AppointmentSystem(self.patient_id)
        self.appointment_window.show()

    def logout(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        patient_id = sys.argv[1]
        health_record_window = PersonalHealthRecordWindow(patient_id)
    else:
        QMessageBox.critical(None, "Error", "No patient ID provided")
        sys.exit(1)
    health_record_window.show()
    sys.exit(app.exec_())
