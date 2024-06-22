import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from PyQt5.QtGui import QPalette, QColor
from records_screen import RecordsScreen
from doctors_screen import DoctorsScreen
from appointments_screen import AppointmentsScreen

class ClinicDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clinic Dashboard')
        self.setGeometry(100, 100, 800, 600)

        # Set light blue theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(200, 220, 255))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.AlternateBase, QColor(220, 220, 220))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(200, 220, 255))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
        palette.setColor(QPalette.Link, QColor(0, 0, 255))
        palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

        # Create tabs
        tab_widget = QTabWidget()
        tab_widget.addTab(RecordsScreen(), "Records")
        tab_widget.addTab(DoctorsScreen(), "Doctors")
        tab_widget.addTab(AppointmentsScreen(), "Appointments")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = ClinicDashboard()
    dashboard.show()
    sys.exit(app.exec_())