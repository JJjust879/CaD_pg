import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from PyQt5.QtGui import QPalette, QColor
from records_screen import RecordsScreen
from doctors_screen import DoctorsScreen
from appointments_screen import AppointmentsScreen

class ClinicDashboard(QWidget):
    def __init__(self, clinic_id):  # Accept clinic_id as a parameter
        super().__init__()
        self.clinic_id = clinic_id  # Store the clinic_id
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clinic Dashboard')
        self.setGeometry(100, 100, 800, 600)

        # Set light blue theme
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(200, 220, 255))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Button, QColor(200, 220, 255))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Link, QColor(0, 0, 255))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 120, 215))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

        # Create tabs
        tab_widget = QTabWidget()
        tab_widget.addTab(RecordsScreen(self.clinic_id), "Records")  # Pass clinic_id to screens if needed
        tab_widget.addTab(DoctorsScreen(self.clinic_id), "Doctors")
        tab_widget.addTab(AppointmentsScreen(self.clinic_id), "Appointments")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clinic_id = int(sys.argv[1])  # Get the clinic_id from command-line arguments
    dashboard = ClinicDashboard(clinic_id)
    dashboard.show()
    sys.exit(app.exec_())
