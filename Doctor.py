
import os
import sys
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt6.QtGui import QFont, QPixmap



class DoctorProfileDialog(QDialog):
    def __init__(self, Form):
        super().__init__()
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

        self.name_label = QLabel()  # Replace with actual name
        self.name_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.info_layout.addWidget(self.name_label)

        self.ID_label = QLabel()  #Doctor ID
        self.info_layout.addWidget(self.ID_label)

        self.age_label = QLabel()  # Replace with actual age
        self.info_layout.addWidget(self.age_label)

        self.gender_label = QLabel()  #Doctor Gender
        self.info_layout.addWidget(self.gender_label)

        self.specialty_label = QLabel()  # Replace with actual specialty
        self.info_layout.addWidget(self.specialty_label)

        self.email_label = QLabel()  #Doctor email
        self.info_layout.addWidget(self.ID_label)

        self.phone_label = QLabel()  #Doctor phone
        self.info_layout.addWidget(self.ID_label)

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

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect('CallADoctor.db')
            connection.row_factory = sqlite3.Row
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        return connection


    def fetch_doctor_profile(self):
        connection = self.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                self.cursor.execute("SELECT * FROM Doctor WHERE Doctor_Name = '?'")
                doctor = self.cursor.fetchone()

                if doctor:
                    self.name_label.setText(f"Name: {doctor['Doctor_Name']}")
                    self.ID_label.setText(f"ID: {doctor['Doctor_ID']}")
                    self.age_label.setText(f"Age: {doctor['Doctor_Age']}")
                    self.gender_label.setText(f"Name: {doctor['Doctor_Gender']}")
                    self.specialty_label.setText(f"Specialty: {doctor['Doctor_Specialization']}")
                    self.email_label.setText(f"Email: {doctor['Doctor_Email']}")
                    self.phone_label.setText(f"Phone: {doctor['Doctor_Phone']}")

                else:
                    QMessageBox.warning(self, "Error", "Doctor profile not found.")

            except sqlite3.Error as e:
                print(f"Error loading doctor profile: {e}")

            finally:
                connection.close()

    def set_profile_picture(self, image_path):
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(150, 150, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.picture_label.setPixmap(pixmap)
        else:
            self.picture_label.setText("No Image")

    def change_profile_picture(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Profile Picture", "", "Image Files (*.png *.jpg *.bmp *.jpeg)")
        if file_name:
            self.set_profile_picture(file_name)


    def edit_profile(self):
        # Create input fields for editing
        self.name_edit = QLineEdit(self.name_label.text().split(": ")[1])
        self.ID_edit = QLineEdit(self.ID_label.text().split(": ")[1])
        self.age_edit = QLineEdit(self.age_label.text().split(": ")[1])
        self.gender_edit = QLineEdit(self.gender_label.text().split(": ")[1])
        self.specialty_edit = QLineEdit(self.specialty_label.text().split(": ")[1])
        self.email_edit = QLineEdit(self.email_label.text().split(": ")[1])
        self.phone_edit = QLineEdit(self.phone_label.text().split(": ")[1])

        # Replace labels with edit fields
        self.info_layout.replaceWidget(self.name_label, self.name_edit)
        self.info_layout.replaceWidget(self.ID_label, self.ID_edit)
        self.info_layout.replaceWidget(self.age_label, self.age_edit)
        self.info_layout.replaceWidget(self.gender_label, self.gender_edit)
        self.info_layout.replaceWidget(self.specialty_label, self.specialty_edit)
        self.info_layout.replaceWidget(self.email_label, self.email_edit)
        self.info_layout.replaceWidget(self.phone_label, self.phone_edit)

        # Hide labels
        self.name_label.hide()
        self.ID_label.hide()
        self.age_label.hide()
        self.gender_label.hide()
        self.specialty_label.hide()
        self.email_label.hide()
        self.phone_label.hide()

        # Change Edit button to Save
        self.edit_button.setText("Save Changes")
        self.edit_button.clicked.disconnect()
        self.edit_button.clicked.connect(self.save_changes)

    def save_changes(self):
        # Update labels with new information
        self.name_label.setText(f"Name: {self.name_edit.text()}")
        self.ID_label.setText(f"ID: {self.ID_edit.text()}")
        self.age_label.setText(f"Age: {self.age_edit.text()}")
        self.gender_label.setText(f"Gender: {self.gender_edit.text()}")
        self.specialty_label.setText(f"Specialty: {self.specialty_edit.text()}")
        self.email_label.setText(f"Email: {self.email_edit.text()}")
        self.phone_label.setText(f"Phone: {self.phone_edit.text()}")

        # Save changes to the database
        try:
            self.cursor.execute("""
                UPDATE Doctor SET 
                Doctor_Name = ?, 
                Doctor_ID = ?,                
                Doctor_Age = ?,
                Doctor_Gender = ?,                 
                Doctor_Specialization = ?,
                Doctor_Email = ?,
                Doctor_Phone = ?,                                 
                WHERE Doctor_Name = ?
            """, (self.name_edit.text(), self.ID_edit.text(), self.age_edit.text(), self.gender_edit.text(), self.specialty_edit.text(), self.email_edit.text(), self.phone_edit.text(), 'Dr. John Doe'))
            self.connection.commit()
            QMessageBox.information(self, "Profile Updated", "Your profile has been updated successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Failed to update profile: {e}")

        # Remove edit fields and show labels
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
        self.ID_edit.deleteLater()
        self.age_label.show()
        self.gender_edit.deleteLater()
        self.specialty_label.show()
        self.email_label.show()
        self.phone_edit.deleteLater()

        # Change Save button back to Edit
        self.edit_button.setText("Edit Profile")
        self.edit_button.clicked.disconnect()
        self.edit_button.clicked.connect(self.edit_profile)

        QMessageBox.information(self, "Profile Updated", "Your profile has been updated successfully.")

        # Initialize and fetch the doctor's profile data
        self.initialize_database()
        self.fetch_doctor_profile()


    def delete_profile(self):
        reply = QMessageBox.question(self, 'Delete Profile', 
                                     "Are you sure you want to delete your profile? This action cannot be undone.",
                                     QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.cursor.execute("DELETE FROM Doctor WHERE Doctor_Name = '?'")
                self.connection.commit()
                QMessageBox.information(self, "Profile Deleted", "Your profile has been deleted successfully.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Failed to delete profile: {e}")

            self.close()

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

        self.connection.close()


class Ui_Form(object):
    def setupUi(self, Form):
        self.form = Form  # Store reference to the Form
        Form.setObjectName("Form")
        Form.resize(761, 506)
        self.main_layout = QtWidgets.QVBoxLayout(Form)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.CAD = QtWidgets.QLabel(parent=Form)
        self.CAD.setGeometry(QtCore.QRect(220, 0, 301, 61))
        self.CAD.setStyleSheet("font: 28pt;")
        self.CAD.setObjectName("CAD")

        self.greetings = QtWidgets.QLabel(parent=Form)
        self.greetings.setGeometry(QtCore.QRect(70, 50, 301, 61))
        self.greetings.setStyleSheet("font: 25pt;")
        self.greetings.setObjectName("greetings")

        #Add Prescription
        self.add_prescription_button = QtWidgets.QPushButton(Form)
        self.add_prescription_button.setObjectName("add_prescription_button")
        self.horizontalLayout.addWidget(self.add_prescription_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        # Add the View Profile button
        self.view_profile_btn = QtWidgets.QPushButton(parent=Form)
        self.view_profile_btn.setGeometry(QtCore.QRect(450, 60, 120, 30))
        self.view_profile_btn.setObjectName("view_profile_btn")
        self.view_profile_btn.setText("View Profile")
        self.view_profile_btn.clicked.connect(self.open_doctor_profile)

        # Add the Log Out button
        self.logout_btn = QtWidgets.QPushButton(parent=Form)
        self.logout_btn.setGeometry(QtCore.QRect(600, 60, 120, 30))
        self.logout_btn.setObjectName("logout_btn")
        self.logout_btn.setText("Log Out")
        self.logout_btn.clicked.connect(self.logout)

        #Patient Card view
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setGeometry(QtCore.QRect(40, 140, 671, 331))
        self.scrollArea.setStyleSheet("selection-color: rgb(85, 255, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.load_Appointments_from_db()
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Doctor Dashboard"))
        self.CAD.setText(_translate("Form", "Call a Doctor(CaD)"))
        self.greetings.setText(_translate("Form", "Welcome, Dr."))


    def view_details(self, appointment):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                # Fetch patient details
                cursor.execute("""
                    SELECT p.Patient_Name, p.Patient_Age, p.Patient_Sex, p.Patient_Address, p.Patient_PhoneNo, p.Patient_Email, a.Patient_Name as details
                    FROM Patient p
                    LEFT JOIN Appointments a ON p.Patient_ID = a.Patient_ID
                    WHERE p.Patient_Name = ?
                """, (appointment['name'],))
                patient_details = cursor.fetchone()
                
                if patient_details:
                    message = f"Name: {patient_details['Patient_Name']}\n"
                    message += f"Age: {patient_details['Patient_Age']}\n"
                    message += f"Gender: {patient_details['Patient_Sex']}\n"
                    message += f"Details: {appointment['Description']}\n\n"
                    message += "Medical Records:\n"

                    # Fetch medical records
                    cursor.execute("""
                        SELECT Description, Prescription
                        FROM Records
                        WHERE Patient_ID = (SELECT Patient_ID FROM Patient WHERE Patient_Name = ?)
                    """, (appointment['name'],))
                    records = cursor.fetchall()

                    for record in records:
                        message += f"- Description: {record['Description']}\n"
                        message += f"  Prescription: {record['Prescription']}\n\n"
                else:
                    message = "No detailed information available for this patient."
                
                QMessageBox.information(self.form, "Patient Details", message)
            except sqlite3.Error as e:
                print(f"Error fetching patient details: {e}")
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
        appointment_time_label = QtWidgets.QLabel(f"Appointment Time: {appointment['Appointment_Time']}")
        appointment_date_label = QtWidgets.QLabel(f"Appointment Date: {appointment['Appointment_Date']}")

        layout.addWidget(name_label)
        layout.addWidget(age_label)
        layout.addWidget(appointment_time_label)
        layout.addWidget(appointment_date_label)

        self.main_layout.addWidget(card)
        
        # Checkbox to indicate completion
        completion_checkbox = QtWidgets.QCheckBox("Appointment Completed")
        completion_checkbox.setObjectName("completion_checkbox")
        completion_checkbox.stateChanged.connect(lambda state, a=appointment: self.confirm_completion(state, a))
        layout.addWidget(completion_checkbox)

        view_medical_history_btn = QtWidgets.QPushButton("View Medical Records")
        view_medical_history_btn.clicked.connect(lambda checked, a=appointment: self.view_details(a))
        layout.addWidget(view_medical_history_btn)
            
        prescribe_btn = QtWidgets.QPushButton("Prescribe Medication")
        prescribe_btn.clicked.connect(lambda checked, a=appointment: self.prescribe_medication(a))
        layout.addWidget(prescribe_btn)

        card.setLayout(layout)
        self.verticalLayout.addWidget(card)
        layout.addWidget(prescribe_btn)



    def load_Appointments_from_db(self):
        connection = self.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT a.Patient_Name, p.Patient_Age
                    FROM Appointments a
                    JOIN Patient p ON a.Patient_ID = p.Patient_ID
                               
                    SELECT Appointment_Time, Appointment_Date
                    FROM Appointments
                """)
                appointments = cursor.fetchall()

                for appointment in appointments:
                    self.add_patient_card({
                        "name": appointment['Patient_Name'], 
                        "age": appointment['Patient_Age'],
                        "time": appointment['Appointment_Time'],
                        "date": appointment['Appointment_Date']
                    })
            except sqlite3.Error as e:
                print(f"Error fetching appointments: {e}")
            finally:
                connection.close()
        else:
            print("Error: Could not establish database connection")



    def show_prescription_dialog(self):
        self.dialog = AddPrescriptionDialog()
        self.dialog.exec()



    def prescribe_medication(self, appointment):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Records (Patient_ID, Doctor_ID, Date, Time, Description, Prescription)
                    SELECT p.Patient_ID, d.Doctor_ID, DATE('now'), TIME('now'), 'New prescription', ?
                    FROM Patient p, Doctor d
                    WHERE p.Patient_Name = ? AND d.Doctor_Name = ?
                """, ('New medication prescribed', appointment['name'], 'Current Doctor Name'))
                connection.commit()
                QMessageBox.information(self.form, "Prescribe Medication", f"Medication prescribed for {appointment['name']}")
            except sqlite3.Error as e:
                print(f"Error prescribing medication: {e}")
            finally:
                connection.close()
        else:
            print("Error: Could not establish database connection")


    def confirm_completion(self, state, appointment):
        # Create a custom QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirm Completion")
        msg_box.setText(f"Are you sure you want to mark {appointment['name']}'s appointment as completed?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
            
        # Set icon
        msg_box.setIcon(QMessageBox.Icon.Question)
         
        # Set font
        font = QFont()
        font.setPointSize(10)
        msg_box.setFont(font)

        # Center the dialog on the screen
        msg_box.setGeometry(QtCore.QRect(100, 100, 400, 200))

        # Show the message box and get the user's response
        reply = msg_box.exec()
            
        if reply == QMessageBox.StandardButton.Yes:
            print(f"Appointment for {appointment['name']} marked as completed.")
        else:
            # If user clicks 'No', uncheck the checkbox
            self.sender().setChecked(False)


    def open_doctor_profile(self):
        dialog = DoctorProfileDialog(self.form)
        dialog.exec()

    def show_prescription_dialog(self):
        self.dialog = AddPrescriptionDialog()
        self.dialog.exec()

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect('CallADoctor.db')
            connection.row_factory = sqlite3.Row 
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        return connection

    def logout(self):
        reply = QMessageBox.question(self.form, 'Log Out', 
                                     "Are you sure you want to log out?",
                                     QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self.form, 'Logged Out', "You have been successfully logged out.")
            # Here you would typically close the current window and open the login window
            # For demonstration, we'll just close the current window
            self.form.close()
        else:
            # User chose not to log out, do nothing
            pass

    def view_medical_history(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    SELECT p.*, r.Description, r.Prescription
                    FROM Patient p
                    LEFT JOIN Records r ON p.Patient_ID = r.Patient_ID
                    WHERE p.Patient_Name = ?
                """, (AddPrescriptionDialog['name']))
                patient_details = cursor.fetchone()
                
                if patient_details:
                    message = f"Name: {patient_details['Patient_Name']}\n"
                    message += f"Age: {patient_details['Patient_Age']}\n"
                    message += f"Sex: {patient_details['Patient_Gender']}\n"
                    message += f"Address: {patient_details['Patient_Address']}\n"
                    message += f"Phone: {patient_details['Patient_PhoneNo']}\n"
                    message += f"Email: {patient_details['Patient_Email']}\n"
                    message += f"Latest Description: {patient_details['Description'] or 'N/A'}\n"
                    message += f"Latest Prescription: {patient_details['Prescription'] or 'N/A'}"
                else:
                    message = "No detailed information available for this patient."
                
                QMessageBox.information(self.form, "Patient Details", message)
            except sqlite3.Error as e:
                print(f"Error fetching patient details: {e}")
            finally:
                connection.close()
        else:
            print("Error: Could not establish database connection")
    

class AddPrescriptionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Prescription")
        self.setMinimumSize(300, 200)

        layout = QVBoxLayout()

        self.prescription_label = QLabel("Prescription:")
        layout.addWidget(self.prescription_label)

        self.prescription_text = QLineEdit()
        layout.addWidget(self.prescription_text)

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
        prescription = self.prescription_input.text()
        description = self.prescription_input.text()

        if not (prescription and description):
            QMessageBox.warning(self, "Incomplete Data", "Please fill all fields.")
            return

        connection = self.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO Records (Patient_ID, Prescription, Description)
                    VALUES (?, ?, ?)
                """, (prescription, description))
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

            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
