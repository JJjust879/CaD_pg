import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QTextEdit, QCalendarWidget, QFileDialog, QSplitter, 
    QSizePolicy, QStackedWidget, QToolTip, QButtonGroup
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import QTimer, Qt, QProcess
from Map_v2 import MapHomePage  # Ensure MapHomePage is correctly imported

class AppointmentSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Call a Doctor - Appointment System")
        self.resize(1920, 1080)
        self.center_window()
        self.initUI()

    def center_window(self):
        screen_geometry = QApplication.desktop().screenGeometry()
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
        handle.setStyleSheet("background-color: #CCCCCC;")
        handle.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        handle.setToolTip("Adjust Panel")
        QToolTip.setFont(QFont('Helvetica', 10))
        handle.setCursor(QCursor(Qt.SplitHCursor))

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

        doctor_label = QLabel("Available Doctors:")
        doctor_label.setFont(QFont("Helvetica", 10))
        left_layout.addWidget(doctor_label)

        self.doctor_list = QTextEdit()
        self.doctor_list.setReadOnly(True)
        left_layout.addWidget(self.doctor_list)

        return left_panel

    def create_right_panel(self):
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)

        self.doctor_info_label = QLabel("Doctor's Information:")
        self.doctor_info_label.setFont(QFont("Helvetica", 10))
        right_layout.addWidget(self.doctor_info_label)

        self.purpose_label = QLabel("Purpose of Visit:")
        self.purpose_label.setFont(QFont("Helvetica", 10))
        right_layout.addWidget(self.purpose_label)

        self.medical_checkup_btn = QPushButton("Medical Checkup")
        self.collect_report_btn = QPushButton("Collect Health Report")
        self.custom_inquiry_btn = QPushButton("Custom Inquiry")
        self.medical_checkup_btn.setFont(QFont("Helvetica", 10))
        self.collect_report_btn.setFont(QFont("Helvetica", 10))
        self.custom_inquiry_btn.setFont(QFont("Helvetica", 10))
        
        self.inquiry_button_group = QButtonGroup()
        self.inquiry_button_group.addButton(self.medical_checkup_btn)
        self.inquiry_button_group.addButton(self.collect_report_btn)
        self.inquiry_button_group.addButton(self.custom_inquiry_btn)
        self.custom_inquiry_btn.setCheckable(True)

        right_layout.addWidget(self.medical_checkup_btn)
        right_layout.addWidget(self.collect_report_btn)
        right_layout.addWidget(self.custom_inquiry_btn)

        self.custom_inquiry_box = QTextEdit()
        self.custom_inquiry_box.setPlaceholderText("Type your custom inquiry (max 150 words)")
        self.custom_inquiry_box.hide()
        right_layout.addWidget(self.custom_inquiry_box)

        self.upload_btn = QPushButton("Upload Present Medical Report")
        self.upload_btn.setFont(QFont("Helvetica", 10))
        right_layout.addWidget(self.upload_btn)

        self.send_btn = QPushButton("Send Appointment")
        self.send_btn.setFont(QFont("Helvetica", 12, QFont.Bold))
        right_layout.addWidget(self.send_btn)

        self.custom_inquiry_btn.clicked.connect(self.toggle_custom_inquiry_box)
        self.upload_btn.clicked.connect(self.upload_medical_report)
        self.send_btn.clicked.connect(self.send_appointment)

        return right_panel

    def create_tab_navigation(self, layout):
        tab_layout = QHBoxLayout()
        layout.addLayout(tab_layout)

        buttons = ["Profile", "Map", "Health Record"]
        for btn_text in buttons:
            btn = QPushButton(btn_text)
            btn.setFont(QFont("Helvetica", 10))
            tab_layout.addWidget(btn)
            if btn_text == "Profile":
                btn.clicked.connect(self.show_profile_window)
            elif btn_text == "Map":
                btn.clicked.connect(self.show_map_window)

    def create_success_screen(self):
        self.success_widget = QWidget()
        success_layout = QVBoxLayout()
        self.success_widget.setLayout(success_layout)

        self.success_label = QLabel("Appointment Successful")
        self.success_label.setStyleSheet("background-color: lightgreen; color: black; font-size: 20px;")
        self.success_label.setAlignment(Qt.AlignCenter)
        success_layout.addWidget(self.success_label)

        self.stacked_widget.addWidget(self.success_widget)

    def toggle_custom_inquiry_box(self):
        self.custom_inquiry_box.setVisible(self.custom_inquiry_btn.isChecked())

    def upload_medical_report(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Upload Medical Report", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print(f"Uploaded file: {file_name}")
        else:
            print("File upload canceled or failed")

    def send_appointment(self):
        self.send_btn.setDisabled(True)
        QTimer.singleShot(3000, self.show_success_screen)

    def show_success_screen(self):
        self.stacked_widget.setCurrentIndex(1)
        self.success_label.setFont(QFont("Arial", 40, QFont.Bold))
        self.custom_inquiry_box.clear()
        QTimer.singleShot(3000, self.show_main_screen)

    def show_main_screen(self):
        self.stacked_widget.setCurrentIndex(0)
        self.send_btn.setDisabled(False)

    def show_profile_window(self):
        self.process = QProcess(self)
        self.process.start("python", ["Profile_v1.py"])

    def show_map_window(self):
        self.map_homepage = MapHomePage()
        self.map_homepage.show()

    def logout(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppointmentSystem()
    window.show()
    sys.exit(app.exec_())
