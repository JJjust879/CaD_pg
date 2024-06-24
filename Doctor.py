import os
import sys
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QDateEdit, QTimeEdit
from PyQt6.QtCore import QDate, QTime, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QFont
import subprocess

class DoctorProfileDialog(QDialog):
    def __init__(self, doctor_id, parent=None):
        super().__init__(parent)
        self.doctor_id = doctor_id
        self.setWindowTitle("Doctor Profile")
        self.setMinimumSize(400, 350)
        self.initialize_database()

        self.main_layout = QVBoxLayout()

        # Profile picture
        self.picture_layout = QVBoxLayout()
        self.picture_label = QLabel()
        self.picture_layout.addWidget(self.picture_label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.change_picture_btn = QPushButton("Change Picture")
        self.change_picture_btn.clicked.connect(self.change_profile_picture)
        self.picture_layout.addWidget(self.change_picture_btn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addLayout(self.picture_layout)

        # Set default profile picture
        self.set_profile_picture("profile_icon.jpg")

        # Doctor information
        self.info_layout = QVBoxLayout()

        self.name_label = QLabel()
        self.name_label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Weight.Bold))
        self.info_layout.addWidget(self.name_label)

        self.ID_label = QLabel()
        self.info_layout.addWidget(self.ID_label)

        self.age_label = QLabel()
        self.info_layout.addWidget(self.age_label)

        self.gender_label = QLabel()
        self.info_layout.addWidget(self.gender_label)

        self.specialty_label = QLabel()
        self.info_layout.addWidget(self.specialty_label)

        self.email_label = QLabel()
        self.info_layout.addWidget(self.email_label)

        self.phone_label = QLabel()
        self.info_layout.addWidget(self.phone_label)

        self.main_layout.addLayout(self.info_layout)

        # Add Edit and Delete buttons
        button_layout = QHBoxLayout()

        self.edit_button = QPushButton("Edit Profile")
        self.edit_button.clicked.connect(self.edit_profile)
        button_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Delete Profile")
        self.delete_button.clicked.connect(self.delete_profile)
        button_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(button_layout)

        self.setLayout(self.main_layout)
        self.fetch_doctor_profile()

    def initialize_database(self):
        self.connection = sqlite3.connect('CallADoctor.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def fetch_doctor_profile(self):
        try:
            self.cursor.execute("SELECT * FROM Doctor WHERE Doctor_ID = ?", (self.doctor_id,))
            doctor = self.cursor.fetchone()

            if doctor:
                self.name_label.setText(f"Name: {doctor['Doctor_Name']}")
                self.ID_label.setText(f"ID: {doctor['Doctor_ID']}")
                self.age_label.setText(f"Age: {doctor['Doctor_Age']}")
                self.gender_label.setText(f"Gender: {doctor['Doctor_Gender']}")
                self.specialty_label.setText(f"Specialty: {doctor['Doctor_Specialization']}")
                self.email_label.setText(f"Email: {doctor['Doctor_Email']}")
                self.phone_label.setText(f"Phone: {doctor['Doctor_Phone']}")
            else:
                QMessageBox.warning(self, "Error", "Doctor profile not found.")
        except sqlite3.Error as e:
            print(f"Error loading doctor profile: {e}")

    def set_profile_picture(self, image_path):
        if os.path.exists(image_path):
            pixmap = QtGui.QPixmap(image_path)
            pixmap = pixmap.scaled(150, 150, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.picture_label.setPixmap(pixmap)
        else:
            self.picture_label.setText("No Image")

    def change_profile_picture(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Profile Picture", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.set_profile_picture(file_name)

    def edit_profile(self):
        self.name_edit = QLineEdit(self.name_label.text().split(": ")[1])
        self.ID_edit = QLineEdit(self.ID_label.text().split(": ")[1])
        self.age_edit = QLineEdit(self.age_label.text().split(": ")[1])
        self.gender_edit = QLineEdit(self.gender_label.text().split(": ")[1])
        self.specialty_edit = QLineEdit(self.specialty_label.text().split(": ")[1])
        self.email_edit = QLineEdit(self.email_label.text().split(": ")[1])
        self.phone_edit = QLineEdit(self.phone_label.text().split(": ")[1])

        self.info_layout.replaceWidget(self.name_label, self.name_edit)
        self.info_layout.replaceWidget(self.ID_label, self.ID_edit)
        self.info_layout.replaceWidget(self.age_label, self.age_edit)
        self.info_layout.replaceWidget(self.gender_label, self.gender_edit)
        self.info_layout.replaceWidget(self.specialty_label, self.specialty_edit)
        self.info_layout.replaceWidget(self.email_label, self.email_edit)
        self.info_layout.replaceWidget(self.phone_label, self.phone_edit)

        self.name_label.hide()
        self.ID_label.hide()
        self.age_label.hide()
        self.gender_label.hide()
        self.specialty_label.hide()
        self.email_label.hide()
        self.phone_label.hide()

        self.edit_button.setText("Save Changes")
        self.edit_button.clicked.disconnect()
        self.edit_button.clicked.connect(self.save_changes)

    def save_changes(self):
        try:
            self.cursor.execute("""
                UPDATE Doctor SET 
                Doctor_Name = ?, 
                Doctor_ID = ?,                
                Doctor_Age = ?,
                Doctor_Gender = ?,                 
                Doctor_Specialization = ?,
                Doctor_Email = ?,
                Doctor_Phone = ?                                  
                WHERE Doctor_ID = ?
            """, (self.name_edit.text(), self.ID_edit.text(), self.age_edit.text(), self.gender_edit.text(), self.specialty_edit.text(), self.email_edit.text(), self.phone_edit.text(), self.doctor_id))
            self.connection.commit()
            QMessageBox.information(self, "Profile Updated", "Your profile has been updated successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Failed to update profile: {e}")

        self.info_layout.replaceWidget(self.name_edit, self.name_label)
        self.info_layout.replaceWidget(self.ID_edit, self.ID_label)
        self.info_layout.replaceWidget(self.age_edit, self.age_label)
        self.info_layout.replaceWidget(self.gender_edit, self.gender_label)
        self.info_layout.replaceWidget(self.specialty_edit, self.specialty_label)
        self.info_layout.replaceWidget(self.email_edit, self.email_label)
        self.info_layout.replaceWidget(self.phone_edit, self.phone_label)

        self.name_edit.deleteLater()
        self.ID_edit.deleteLater()
        self.age_edit.deleteLater()
        self.gender_edit.deleteLater()
        self.specialty_edit.deleteLater()
        self.email_edit.deleteLater()
        self.phone_edit.deleteLater()

        self.name_label.show()
        self.ID_label.show()
        self.age_label.show()
        self.gender_label.show()
        self.specialty_label.show()
        self.email_label.show()
        self.phone_label.show()

        self.edit_button.setText("Edit Profile")
        self.edit_button.clicked.disconnect()
        self.edit_button.clicked.connect(self.edit_profile)

    def delete_profile(self):
        reply = QMessageBox.question(self, 'Delete Profile', 
                                     "Are you sure you want to delete your profile? This action cannot be undone.",
                                     QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.cursor.execute("DELETE FROM Doctor WHERE Doctor_ID = ?", (self.doctor_id,))
                self.connection.commit()
                QMessageBox.information(self, "Profile Deleted", "Your profile has been deleted successfully.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Failed to delete profile: {e}")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 
                                     "Are you sure you want to quit?", 
                                     QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


class Ui_Form(object):
    def __init__(self, doctor_id):
        self.doctor_id = doctor_id
        print(f"Doctor ID: {self.doctor_id}")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logout_button = QtWidgets.QPushButton(Form)
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)
        self.edit_profile_button = QtWidgets.QPushButton(Form)
        self.edit_profile_button.setObjectName("edit_profile_button")
        self.horizontalLayout.addWidget(self.edit_profile_button)
        self.add_prescription_button = QtWidgets.QPushButton(Form)
        self.add_prescription_button.setObjectName("add_prescription_button")
        self.horizontalLayout.addWidget(self.add_prescription_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.logout_button.clicked.connect(self.logout)
        self.edit_profile_button.clicked.connect(self.show_edit_dialog)
        self.add_prescription_button.clicked.connect(self.show_prescription_dialog)

        self.load_Appointments_from_db()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Doctor Dashboard"))
        self.label.setText(_translate("Form", f"Welcome, Dr. {self.get_doctor_name()}!"))
        self.logout_button.setText(_translate("Form", "Logout"))
        self.edit_profile_button.setText(_translate("Form", "Edit Profile"))
        self.add_prescription_button.setText(_translate("Form", "Add Records"))

    def get_doctor_name(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT Doctor_Name FROM Doctor WHERE Doctor_ID = ?", (self.doctor_id,))
                result = cursor.fetchone()
                return result['Doctor_Name'] if result else "Unknown"
            except sqlite3.Error as e:
                print(f"Error fetching doctor name: {e}")
                return "Unknown"
            finally:
                connection.close()
        return "Unknown"

    def logout(self):
        print("Logging out...")
        subprocess.Popen([sys.executable, "startupwindow.py"])
        sys.exit()

    def show_edit_dialog(self):
        self.dialog = DoctorProfileDialog(self.doctor_id)
        self.dialog.exec()

    def show_prescription_dialog(self):
        self.dialog = AddPrescriptionDialog(self.doctor_id)
        self.dialog.exec()

    def load_Appointments_from_db(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    SELECT p.Patient_Name, p.Patient_Age
                    FROM Appointments a
                    JOIN Patient p ON a.Patient_ID = p.Patient_ID
                    WHERE a.Doctor_ID = ?
                """, (self.doctor_id,))
                appointments = cursor.fetchall()

                for appointment in appointments:
                    self.add_patient_card({"name": appointment['Patient_Name'], "age": appointment['Patient_Age']})
            except sqlite3.Error as e:
                print(f"Error fetching appointments: {e}")
            finally:
                connection.close()
        else:
            print("Error: Could not establish database connection")

    def add_patient_card(self, appointment):
        card = QtWidgets.QGroupBox()
        card.setStyleSheet("background-color: rgb(255, 255, 255);")
        card.setTitle("Patient Info")

        layout = QtWidgets.QVBoxLayout()

        name_label = QtWidgets.QLabel(f"Name: {appointment['name']}")
        age_label = QtWidgets.QLabel(f"Age: {appointment['age']}")

        layout.addWidget(name_label)
        layout.addWidget(age_label)

        completion_checkbox = QtWidgets.QCheckBox("Appointment Completed")
        completion_checkbox.setObjectName("completion_checkbox")
        completion_checkbox.stateChanged.connect(lambda state, a=appointment: self.confirm_completion(state, a))
        layout.addWidget(completion_checkbox)

        card.setLayout(layout)
        self.verticalLayout.addWidget(card)

    def confirm_completion(self, state, appointment):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirm Completion")
        msg_box.setText(f"Are you sure you want to mark {appointment['name']}'s appointment as completed?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        msg_box.setIcon(QMessageBox.Icon.Question)
        font = QFont()
        font.setPointSize(10)
        msg_box.setFont(font)
        msg_box.setGeometry(QtCore.QRect(100, 100, 400, 200))
        reply = msg_box.exec()

        if reply == QMessageBox.StandardButton.Yes:
            print(f"Appointment for {appointment['name']} marked as completed.")
        else:
            self.sender().setChecked(False)

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect('CallADoctor.db')
            connection.row_factory = sqlite3.Row
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        return connection


class AddPrescriptionDialog(QDialog):
    def __init__(self, doctor_id, parent=None):
        super().__init__(parent)
        self.doctor_id = doctor_id
        self.setWindowTitle("Add Prescription")
        self.setMinimumSize(400, 350)

        layout = QVBoxLayout()

        self.clinic_name_label = QLabel("Clinic Name:")
        layout.addWidget(self.clinic_name_label)
        self.clinic_name_input = QLineEdit()
        layout.addWidget(self.clinic_name_input)

        self.patient_name_label = QLabel("Patient Name:")
        layout.addWidget(self.patient_name_label)
        self.patient_name_input = QLineEdit()
        layout.addWidget(self.patient_name_input)

        self.date_label = QLabel("Date:")
        layout.addWidget(self.date_label)
        self.date_input = QDateEdit()
        self.date_input.setDisplayFormat("dd/MM/yyyy")
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        layout.addWidget(self.date_input)

        self.time_label = QLabel("Time:")
        layout.addWidget(self.time_label)
        print("Adding CustomTimeEdit...")
        self.time_input = CustomTimeEdit()
        layout.addWidget(self.time_input)
        print("CustomTimeEdit added.")

        self.description_label = QLabel("Description:")
        layout.addWidget(self.description_label)
        self.description_input = QLineEdit()
        layout.addWidget(self.description_input)

        self.prescription_label = QLabel("Prescription:")
        layout.addWidget(self.prescription_label)
        self.prescription_input = QLineEdit()
        layout.addWidget(self.prescription_input)

        button_layout = QHBoxLayout()

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_prescription)
        button_layout.addWidget(save_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        

    def save_prescription(self):
        clinic_name = self.clinic_name_input.text()
        patient_name = self.patient_name_input.text()
        date = self.date_input.date().toString("dd/MM/yyyy")
        time = self.time_input.time().toString("hh:mm AP")
        description = self.description_input.text()
        prescription = self.prescription_input.text()

        if not all([clinic_name, patient_name, date, time, description, prescription]):
            QMessageBox.warning(self, "Incomplete Data", "Please fill all fields.")
            return

        connection = self.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                clinic_id = self.get_clinic_id(cursor, clinic_name)
                if clinic_id is None:
                    QMessageBox.warning(self, "Error", "Clinic not found.")
                    return

                cursor.execute("SELECT Doctor_ID FROM Doctor WHERE Doctor_ID = ?", (self.doctor_id,))
                result = cursor.fetchone()
                if result:
                    doctor_id = result['Doctor_ID']
                else:
                    QMessageBox.warning(self, "Error", "Doctor not found.")
                    return

                cursor.execute("""
                    INSERT INTO Records (Clinic_ID, Patient_ID, Doctor_ID, Date, Time, Description, Prescription)
                    VALUES (
                        ?,
                        (SELECT Patient_ID FROM Patient WHERE Patient_Name = ?),
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    )
                """, (clinic_id, patient_name, doctor_id, date, time, description, prescription))
                connection.commit()
                QMessageBox.information(self, "Prescription Added", "Prescription added successfully.")
                self.accept()
            except sqlite3.Error as e:
                print(f"Error adding prescription: {e}")
                QMessageBox.warning(self, "Error", "An error occurred while adding the prescription.")
            finally:
                connection.close()
        else:
            print("Error: Could not establish database connection")

    def get_clinic_id(self, cursor, clinic_name):
        try:
            cursor.execute("SELECT Clinic_ID FROM Clinic WHERE Clinic_Name = ?", (clinic_name,))
            result = cursor.fetchone()
            return result['Clinic_ID'] if result else None
        except sqlite3.Error as e:
            print(f"Error fetching Clinic ID: {e}")
            return None

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect('CallADoctor.db')
            connection.row_factory = sqlite3.Row
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        return connection


class CustomTimeEdit(QTimeEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDisplayFormat("hh:mm AP")
        self.setTime(QTime.currentTime())
        print("CustomTimeEdit initialized successfully.")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    doctor_id = 1  # Replace this with the actual doctor ID obtained from login
    Form = QtWidgets.QWidget()
    ui = Ui_Form(doctor_id)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
