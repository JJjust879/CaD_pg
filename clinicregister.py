from PyQt6 import QtCore, QtGui, QtWidgets
import ClinicLoginRegisterbuttons
import sqlite3


class Ui_clinicRegister(object):
    def setupUi(self, clinicRegister):
        clinicRegister.setObjectName("clinicRegister")
        clinicRegister.resize(800, 500)
        clinicRegister.setMinimumSize(QtCore.QSize(800, 500))
        clinicRegister.setMaximumSize(QtCore.QSize(800, 500))
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=clinicRegister)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("clinic.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Location = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Location.setFont(font)
        self.Location.setObjectName("Location")
        self.gridLayout.addWidget(self.Location, 2, 1, 1, 1)
        self.ConfirmPasswordEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ConfirmPasswordEdit.setFont(font)
        self.ConfirmPasswordEdit.setObjectName("ConfirmPasswordEdit")
        self.ConfirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.gridLayout.addWidget(self.ConfirmPasswordEdit, 5, 2, 1, 1)
        self.PhoneNumber = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PhoneNumber.setFont(font)
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.gridLayout.addWidget(self.PhoneNumber, 3, 1, 1, 1)
        self.Password = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 4, 1, 1, 1)
        self.PhoneNumberEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PhoneNumberEdit.setFont(font)
        self.PhoneNumberEdit.setObjectName("PhoneNumberEdit")
        self.PhoneNumberEdit.setInputMask("9999999999")  # Set input mask to allow only 10 digits
        self.gridLayout.addWidget(self.PhoneNumberEdit, 3, 2, 1, 1)
        self.ConfirmPassword = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ConfirmPassword.setFont(font)
        self.ConfirmPassword.setObjectName("ConfirmPassword")
        self.gridLayout.addWidget(self.ConfirmPassword, 5, 1, 1, 1)
        self.ClinicNameEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClinicNameEdit.setFont(font)
        self.ClinicNameEdit.setObjectName("ClinicNameEdit")
        self.gridLayout.addWidget(self.ClinicNameEdit, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton { background-color: lightgreen }")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 3, 1, 1)
        self.ClinicName = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClinicName.setFont(font)
        self.ClinicName.setObjectName("ClinicName")
        self.gridLayout.addWidget(self.ClinicName, 0, 1, 1, 1)
        self.LocationEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LocationEdit.setFont(font)
        self.LocationEdit.setObjectName("LocationEdit")
        self.gridLayout.addWidget(self.LocationEdit, 2, 2, 1, 1)
        self.PasswordEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordEdit.setFont(font)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.gridLayout.addWidget(self.PasswordEdit, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton { background-color: lightgreen }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(clinicRegister)
        QtCore.QMetaObject.connectSlotsByName(clinicRegister)

        # Connect buttons and checkbox
        self.pushButton.clicked.connect(self.openClinicLoginRegisterbuttons)
        self.pushButton_2.clicked.connect(self.register_clinic)
        self.checkBox.stateChanged.connect(self.toggle_password_visibility)

        self.current_window = clinicRegister  # Set the current window attribute

    def retranslateUi(self, clinicRegister):
        _translate = QtCore.QCoreApplication.translate
        clinicRegister.setWindowTitle(_translate("clinicRegister", "Clinic Register"))
        self.Location.setText(_translate("clinicRegister", "Location:"))
        self.PhoneNumber.setText(_translate("clinicRegister", "Phone Number:"))
        self.Password.setText(_translate("clinicRegister", "Password:"))
        self.ConfirmPassword.setText(_translate("clinicRegister", "Confirm Password:"))
        self.pushButton.setText(_translate("clinicRegister", "Back"))
        self.checkBox.setText(_translate("clinicRegister", "Show Password"))
        self.ClinicName.setText(_translate("clinicRegister", "Clinic Name:"))
        self.pushButton_2.setText(_translate("clinicRegister", "Register"))

    def openClinicLoginRegisterbuttons(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = ClinicLoginRegisterbuttons.Ui_ClinicLoginRegisterbuttons()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def toggle_password_visibility(self):
        if self.checkBox.isChecked():
            self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.ConfirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.ConfirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def register_clinic(self):
        clinic_name = self.ClinicNameEdit.text()
        location = self.LocationEdit.text()
        phone_number = self.PhoneNumberEdit.text()
        password = self.PasswordEdit.text()
        confirm_password = self.ConfirmPasswordEdit.text()

        if not all([clinic_name, location, phone_number, password, confirm_password]):
            QtWidgets.QMessageBox.warning(self.current_window, "Error", "All fields must be filled")
            return

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self.current_window, "Error", "Passwords do not match")
            return

        if not phone_number.isdigit():
            QtWidgets.QMessageBox.warning(self.current_window, "Error", "Phone number must contain only digits")
            return

        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()

        try:
            # Check if the clinic name already exists
            cursor.execute('SELECT COUNT(*) FROM Clinic WHERE Clinic_Name = ?', (clinic_name,))
            if cursor.fetchone()[0] > 0:
                QtWidgets.QMessageBox.warning(self.current_window, "Error", "Clinic name already exists")
                return

            cursor.execute('''
                INSERT INTO Clinic (Clinic_Name, Clinic_Location, Clinic_Phone, Clinic_Password, Clinic_Approval)
                VALUES (?, ?, ?, ?, ?)
            ''', (clinic_name, location, phone_number, password, "Pending"))

            conn.commit()
            QtWidgets.QMessageBox.information(self.current_window, "Success", "Registration successful")
            self.openClinicLoginRegisterbuttons()

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self.current_window, "Error", f"Database error: {e}")

        finally:
            conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    clinicRegister = QtWidgets.QWidget()
    ui = Ui_clinicRegister()
    ui.setupUi(clinicRegister)
    clinicRegister.show()
    sys.exit(app.exec())
