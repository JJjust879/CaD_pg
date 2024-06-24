import sys
import os
import folium
import sqlite3
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QTextEdit, QCalendarWidget, QFileDialog, QSplitter, QSizePolicy, QStackedWidget, QToolTip,
                             QButtonGroup, QFormLayout, QComboBox, QTimeEdit)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import QTimer, Qt, QDate, QTime
from Map_v2 import MapHomePage
from health_rec import PersonalHealthRecordWindow
from Profile_v1 import ProfileWindow

class AppointmentSystem(QMainWindow):
    def __init__(self, patient_id):
        super().__init__()
        self.patient_id = patient_id
        self.setWindowTitle("Call a Doctor - Appointment System")
        self.resize(1920, 1080)
        self.center_window()
        self.initUI()

        self.current_secondary_window = None

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def initUI(self):
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_widget = QWidget()
        self.stacked_widget.addWidget(self.main_widget)

        layout = QVBoxLayout()
        self.main_widget.setLayout(layout)

        # Top Layout for Logout Button
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)

        # Clinic Selection Label
        clinic_label = QLabel("Please Select Clinic")
        clinic_label.setFont(QFont("Helvetica", 12, QFont.Bold))
        top_layout.addWidget(clinic_label)

        # Add Clinic Selection Dropdown
        self.clinic_dropdown = QComboBox()
        self.clinic_dropdown.setFont(QFont("Helvetica", 10))
        clinics = ["Clinic B.S Tan", "Clinic Lee", "Clinic Singapore", "Clinic Tropica", "Clinic Koe", "Clinic Medivirion", "Clinic Kesihatan Bayan Lepas", "Clinic Kare", "Clinic Health Plus", "Clinic Bayan Baru"]
        self.clinic_dropdown.addItems(clinics)
        self.clinic_dropdown.setMinimumWidth(200)  # Set a minimum width to make the dropdown bigger
        top_layout.addWidget(self.clinic_dropdown)

        top_layout.addStretch()  # Add stretch to push the button to the right
        logout_btn = QPushButton("Logout")
        logout_btn.setFont(QFont("Helvetica", 10))
        logout_btn.clicked.connect(self.logout)
        top_layout.addWidget(logout_btn)

        splitter = QSplitter(Qt.Horizontal)

        self.left_panel = self.create_left_panel()
        splitter.addWidget(self.left_panel)

        self.right_panel = self.create_right_panel()
        splitter.addWidget(self.right_panel)

        handle = splitter.handle(1)
        handle.setStyleSheet("QSplitterHandle { background-color: lightgray }")
        handle.setDisabled(True)

        layout.addWidget(splitter)
        self.create_tab_navigation(layout)
        self.create_success_screen()

    def create_left_panel(self):
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        calendar_label = QLabel("Select Appointment Date:")
        calendar_label.setFont(QFont("Helvetica", 10))
        left_layout.addWidget(calendar_label)

        self.calendar = QCalendarWidget()
        left_layout.addWidget(self.calendar)

        time_label = QLabel("Select Appointment Time:")
        time_label.setFont(QFont("Helvetica", 10))
        left_layout.addWidget(time_label)

        self.time_edit = QTimeEdit()
        self.time_edit.setFont(QFont("Helvetica", 10))
        self.time_edit.setTime(QTime.currentTime())
        left_layout.addWidget(self.time_edit)

        doctor_label = QLabel("Available Doctors:")
        doctor_label.setFont(QFont("Helvetica", 10))
        left_layout.addWidget(doctor_label)

        self.doctor_list = QTextEdit()
        self.doctor_list.setReadOnly(True)
        left_layout.addWidget(self.doctor_list)

        return left_panel

    def create_right_panel(self):
        right_panel = QWidget()
        right_layout = QFormLayout()
        right_panel.setLayout(right_layout)

        self.doctor_info_label = QLabel("Doctor's Information:")
        self.doctor_info_label.setFont(QFont("Helvetica", 10))
        right_layout.addRow(self.doctor_info_label)

        self.doctor_info_box = QTextEdit()
        self.doctor_info_box.setReadOnly(True)
        right_layout.addRow(self.doctor_info_box)

        self.send_btn = QPushButton("Send Appointment")
        self.send_btn.setFont(QFont("Helvetica", 12, QFont.Bold))
        right_layout.addRow(self.send_btn)

        self.error_label = QLabel("")
        self.error_label.setFont(QFont("Helvetica", 10))
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setVisible(False)
        right_layout.addRow(self.error_label)

        self.send_btn.clicked.connect(self.send_appointment)

        return right_panel

    def create_tab_navigation(self, layout):
        tab_layout = QHBoxLayout()
        layout.addLayout(tab_layout)

        buttons = ["Profile", "Map", "Health Record"]
        for btn_text in buttons:
            btn = QPushButton(btn_text)
            btn.setFont(QFont("Helvetica", 10))
            btn.setStyleSheet("background-color: #3e8e41; color: white; border: none;")
            tab_layout.addWidget(btn)
            if btn_text == "Profile":
                btn.clicked.connect(self.show_profile_window)
            elif btn_text == "Map":
                btn.clicked.connect(self.show_map_window)
            elif btn_text == "Health Record":
                btn.clicked.connect(self.show_health_record_window)

    def create_success_screen(self):
        self.success_widget = QWidget()
        success_layout = QVBoxLayout()
        self.success_widget.setLayout(success_layout)

        self.success_label = QLabel("Appointment Request Sent")
        self.success_label.setStyleSheet("background-color: lightgreen; color: black; font-size: 50px;")
        self.success_label.setAlignment(Qt.AlignCenter)
        success_layout.addWidget(self.success_label)

        self.stacked_widget.addWidget(self.success_widget)

    def send_appointment(self):
        selected_date = self.calendar.selectedDate()
        current_date = QDate.currentDate()
        selected_time = self.time_edit.time()
        current_time = QTime.currentTime()

        if selected_date < current_date or (selected_date == current_date and selected_time < current_time):
            self.error_label.setText("Invalid Date or Time")
            self.error_label.setVisible(True)
        else:
            self.error_label.setVisible(False)
            self.send_btn.setDisabled(True)

            conn = sqlite3.connect('CallADoctor.db')
            cursor = conn.cursor()

            try:
                # Fetch the patient's name using patient_id
                cursor.execute('''
                    SELECT Patient_Name FROM Patient 
                    WHERE Patient_ID = ?
                ''', (self.patient_id,))
                patient_name = cursor.fetchone()

                if patient_name:
                    patient_name = patient_name[0]

                    # Insert the appointment with the fetched patient name
                    cursor.execute('''
                        INSERT INTO Appointments (Patient_ID, Appointment_Date, Appointment_Time, Clinic_ID, Patient_Name)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (self.patient_id, selected_date.toString(Qt.DateFormat.ISODate), selected_time.toString(), self.clinic_dropdown.currentText(), patient_name))
                    conn.commit()
                    QTimer.singleShot(3000, self.show_success_screen)
                else:
                    self.error_label.setText("Patient not found")
                    self.error_label.setVisible(True)

            except sqlite3.Error as e:
                self.error_label.setText(f"Database error: {e}")
                self.error_label.setVisible(True)

            finally:
                conn.close()


    def show_success_screen(self):
        self.stacked_widget.setCurrentIndex(1)
        self.success_label.setFont(QFont("Arial", 40, QFont.Bold))
        QTimer.singleShot(3000, self.show_main_screen)

    def show_main_screen(self):
        self.stacked_widget.setCurrentIndex(0)
        self.send_btn.setDisabled(False)

    def show_profile_window(self):
        self.profile_window = ProfileWindow()
        self.profile_window.show()

    def show_map_window(self):
        if not self.current_secondary_window or not isinstance(self.current_secondary_window, MapHomePage):
            self.current_secondary_window = MapHomePage()
        if self.current_secondary_window:
            self.current_secondary_window.destroyed.connect(self.secondary_window_closed)
            self.current_secondary_window.show()

    def show_health_record_window(self):
        if not self.current_secondary_window or not isinstance(self.current_secondary_window, PersonalHealthRecordWindow):
            self.current_secondary_window = PersonalHealthRecordWindow(self.patient_id)
        if self.current_secondary_window:
            self.current_secondary_window.destroyed.connect(self.secondary_window_closed)
            self.current_secondary_window.show()

    def secondary_window_closed(self):
        self.current_secondary_window = None

    def logout(self):
        QApplication.quit()

if __name__ == "__main__":
    print("Received arguments:", sys.argv)
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        patient_id = sys.argv[1]
        window = AppointmentSystem(patient_id)
    else:
        window = AppointmentSystem()  # for testing without patient_id
    window.show()
    sys.exit(app.exec_())
