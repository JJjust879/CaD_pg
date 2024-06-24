import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QLineEdit, QFileDialog, QTextEdit, QSizePolicy, 
    QComboBox, QDateEdit, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QDate

class ProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personal Profile")
        self.setGeometry(0, 0, 1920, 1080)  # Set initial window size to 1920x1080
        self.setStyleSheet("background-color: #f0f0f0; font-family: Helvetica; font-size: 11pt;")
        self.initUI()

    def initUI(self):
        scroll_area = QScrollArea()
        central_widget = QWidget()
        scroll_area.setWidget(central_widget)
        scroll_area.setWidgetResizable(True)

        self.setCentralWidget(scroll_area)

        main_layout = QVBoxLayout(central_widget)

        # Logout Button at the top-right
        top_layout = QHBoxLayout()
        top_layout.addStretch()
        self.logout_btn = QPushButton("Logout", clicked=self.logout)
        self.logout_btn.setFont(QFont("Helvetica", 14))
        self.logout_btn.setFixedHeight(30)
        top_layout.addWidget(self.logout_btn)
        main_layout.addLayout(top_layout)

        # Profile Picture Section
        pic_layout = QHBoxLayout()
        self.profile_pic_label = QLabel("Profile Picture")
        self.profile_pic_label.setAlignment(Qt.AlignCenter)
        self.profile_pic_label.setFont(QFont("Helvetica", 20, QFont.Bold))
        self.profile_pic_label.setFixedSize(400, 400)
        self.profile_pic_label.setStyleSheet("border: 2px solid black; background-color: #ffffff;")
        pic_layout.addWidget(self.profile_pic_label)

        self.upload_btn = QPushButton("Upload Image", clicked=self.upload_image)
        self.upload_btn.setFont(QFont("Helvetica", 14))
        self.upload_btn.setFixedHeight(30)
        pic_layout.addWidget(self.upload_btn)
        main_layout.addLayout(pic_layout)

        # User Information Fields
        info_layout = QVBoxLayout()
        fields = [
            ('Name', QLineEdit),
            ('Password', QLineEdit),
            ('Email', QLineEdit),
            ('Age', QLineEdit),
            ('Sex/Gender', QComboBox),
            ('Home Address', QLineEdit),
            ('Phone Number', QLineEdit),
        ]

        self.fields = {}
        for label_text, widget_type in fields:
            label = QLabel(label_text)
            label.setFont(QFont("Helvetica", 14, QFont.Bold))
            entry = widget_type()
            entry.setStyleSheet("border: 1px solid black; background-color: #ffffff;")
            if isinstance(entry, QLineEdit):
                if label_text == 'Password':
                    entry.setEchoMode(QLineEdit.Password)
                entry.setFixedHeight(50)
                entry.setReadOnly(True)  # Initially set QLineEdit to read-only
            elif isinstance(entry, QComboBox):
                entry.setFixedHeight(50)
                entry.setEnabled(False)  # Initially disable QComboBox
                if label_text == 'Sex/Gender':
                    entry.addItems(['Male', 'Female', 'Other'])
                elif label_text == 'Blood Type':
                    entry.addItems(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
            elif isinstance(entry, QTextEdit):
                entry.setFixedHeight(50)
                entry.setReadOnly(True)  # Initially set QTextEdit to read-only
            info_layout.addWidget(label)
            info_layout.addWidget(entry)
            self.fields[label_text] = entry

        main_layout.addLayout(info_layout)

        # Edit and Save Buttons
        edit_save_layout = QHBoxLayout()
        self.edit_btn = QPushButton("Edit", clicked=self.enable_editing)
        self.edit_btn.setFont(QFont("Helvetica", 14))
        self.edit_btn.setFixedHeight(40)
        edit_save_layout.addWidget(self.edit_btn)

        self.save_btn = QPushButton("Save", clicked=self.save_profile)
        self.save_btn.setFont(QFont("Helvetica", 14))
        self.save_btn.setFixedHeight(40)
        self.save_btn.setEnabled(False)  # Initially disable Save button
        edit_save_layout.addWidget(self.save_btn)

        main_layout.addLayout(edit_save_layout)

        # Bottom Tab Buttons
        bottom_tab_layout = QHBoxLayout()
        map_btn = QPushButton("Map")
        appointment_btn = QPushButton("Appointment")
        health_record_btn = QPushButton("Health Record")

        button_style = """
            background-color: #3e8e41; 
            color: white; 
            border: none; 
            font-size: 14pt; 
            min-height: 40px;
        """
        
        map_btn.setStyleSheet(button_style)
        appointment_btn.setStyleSheet(button_style)
        health_record_btn.setStyleSheet(button_style)

        map_btn.clicked.connect(self.show_map_window)
        appointment_btn.clicked.connect(self.show_appointment_window)
        health_record_btn.clicked.connect(self.show_health_record_window)

        bottom_tab_layout.addWidget(map_btn)
        bottom_tab_layout.addWidget(appointment_btn)
        bottom_tab_layout.addWidget(health_record_btn)

        main_layout.addLayout(bottom_tab_layout)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.profile_pic_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
        else:
            QMessageBox.warning(self, "Error", "Failed to upload image.")

    def enable_editing(self):
        for entry in self.fields.values():
            if isinstance(entry, (QLineEdit, QTextEdit)):
                entry.setReadOnly(False)
            elif isinstance(entry, (QComboBox, QDateEdit)):
                entry.setEnabled(True)
        self.upload_btn.setEnabled(True)
        self.edit_btn.setEnabled(False)
        self.save_btn.setEnabled(True)

    def save_profile(self):
        profile_data = {}
        for label, entry in self.fields.items():
            if isinstance(entry, QLineEdit) or isinstance(entry, QTextEdit):
                profile_data[label] = entry.text() if isinstance(entry, QLineEdit) else entry.toPlainText()
            elif isinstance(entry, QComboBox):
                profile_data[label] = entry.currentText()
            elif isinstance(entry, QDateEdit):
                profile_data[label] = entry.date().toString(Qt.ISODate)
        
        QMessageBox.information(self, "Profile Saved", "Profile information has been saved successfully!")

        for entry in self.fields.values():
            if isinstance(entry, (QLineEdit, QTextEdit)):
                entry.setReadOnly(True)
            elif isinstance(entry, (QComboBox, QDateEdit)):
                entry.setEnabled(False)

        self.upload_btn.setEnabled(False)
        self.edit_btn.setEnabled(True)
        self.save_btn.setEnabled(False)

    def show_map_window(self):
        from Map_v2 import MapHomePage
        self.map_window = MapHomePage()
        self.map_window.show()

    def show_appointment_window(self):
        from Appoint_v1 import AppointmentSystem
        self.appointment_window = AppointmentSystem()
        self.appointment_window.show()

    def show_health_record_window(self):
        from health_rec import PersonalHealthRecordWindow
        self.health_record_window = PersonalHealthRecordWindow()
        self.health_record_window.show()

    def logout(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    profile_window = ProfileWindow()
    profile_window.show()
    sys.exit(app.exec_())
