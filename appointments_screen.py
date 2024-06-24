from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                             QDateEdit, QTimeEdit, QComboBox, QPushButton, QMessageBox, QListWidgetItem)
from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QIcon
from base_screen import BaseScreen, CustomListItem
from view_dialog import ViewDialog
import sqlite3

class AppointmentViewDialog(ViewDialog):
    def __init__(self, appointment_id, clinic_id, parent=None):
        super().__init__("Appointment Details", parent)
        self.appointment_id = appointment_id
        self.clinic_id = clinic_id
        self.load_appointment()

    def load_appointment(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Appointments WHERE Appointment_ID = ? AND Clinic_ID = ?", (self.appointment_id, self.clinic_id))
        appointment = cursor.fetchone()
        conn.close()

        if appointment:
            self.add_field("Appointment ID", str(appointment[0]))
            self.add_field("Clinic ID", str(appointment[1]))
            self.add_field("Patient ID", str(appointment[2]))
            self.add_field("Patient Name", appointment[3])
            self.add_field("Doctor ID", str(appointment[4]))
            self.add_field("Doctor Name", appointment[5])
            self.add_field("Date", appointment[6])
            self.add_field("Time", appointment[7])
            self.add_field("Status", appointment[8])
        else:
            QMessageBox.warning(self, "Error", "Appointment not found or you do not have permission to view this appointment.")
            self.close()


class AppointmentDetailDialog(QDialog):
    def __init__(self, appointment_id=None, clinic_id=None, parent=None, editable=False):
        super().__init__(parent)
        self.appointment_id = appointment_id
        self.clinic_id = clinic_id  # Store clinic_id
        self.setWindowTitle("Appointment Details")
        self.layout = QVBoxLayout(self)

        self.patient_name = QLineEdit()
        self.doctor_name = QLineEdit()
        self.date = QDateEdit()
        self.date.setDate(QDate.currentDate())
        self.date.setMinimumDate(QDate.currentDate())  # Constraint: Can't set appointments in the past
        self.time = QTimeEdit()
        self.time.setTime(QTime.currentTime())
        self.approval = QComboBox()
        self.approval.addItems(["Pending", "Approved", "Rejected"])

        self.layout.addWidget(QLabel("Patient Name:"))
        self.layout.addWidget(self.patient_name)
        self.layout.addWidget(QLabel("Doctor Name:"))
        self.layout.addWidget(self.doctor_name)
        self.layout.addWidget(QLabel("Date:"))
        self.layout.addWidget(self.date)
        self.layout.addWidget(QLabel("Time:"))
        self.layout.addWidget(self.time)
        self.layout.addWidget(QLabel("Approval Status:"))
        self.layout.addWidget(self.approval)

        if editable:
            self.save_button = QPushButton("Save")
            self.save_button.clicked.connect(self.save_appointment)
            self.layout.addWidget(self.save_button)
        else:
            for widget in [self.patient_name, self.doctor_name, self.date, self.time, self.approval]:
                widget.setEnabled(False)

        if appointment_id:
            self.load_appointment()

    def load_appointment(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Appointments WHERE Appointment_ID = ?", (self.appointment_id,))
        appointment = cursor.fetchone()
        conn.close()

        if appointment:
            self.patient_name.setText(appointment[2])
            self.doctor_name.setText(appointment[4])
            self.date.setDate(QDate.fromString(appointment[5], "yyyy-MM-dd"))
            self.time.setTime(QTime.fromString(appointment[6], "HH:mm"))
            self.approval.setCurrentText(appointment[7])

    def save_appointment(self):
        if not self.patient_name.text() or not self.doctor_name.text():
            QMessageBox.warning(self, "Invalid Input", "Please enter both patient and doctor names.")
            return

        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        
        # Check if the doctor exists
        cursor.execute("SELECT * FROM Doctor WHERE Doctor_Name = ?", (self.doctor_name.text(),))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Invalid Doctor", "The specified doctor does not exist.")
            conn.close()
            return

        if self.appointment_id:
            cursor.execute("""
                UPDATE Appointments 
                SET Patient_Name = ?, Doctor_Name = ?, Appointment_Date = ?, 
                    Appointment_Time = ?, Appointment_Approval = ?
                WHERE Appointment_ID = ?
            """, (self.patient_name.text(), self.doctor_name.text(), 
                  self.date.date().toString("yyyy-MM-dd"), 
                  self.time.time().toString("HH:mm"),
                  self.approval.currentText(), self.appointment_id))
        else:
            cursor.execute("""
                INSERT INTO Appointments (Clinic_ID, Patient_Name, Doctor_Name, Appointment_Date, 
                                          Appointment_Time, Appointment_Approval)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (self.clinic_id, self.patient_name.text(), self.doctor_name.text(), 
                  self.date.date().toString("yyyy-MM-dd"), 
                  self.time.time().toString("HH:mm"),
                  self.approval.currentText()))
        conn.commit()
        conn.close()
        self.accept()


class AppointmentsScreen(BaseScreen):
    def __init__(self, clinic_id):
        super().__init__()
        self.clinic_id = clinic_id
        self.current_sort_index = 0
        self.sort_order = Qt.AscendingOrder
        self.sort_combo.addItems(["Patient Name", "Doctor Name", "Date", "Status"])
        self.sort_combo.currentIndexChanged.connect(self.on_sort_changed)

        # Remove add, edit, and delete buttons
        self.add_button.setParent(None)
        self.edit_button.setParent(None)
        self.delete_button.setParent(None)

        # Add approve and reject buttons
        button_layout = QHBoxLayout()
        self.approve_button = QPushButton("Approve")
        self.reject_button = QPushButton("Reject")
        self.approve_button.clicked.connect(self.approve_appointment)
        self.reject_button.clicked.connect(self.reject_appointment)
        button_layout.addWidget(self.approve_button)
        button_layout.addWidget(self.reject_button)
        self.layout.addLayout(button_layout)

        # Connect double-click signal
        self.list_widget.itemDoubleClicked.connect(self.view_appointment)

        self.load_data()

    def load_data(self):
        self.list_widget.clear()
        try:
            conn = sqlite3.connect('CallADoctor.db')
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Appointment_ID, Patient_Name, Doctor_Name, Appointment_Date, Appointment_Approval 
                FROM Appointments 
                WHERE Clinic_ID = ?
            """, (self.clinic_id,))
            appointments = cursor.fetchall()
            conn.close()

            for appointment in appointments:
                item = QListWidgetItem(self.list_widget)
                item_widget = CustomListItem(
                    appointment[0],
                    f"Patient: {appointment[1]} | Doctor: {appointment[2]}",
                    f"Date: {appointment[3]} | Status: {appointment[4]}"
                )
                item.setSizeHint(item_widget.sizeHint())
                self.list_widget.addItem(item)
                self.list_widget.setItemWidget(item, item_widget)
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")

    def sort_items(self):
        try:
            items = []
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                widget = self.list_widget.itemWidget(item)
                if widget:
                    items.append((widget.id, widget.findChild(QLabel).text(), widget.findChildren(QLabel)[1].text()))

            reverse = self.sort_order == Qt.DescendingOrder
            if self.current_sort_index == 0:  # Sort by Patient Name
                items.sort(key=lambda x: x[1].split('|')[0].split(': ')[-1], reverse=reverse)
            elif self.current_sort_index == 1:  # Sort by Doctor Name
                items.sort(key=lambda x: x[1].split('|')[1].split(': ')[-1], reverse=reverse)
            elif self.current_sort_index == 2:  # Sort by Date
                items.sort(key=lambda x: x[2].split('|')[0].split(': ')[-1], reverse=reverse)
            elif self.current_sort_index == 3:  # Sort by Status
                def status_key(x):
                    status = x[2].split('|')[1].split(': ')[-1]
                    if status == "Pending":
                        return 0
                    elif status == "Approved":
                        return 1
                    else:  # Rejected
                        return 2
                items.sort(key=status_key, reverse=reverse)

            self.list_widget.clear()
            for id, main_text, sub_text in items:
                item = QListWidgetItem(self.list_widget)
                item_widget = CustomListItem(id, main_text, sub_text)
                item.setSizeHint(item_widget.sizeHint())
                self.list_widget.addItem(item)
                self.list_widget.setItemWidget(item, item_widget)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while sorting: {e}")

    def on_sort_changed(self, index):
        self.current_sort_index = index
        self.sort_items()

    def toggle_sort_order(self):
        self.sort_order = Qt.DescendingOrder if self.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sort_order_button.setIcon(QIcon(r"C:/Users/nmubu/Desktop/CaD/icon/sort-down-solid.svg" if self.sort_order == Qt.DescendingOrder else r"C:/Users/nmubu/Desktop/CaD/icon/sort-up-solid.svg"))
        self.sort_items()

    def view_appointment(self, item):
        appointment_id = self.list_widget.itemWidget(item).id
        dialog = AppointmentViewDialog(appointment_id, self.clinic_id, self)
        dialog.exec_()

    def approve_appointment(self):
        self.update_appointment_status("Approved")

    def reject_appointment(self):
        self.update_appointment_status("Rejected")

    def update_appointment_status(self, status):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            appointment_id = self.list_widget.itemWidget(selected_items[0]).id
            try:
                conn = sqlite3.connect('CallADoctor.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE Appointments SET Appointment_Approval = ? WHERE Appointment_ID = ?", (status, appointment_id))
                conn.commit()
                conn.close()
                self.load_data()
                QMessageBox.information(self, "Status Updated", f"Appointment status updated to {status}")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Database Error", f"An error occurred while updating status: {e}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
