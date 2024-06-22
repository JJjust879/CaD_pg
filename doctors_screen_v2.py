from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                             QComboBox, QPushButton, QMessageBox, QFileDialog, QListWidgetItem, QSpinBox)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator
from base_screen import BaseScreen, CustomListItem
from view_dialog import ViewDialog
import sqlite3
class PhoneEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setInputMask('(999) 999-9999')

class DoctorViewDialog(ViewDialog):
    def __init__(self, doctor_id, parent=None):
        super().__init__("Doctor Details", parent)
        self.doctor_id = doctor_id
        self.load_doctor()

    def load_doctor(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Doctor WHERE Doctor_ID = ?", (self.doctor_id,))
        doctor = cursor.fetchone()
        conn.close()

        if doctor:
            if doctor[8]:  # Assuming the portrait is stored as BLOB
                pixmap = QPixmap()
                pixmap.loadFromData(doctor[8])
                self.add_image(pixmap)
            self.add_field("Name", f"Dr. {doctor[2]}")
            self.add_field("Specialization", doctor[3])
            self.add_field("Age", str(doctor[4]))
            self.add_field("Gender", doctor[5])
            self.add_field("Email", doctor[6])
            self.add_field("Phone", doctor[7])

class DoctorDetailDialog(QDialog):
    def __init__(self, doctor_id=None, parent=None, editable=False):
        super().__init__(parent)
        self.doctor_id = doctor_id
        self.setWindowTitle("Doctor Details")
        self.layout = QVBoxLayout(self)

        self.name = QLineEdit()
        self.specialization = QLineEdit()
        self.age = QSpinBox()
        self.age.setRange(18, 100)
        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female", "Other"])
        self.email = QLineEdit()
        email_regex = QRegExp(r"[^@]+@[^@]+\.[^@]+")
        self.email.setValidator(QRegExpValidator(email_regex))
        self.phone = PhoneEdit()
        self.portrait_path = ""
        self.portrait_label = QLabel()
        self.portrait_button = QPushButton("Select Portrait")
        self.portrait_button.clicked.connect(self.select_portrait)

        self.layout.addWidget(QLabel("Name:"))
        self.layout.addWidget(self.name)
        self.layout.addWidget(QLabel("Specialization:"))
        self.layout.addWidget(self.specialization)
        self.layout.addWidget(QLabel("Age:"))
        self.layout.addWidget(self.age)
        self.layout.addWidget(QLabel("Gender:"))
        self.layout.addWidget(self.gender)
        self.layout.addWidget(QLabel("Email:"))
        self.layout.addWidget(self.email)
        self.layout.addWidget(QLabel("Phone:"))
        self.layout.addWidget(self.phone)
        self.layout.addWidget(self.portrait_label)
        self.layout.addWidget(self.portrait_button)

        if editable:
            self.save_button = QPushButton("Save")
            self.save_button.clicked.connect(self.save_doctor)
            self.layout.addWidget(self.save_button)
        else:
            for widget in [self.name, self.specialization, self.age, self.gender, self.email, self.phone]:
                widget.setEnabled(False)
            self.portrait_button.setEnabled(False)

        if doctor_id:
            self.load_doctor()

    def load_doctor(self):
        try:
            conn = sqlite3.connect('CallADoctor.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Doctor WHERE Doctor_ID = ?", (self.doctor_id,))
            doctor = cursor.fetchone()
            conn.close()

            if doctor:
                self.name.setText(doctor[2])
                self.specialization.setText(doctor[3])
                self.age.setValue(doctor[4])
                self.gender.setCurrentText(doctor[5])
                self.email.setText(doctor[6])
                self.phone.setText(doctor[7])
                if doctor[8]:  # Assuming the portrait is stored as BLOB
                    pixmap = QPixmap()
                    pixmap.loadFromData(doctor[8])
                    self.portrait_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                raise Exception("Doctor not found")
        except sqlite3.Error as e:
            raise Exception(f"Database error: {e}")
        except Exception as e:
            raise Exception(f"Error loading doctor data: {e}")

    def select_portrait(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Portrait", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.portrait_path = file_name
            pixmap = QPixmap(file_name)
            self.portrait_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))

    def save_doctor(self):
        if self.age.value() < 18:
            QMessageBox.warning(self, "Invalid Input", "Doctor must be at least 18 years old.")
            return

        try:
            conn = sqlite3.connect('CallADoctor.db')
            cursor = conn.cursor()

            portrait_data = None
            if self.portrait_path:
                with open(self.portrait_path, 'rb') as file:
                    portrait_data = file.read()

            if self.doctor_id:
                cursor.execute("""
                    UPDATE Doctor 
                    SET Doctor_Name = ?, Doctor_Specialization = ?, Doctor_Age = ?, 
                        Doctor_Gender = ?, Doctor_Email = ?, Doctor_Phone = ?, Doctor_Portrait = ?
                    WHERE Doctor_ID = ?
                """, (self.name.text(), self.specialization.text(), self.age.value(), 
                    self.gender.currentText(), self.email.text(), self.phone.text(), 
                    portrait_data, self.doctor_id))
            else:
                cursor.execute("""
                    INSERT INTO Doctor (Doctor_Name, Doctor_Specialization, Doctor_Age, 
                                        Doctor_Gender, Doctor_Email, Doctor_Phone, Doctor_Portrait)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (self.name.text(), self.specialization.text(), self.age.value(), 
                    self.gender.currentText(), self.email.text(), self.phone.text(), portrait_data))
            
            conn.commit()
            conn.close()
            print(f"Doctor {'updated' if self.doctor_id else 'added'}: {self.name.text()}")
            self.accept()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while saving the doctor: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")

class DoctorsScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.current_sort_index = 0
        self.sort_order = Qt.AscendingOrder
        self.sort_combo.addItems(["Name", "Specialization", "Age"])
        self.add_button.clicked.connect(self.add_doctor)
        self.edit_button.clicked.connect(self.edit_doctor)
        self.delete_button.clicked.connect(self.delete_doctor)
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        self.list_widget.itemDoubleClicked.connect(self.view_doctor)
        self.load_data()

    def sort_items(self):
        try:
            items = []
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                widget = self.list_widget.itemWidget(item)
                if widget:
                    items.append((widget.id, widget.findChild(QLabel).text(), widget.findChildren(QLabel)[1].text()))

            reverse = self.sort_order == Qt.DescendingOrder
            if self.current_sort_index == 0:  # Sort by Name
                items.sort(key=lambda x: x[1].split('. ')[-1], reverse=reverse)
            elif self.current_sort_index == 1:  # Sort by Specialization
                items.sort(key=lambda x: x[2].split('|')[0].split(': ')[-1], reverse=reverse)
            elif self.current_sort_index == 2:  # Sort by Age
                items.sort(key=lambda x: int(x[2].split('|')[1].split(': ')[-1]), reverse=reverse)

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
        self.sort_order_button.setIcon(QIcon("C:/Users/nmubu/Desktop/CaD/icon/sort-down-solid.svg" if self.sort_order == Qt.DescendingOrder else "C:/Users/nmubu/Desktop/CaD/icon/sort-up-solid.svg"))
        self.sort_items()

    def on_item_clicked(self, item):
        self.edit_button.setEnabled(True)
        self.delete_button.setEnabled(True)

    def load_data(self):
        self.list_widget.clear()
        try:
            conn = sqlite3.connect('CallADoctor.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Doctor_ID, Doctor_Name, Doctor_Specialization, Doctor_Age FROM Doctor")
            doctors = cursor.fetchall()
            conn.close()

            for doctor in doctors:
                item = QListWidgetItem(self.list_widget)
                item_widget = CustomListItem(
                    doctor[0],
                    f"Dr. {doctor[1]}",
                    f"Specialization: {doctor[2]} | Age: {doctor[3]}"
                )
                item.setSizeHint(item_widget.sizeHint())
                self.list_widget.addItem(item)
                self.list_widget.setItemWidget(item, item_widget)

            print(f"Loaded {self.list_widget.count()} doctors")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while loading doctors: {e}")

    def view_doctor(self, item):
        try:
            doctor_id = self.list_widget.itemWidget(item).id
            dialog = DoctorViewDialog(doctor_id, self)
            dialog.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while viewing the doctor: {e}")

    def add_doctor(self):
        dialog = DoctorDetailDialog(parent=self, editable=True)
        if dialog.exec_():
            self.load_data()

    def edit_doctor(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            doctor_id = self.list_widget.itemWidget(selected_items[0]).id
            dialog = DoctorDetailDialog(doctor_id, self, editable=True)
            if dialog.exec_():
                self.load_data()

    def delete_doctor(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            doctor_id = self.list_widget.itemWidget(selected_items[0]).id
            reply = QMessageBox.question(self, 'Delete Doctor', 
                                         'Are you sure you want to delete this doctor?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                conn = sqlite3.connect('CallADoctor.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Doctor WHERE Doctor_ID = ?", (doctor_id,))
                conn.commit()
                conn.close()
                self.load_data()

    def update_sort_indicator(self, index):
        pass

