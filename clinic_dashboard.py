import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QPushButton
from PyQt5.QtGui import QPalette, QColor
from records_screen import RecordsScreen
from doctors_screen import DoctorsScreen
from appointments_screen import AppointmentsScreen
import subprocess

class ClinicDashboard(QWidget):
    def __init__(self, clinic_id):
        super().__init__()
        self.clinic_id = clinic_id
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clinic Dashboard')
        self.setGeometry(100, 100, 800, 600)

        # Set light blue theme
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(200, 220, 255))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
        self.setPalette(palette)

        # Create tabs
        tab_widget = QTabWidget()
        tab_widget.addTab(RecordsScreen(self.clinic_id), "Records")
        tab_widget.addTab(DoctorsScreen(self.clinic_id), "Doctors")
        tab_widget.addTab(AppointmentsScreen(self.clinic_id), "Appointments")

        # Add logout button
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        main_layout.addWidget(self.logout_button)
        self.setLayout(main_layout)
        self.current_window = ClinicDashboard

    def logout(self):
        subprocess.Popen([sys.executable, "startupwindow.py"])
        self.current_window.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        clinic_id = int(sys.argv[1])
        dashboard = ClinicDashboard(clinic_id)
        dashboard.show()
        sys.exit(app.exec_())
    else:
        print("Please provide a clinic_id as a command-line argument")