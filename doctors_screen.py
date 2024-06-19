from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QComboBox, QDialog, QFormLayout, QFileDialog
from PyQt5.QtGui import QPixmap

class DoctorDialog(QDialog):
    def __init__(self, parent=None, doctor_data=None):
        super().__init__(parent)
        self.setWindowTitle("Doctor Information")
        self.layout = QFormLayout(self)

        if doctor_data is None:
            doctor_data = {}
            
        self.name_input = QLineEdit(doctor_data.get("name", ""))
        self.spec_input = QLineEdit(doctor_data.get("specialization", ""))
        self.age_input = QLineEdit(doctor_data.get("age", ""))
        self.gender_input = QComboBox()
        self.gender_input.addItems(['Male', 'Female', 'Other'])
        self.gender_input.setCurrentText(doctor_data.get("gender", ""))
        self.email_input = QLineEdit(doctor_data.get("email", ""))
        self.phone_input = QLineEdit(doctor_data.get("phone", ""))
        self.image_label = QLabel()
        self.image_path = doctor_data.get("image", "")
        if self.image_path:
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(pixmap)
        self.image_button = QPushButton("Select Image")
        self.image_button.clicked.connect(self.select_image)

        self.layout.addRow("Name:", self.name_input)
        self.layout.addRow("Specialization:", self.spec_input)
        self.layout.addRow("Age:", self.age_input)
        self.layout.addRow("Gender:", self.gender_input)
        self.layout.addRow("Email:", self.email_input)
        self.layout.addRow("Phone:", self.phone_input)
        self.layout.addRow(self.image_label)
        self.layout.addRow(self.image_button)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.accept)
        self.layout.addRow(self.submit_button)

    def select_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if image_path:
            self.image_path = image_path
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)

    def get_doctor_data(self):
        return {
            "name": self.name_input.text(),
            "specialization": self.spec_input.text(),
            "age": self.age_input.text(),
            "gender": self.gender_input.currentText(),
            "email": self.email_input.text(),
            "phone": self.phone_input.text(),
            "image": self.image_path
        }

class DoctorsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create table to display doctors
        self.doctors_table = QTableWidget()
        self.doctors_table.setColumnCount(8)
        self.doctors_table.setHorizontalHeaderLabels(['Doctor ID', 'Name', 'Specialization', 'Age', 'Gender', 'Email', 'Phone', 'Image'])
        self.doctors_table.setRowCount(0)
        self.doctors_table.cellClicked.connect(self.highlight_row)

        # Create buttons for adding and editing doctors
        self.add_button = QPushButton('Add Doctor')
        self.add_button.clicked.connect(self.add_doctor)
        self.edit_button = QPushButton('Edit Doctor')
        self.edit_button.clicked.connect(self.edit_doctor)
        self.edit_button.setEnabled(False)

        # Create layout for doctors screen
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addStretch()

        doctors_layout = QVBoxLayout()
        doctors_layout.addWidget(self.doctors_table)
        doctors_layout.addLayout(button_layout)

        self.setLayout(doctors_layout)

    def highlight_row(self, row, column):
        self.doctors_table.selectRow(row)
        self.edit_button.setEnabled(True)

    def add_doctor(self):
        dialog = DoctorDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            doctor_data = dialog.get_doctor_data()

            # Generate a unique doctor ID 
            doctor_id = str(self.doctors_table.rowCount() + 1)

            # Add the new doctor to the table
            row_count = self.doctors_table.rowCount()
            self.doctors_table.insertRow(row_count)
            self.doctors_table.setItem(row_count, 0, QTableWidgetItem(doctor_id))
            self.doctors_table.setItem(row_count, 1, QTableWidgetItem(doctor_data["name"]))
            self.doctors_table.setItem(row_count, 2, QTableWidgetItem(doctor_data["specialization"]))
            self.doctors_table.setItem(row_count, 3, QTableWidgetItem(doctor_data["age"]))
            self.doctors_table.setItem(row_count, 4, QTableWidgetItem(doctor_data["gender"]))
            self.doctors_table.setItem(row_count, 5, QTableWidgetItem(doctor_data["email"]))
            self.doctors_table.setItem(row_count, 6, QTableWidgetItem(doctor_data["phone"]))
            self.doctors_table.setItem(row_count, 7, QTableWidgetItem(doctor_data["image"]))

    def edit_doctor(self):
        selected_row = self.doctors_table.currentRow()
        if selected_row >= 0:
            doctor_data = {
                "name": self.doctors_table.item(selected_row, 1).text(),
                "specialization": self.doctors_table.item(selected_row, 2).text(),
                "age": self.doctors_table.item(selected_row, 3).text(),
                "gender": self.doctors_table.item(selected_row, 4).text(),
                "email": self.doctors_table.item(selected_row, 5).text(),
                "phone": self.doctors_table.item(selected_row, 6).text(),
                "image": self.doctors_table.item(selected_row, 7).text()
            }
            dialog = DoctorDialog(self, doctor_data)
            if dialog.exec_() == QDialog.Accepted:
                updated_data = dialog.get_doctor_data()
                self.doctors_table.setItem(selected_row, 1, QTableWidgetItem(updated_data["name"]))
                self.doctors_table.setItem(selected_row, 2, QTableWidgetItem(updated_data["specialization"]))
                self.doctors_table.setItem(selected_row, 3, QTableWidgetItem(updated_data["age"]))
                self.doctors_table.setItem(selected_row, 4, QTableWidgetItem(updated_data["gender"]))
                self.doctors_table.setItem(selected_row, 5, QTableWidgetItem(updated_data["email"]))
                self.doctors_table.setItem(selected_row, 6, QTableWidgetItem(updated_data["phone"]))
                self.doctors_table.setItem(selected_row, 7, QTableWidgetItem(updated_data["image"]))
