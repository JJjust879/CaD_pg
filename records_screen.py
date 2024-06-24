from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QTextEdit, QPushButton, QMessageBox, QListWidgetItem,
                             QDateEdit, QTimeEdit, QSpinBox)
from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QIcon
from base_screen import BaseScreen, CustomListItem
from view_dialog import ViewDialog
import sqlite3

class RecordViewDialog(ViewDialog):
    def __init__(self, record_id, clinic_id, parent=None):
        super().__init__("Record Details", parent)
        self.record_id = record_id
        self.clinic_id = clinic_id  # Store clinic_id
        self.load_record()

    def load_record(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Records WHERE Record_ID = ? AND Clinic_ID = ?", (self.record_id, self.clinic_id))
        record = cursor.fetchone()
        conn.close()

        if record:
            self.add_field("Patient Name", record[2])
            self.add_field("Doctor Name", record[4])
            self.add_field("Date", record[5])
            self.add_field("Time", record[6])
            self.add_field("Description", record[7])
            self.add_field("Prescription", record[8])
        else:
            QMessageBox.warning(self, "Error", "Record not found or you do not have permission to view this record.")
            self.close()


class RecordDetailDialog(QDialog):
    def __init__(self, record_id=None, clinic_id=None, parent=None, editable=False):
        super().__init__(parent)
        self.record_id = record_id
        self.clinic_id = clinic_id  # Store clinic_id
        self.setWindowTitle("Record Details")
        self.layout = QVBoxLayout(self)

        self.patient_name = QLineEdit()
        self.doctor_name = QLineEdit()

        self.date = QDateEdit()
        self.date.setCalendarPopup(True)
        self.date.setDateRange(QDate(1900, 1, 1), QDate.currentDate()) 
        
        self.time = QTimeEdit()
        self.time.setDisplayFormat("HH:mm")

        self.description = QTextEdit()
        self.prescription = QTextEdit()

        self.layout.addWidget(QLabel("Patient Name:"))
        self.layout.addWidget(self.patient_name)
        self.layout.addWidget(QLabel("Doctor Name:"))
        self.layout.addWidget(self.doctor_name)
        self.layout.addWidget(QLabel("Date:"))
        self.layout.addWidget(self.date)
        self.layout.addWidget(QLabel("Time:"))
        self.layout.addWidget(self.time)
        self.layout.addWidget(QLabel("Description:"))
        self.layout.addWidget(self.description)
        self.layout.addWidget(QLabel("Prescription:"))
        self.layout.addWidget(self.prescription)

        if editable:
            self.save_button = QPushButton("Save")
            self.save_button.clicked.connect(self.save_record)
            self.layout.addWidget(self.save_button)
        else:
            for widget in [self.patient_name, self.doctor_name, self.date, self.time, self.description, self.prescription]:
                widget.setReadOnly(True)

        if record_id:
            self.load_record()

    def load_record(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Records WHERE Record_ID = ?", (self.record_id,))
        record = cursor.fetchone()
        conn.close()

        if record:
            self.patient_name.setText(record[2])
            self.doctor_name.setText(record[4])
            self.date.setDate(QDate.fromString(record[5], "yyyy-MM-dd"))
            self.time.setTime(QTime.fromString(record[6], "HH:mm:ss"))
            self.description.setText(record[7])
            self.prescription.setText(record[8])

    def save_record(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        try:
            if self.record_id:
                cursor.execute("""
                    UPDATE Records 
                    SET Patient_Name = ?, Doctor_Name = ?, Date = ?, Time = ?, Description = ?, Prescription = ?
                    WHERE Record_ID = ?
                """, (self.patient_name.text(), self.doctor_name.text(), self.date.date().toString("yyyy-MM-dd"), 
                      self.time.time().toString("HH:mm:ss"), self.description.toPlainText(), 
                      self.prescription.toPlainText(), self.record_id))
            else:
                cursor.execute("""
                    INSERT INTO Records (Clinic_ID, Patient_Name, Doctor_Name, Date, Time, Description, Prescription)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (self.clinic_id, self.patient_name.text(), self.doctor_name.text(), self.date.date().toString("yyyy-MM-dd"), 
                      self.time.time().toString("HH:mm:ss"), self.description.toPlainText(), 
                      self.prescription.toPlainText()))
            conn.commit()
            QMessageBox.information(self, "Success", "Record saved successfully.")
            self.accept()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
        finally:
            conn.close()


class RecordsScreen(BaseScreen):
    def __init__(self, clinic_id):
        super().__init__()
        self.clinic_id = clinic_id
        self.current_sort_index = 0
        self.sort_order = Qt.AscendingOrder
        self.sort_combo.addItems(["Patient Name", "Doctor Name", "Date"])
        self.add_button.clicked.connect(self.add_record)
        self.edit_button.clicked.connect(self.edit_record)
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        self.list_widget.itemDoubleClicked.connect(self.view_record)
        self.delete_button.setParent(None)
        self.load_data()

    def load_data(self):
        self.list_widget.clear()
        try:
            conn = sqlite3.connect('CallADoctor.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Record_ID, Patient_Name, Doctor_Name, Date FROM Records WHERE Clinic_ID = ?", (self.clinic_id,))
            records = cursor.fetchall()
            conn.close()

            for record in records:
                item = QListWidgetItem(self.list_widget)
                item_widget = CustomListItem(
                    record[0],
                    f"Patient: {record[1]}",
                    f"Doctor: {record[2]} | Date: {record[3]}"
                )
                item.setSizeHint(item_widget.sizeHint())
                self.list_widget.addItem(item)
                self.list_widget.setItemWidget(item, item_widget)
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")

    def on_item_clicked(self, item):
        self.edit_button.setEnabled(True)

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
                items.sort(key=lambda x: x[1].split(': ')[-1], reverse=reverse)
            elif self.current_sort_index == 1:  # Sort by Doctor Name
                items.sort(key=lambda x: x[2].split('|')[0].split(': ')[-1], reverse=reverse)
            elif self.current_sort_index == 2:  # Sort by Date
                items.sort(key=lambda x: x[2].split('|')[1].split(': ')[-1], reverse=reverse)

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

    def update_sort_indicator(self, index):
        pass

    def view_record(self, item):
        record_id = self.list_widget.itemWidget(item).id
        dialog = RecordViewDialog(record_id, self)
        dialog.exec_()

    def add_record(self):
        dialog = RecordDetailDialog(parent=self, editable=True)
        if dialog.exec_():
            self.load_data()

    def edit_record(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            record_id = self.list_widget.itemWidget(selected_items[0]).id
            dialog = RecordDetailDialog(record_id, self, editable=True)
            if dialog.exec_() == QDialog.Accepted:
                self.load_data()
        else:
            QMessageBox.warning(self, "No Selection", "Please select a record to edit.")
    
    def toggle_sort_order(self):
        self.sort_order = Qt.DescendingOrder if self.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sort_order_button.setIcon(QIcon("icon/sort-down-solid.svg" if self.sort_order == Qt.DescendingOrder else "icon/sort-up-solid.svg"))
        self.sort_items()

