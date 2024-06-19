from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QDateEdit, QTimeEdit, QTextEdit, QDialog, QFormLayout
from PyQt5.QtCore import QDate, QTime

class RecordDialog(QDialog):
    def __init__(self, parent=None, record_data=None):
        super().__init__(parent)
        self.setWindowTitle("Record Information")
        self.layout = QFormLayout(self)

        if record_data is None:
            record_data = {}

        self.date_input = QDateEdit(QDate.fromString(record_data.get("date", ""), "yyyy-MM-dd"))
        self.doctor_id_input = QLineEdit(record_data.get("doctor_id", ""))
        self.time_input = QTimeEdit(QTime.fromString(record_data.get("time", ""), "HH:mm"))
        self.description_input = QTextEdit(record_data.get("description", ""))
        self.prescription_input = QTextEdit(record_data.get("prescription", ""))

        self.layout.addRow("Date:", self.date_input)
        self.layout.addRow("Doctor ID:", self.doctor_id_input)
        self.layout.addRow("Time:", self.time_input)
        self.layout.addRow("Description:", self.description_input)
        self.layout.addRow("Prescription:", self.prescription_input)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.accept)
        self.layout.addRow(self.submit_button)

    def get_record_data(self):
        return {
            "date": self.date_input.date().toString("yyyy-MM-dd"),
            "doctor_id": self.doctor_id_input.text(),
            "time": self.time_input.time().toString("HH:mm"),
            "description": self.description_input.toPlainText(),
            "prescription": self.prescription_input.toPlainText()
        }

class RecordsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create table to display records
        self.records_table = QTableWidget()
        self.records_table.setColumnCount(6)
        self.records_table.setHorizontalHeaderLabels(['Record ID', 'Date', 'Doctor ID', 'Time', 'Description', 'Prescription'])
        self.records_table.setRowCount(0)
        self.records_table.cellClicked.connect(self.highlight_row)

        # Create buttons for adding and editing records
        self.add_button = QPushButton('Add Record')
        self.add_button.clicked.connect(self.add_record)
        self.edit_button = QPushButton('Edit Record')
        self.edit_button.clicked.connect(self.edit_record)
        self.edit_button.setEnabled(False)

        # Create layout for records screen
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addStretch()

        records_layout = QVBoxLayout()
        records_layout.addWidget(self.records_table)
        records_layout.addLayout(button_layout)

        self.setLayout(records_layout)

    def highlight_row(self, row, column):
        self.records_table.selectRow(row)
        self.edit_button.setEnabled(True)

    def add_record(self):
        dialog = RecordDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            record_data = dialog.get_record_data()

            # Generate a unique record ID 
            record_id = str(self.records_table.rowCount() + 1)

            # Add the new record to the table
            row_count = self.records_table.rowCount()
            self.records_table.insertRow(row_count)
            self.records_table.setItem(row_count, 0, QTableWidgetItem(record_id))
            self.records_table.setItem(row_count, 1, QTableWidgetItem(record_data["date"]))
            self.records_table.setItem(row_count, 2, QTableWidgetItem(record_data["doctor_id"]))
            self.records_table.setItem(row_count, 3, QTableWidgetItem(record_data["time"]))
            self.records_table.setItem(row_count, 4, QTableWidgetItem(record_data["description"]))
            self.records_table.setItem(row_count, 5, QTableWidgetItem(record_data["prescription"]))

    def edit_record(self):
        selected_row = self.records_table.currentRow()
        if selected_row >= 0:
            record_data = {
                "date": self.records_table.item(selected_row, 1).text(),
                "doctor_id": self.records_table.item(selected_row, 2).text(),
                "time": self.records_table.item(selected_row, 3).text(),
                "description": self.records_table.item(selected_row, 4).text(),
                "prescription": self.records_table.item(selected_row, 5).text()
            }
            dialog = RecordDialog(self, record_data)
            if dialog.exec_() == QDialog.Accepted:
                updated_data = dialog.get_record_data()
                self.records_table.setItem(selected_row, 1, QTableWidgetItem(updated_data["date"]))
                self.records_table.setItem(selected_row, 2, QTableWidgetItem(updated_data["doctor_id"]))
                self.records_table.setItem(selected_row, 3, QTableWidgetItem(updated_data["time"]))
                self.records_table.setItem(selected_row, 4, QTableWidgetItem(updated_data["description"]))
                self.records_table.setItem(selected_row, 5, QTableWidgetItem(updated_data["prescription"]))
