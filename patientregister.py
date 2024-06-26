from PyQt6 import QtCore, QtGui, QtWidgets
import PatientLoginRegisterbuttons
import sqlite3

class Ui_patientRegister(object):
    def setupUi(self, patientRegister):
        patientRegister.setObjectName("patientRegister")
        patientRegister.resize(800, 500)
        patientRegister.setMinimumSize(QtCore.QSize(800, 500))
        patientRegister.setMaximumSize(QtCore.QSize(800, 500))
        patientRegister.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        patientRegister.setWindowTitle("Call A Doctor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=patientRegister)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clinicPic = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.clinicPic.setMinimumSize(QtCore.QSize(300, 300))
        self.clinicPic.setMaximumSize(QtCore.QSize(300, 300))
        self.clinicPic.setText("")
        self.clinicPic.setPixmap(QtGui.QPixmap("patientPic.png"))
        self.clinicPic.setScaledContents(True)
        self.clinicPic.setObjectName("clinicPic")
        self.horizontalLayout_2.addWidget(self.clinicPic)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.adressline = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adressline.sizePolicy().hasHeightForWidth())
        self.adressline.setSizePolicy(sizePolicy)
        self.adressline.setMinimumSize(QtCore.QSize(0, 30))
        self.adressline.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.adressline.setFont(font)
        self.adressline.setText("")
        self.adressline.setObjectName("adressline")
        self.gridLayout_2.addWidget(self.adressline, 7, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 8, 0, 1, 1)
        self.emailline = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.emailline.setMinimumSize(QtCore.QSize(0, 30))
        self.emailline.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emailline.setFont(font)
        self.emailline.setText("")
        self.emailline.setObjectName("emailline")
        self.gridLayout_2.addWidget(self.emailline, 11, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 15, 0, 1, 1)
        self.Sex = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sex.setFont(font)
        self.Sex.setObjectName("Sex")
        self.gridLayout_2.addWidget(self.Sex, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 17, 0, 1, 1)
        self.Login = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy)
        self.Login.setMinimumSize(QtCore.QSize(125, 50))
        self.Login.setMaximumSize(QtCore.QSize(125, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Login.setFont(font)
        self.Login.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.Login.setObjectName("Login")
        self.gridLayout_2.addWidget(self.Login, 18, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 6, 0, 1, 1)
        self.confirmpasswordline = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.confirmpasswordline.setMinimumSize(QtCore.QSize(0, 30))
        self.confirmpasswordline.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confirmpasswordline.setFont(font)
        self.confirmpasswordline.setObjectName("confirmpasswordline")
        self.confirmpasswordline.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.gridLayout_2.addWidget(self.confirmpasswordline, 16, 1, 1, 1)
        self.Password_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password_2.setFont(font)
        self.Password_2.setObjectName("Password_2")
        self.gridLayout_2.addWidget(self.Password_2, 16, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem6, 0, 0, 1, 1)
        self.Sex_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sex_2.setFont(font)
        self.Sex_2.setObjectName("Sex_2")
        self.gridLayout_2.addWidget(self.Sex_2, 11, 0, 1, 1)
        self.passwordline = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.passwordline.setMinimumSize(QtCore.QSize(0, 30))
        self.passwordline.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordline.setFont(font)
        self.passwordline.setObjectName("passwordline")
        self.passwordline.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.gridLayout_2.addWidget(self.passwordline, 14, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem7, 10, 0, 1, 1)
        self.Password = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.gridLayout_2.addWidget(self.Password, 14, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 5, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem8, 19, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem9, 4, 0, 1, 1)
        self.Name = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.gridLayout_2.addWidget(self.Name, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem10, 2, 0, 1, 1)
        self.Age = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Age.setFont(font)
        self.Age.setObjectName("Age")
        self.gridLayout_2.addWidget(self.Age, 3, 0, 1, 1)
        self.Sex_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sex_4.setFont(font)
        self.Sex_4.setObjectName("Sex_4")
        self.gridLayout_2.addWidget(self.Sex_4, 9, 0, 1, 1)
        self.Sex_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sex_3.setFont(font)
        self.Sex_3.setObjectName("Sex_3")
        self.gridLayout_2.addWidget(self.Sex_3, 7, 0, 1, 1)
        self.phonnumberline = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.phonnumberline.setMinimumSize(QtCore.QSize(0, 30))
        self.phonnumberline.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.phonnumberline.setFont(font)
        self.phonnumberline.setText("")
        self.phonnumberline.setObjectName("phonnumberline")
        self.gridLayout_2.addWidget(self.phonnumberline, 9, 1, 1, 1)
        self.nameline = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.nameline.setMinimumSize(QtCore.QSize(0, 30))
        self.nameline.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameline.setFont(font)
        self.nameline.setText("")
        self.nameline.setObjectName("nameline")
        self.gridLayout_2.addWidget(self.nameline, 1, 1, 1, 1)
        self.age = QtWidgets.QSpinBox(parent=self.horizontalLayoutWidget)
        self.age.setMinimumSize(QtCore.QSize(0, 30))
        self.age.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.age.setFont(font)
        self.age.setMaximum(200)
        self.age.setObjectName("age")
        self.gridLayout_2.addWidget(self.age, 3, 1, 1, 1)
        self.Back = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Back.sizePolicy().hasHeightForWidth())
        self.Back.setSizePolicy(sizePolicy)
        self.Back.setMinimumSize(QtCore.QSize(125, 50))
        self.Back.setMaximumSize(QtCore.QSize(125, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Back.setFont(font)
        self.Back.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.Back.setObjectName("Back")
        self.gridLayout_2.addWidget(self.Back, 18, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 14, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem11, 13, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.phonnumberline.setValidator(QtGui.QIntValidator()) 

        self.retranslateUi(patientRegister)
        QtCore.QMetaObject.connectSlotsByName(patientRegister)
        self.checkBox.stateChanged.connect(self.toggle_password_visibility)

        # Connect the Back button to the openPatientLoginRegisterbuttons method
        self.Back.clicked.connect(self.openPatientLoginRegisterbuttons)
        self.current_window = patientRegister  # Set the current window attribute

        # Connect the Register button to the register_patient method
        self.Login.clicked.connect(self.register_patient)

    def retranslateUi(self, patientRegister):
        _translate = QtCore.QCoreApplication.translate
        self.Sex.setText(_translate("patientRegister", "Sex:"))
        self.Login.setText(_translate("patientRegister", "Register"))
        self.Password_2.setText(_translate("patientRegister", "Confirm Password:"))
        self.Sex_2.setText(_translate("patientRegister", "Email:"))
        self.Password.setText(_translate("patientRegister", "Password:"))
        self.comboBox.setItemText(0, _translate("patientRegister", "Male"))
        self.comboBox.setItemText(1, _translate("patientRegister", "Female"))
        self.Name.setText(_translate("patientRegister", "Name:"))
        self.Age.setText(_translate("patientRegister", "Age:"))
        self.Sex_4.setText(_translate("patientRegister", "Phone Number:"))
        self.Sex_3.setText(_translate("patientRegister", "Address:"))
        self.Back.setText(_translate("patientRegister", "Back"))
        self.checkBox.setText(_translate("patientRegister", "Show Password"))
    
    def toggle_password_visibility(self):
        if self.checkBox.isChecked():
            self.passwordline.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.confirmpasswordline.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.passwordline.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.confirmpasswordline.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def openPatientLoginRegisterbuttons(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = PatientLoginRegisterbuttons.Ui_PatientLoginRegisterbuttons()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def register_patient(self):
        name = self.nameline.text()
        age = self.age.value()
        sex = self.comboBox.currentText()
        address = self.adressline.text()
        phone = self.phonnumberline.text()
        email = self.emailline.text()
        password = self.passwordline.text()
        confirm_password = self.confirmpasswordline.text()

        if not all([name, address, phone, email, password, confirm_password]):
            QtWidgets.QMessageBox.warning(self.current_window, "Error", "All fields must be filled")
            return

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self.current_window, "Error", "Passwords do not match")
            return

        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO Patient (Patient_Name, Patient_Age, Patient_Sex, Patient_Address, Patient_PhoneNo, Patient_Email, Patient_Password)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, age, sex, address, phone, email, password))

            conn.commit()
            QtWidgets.QMessageBox.information(self.current_window, "Success", "Registration successful")
            self.openPatientLoginRegisterbuttons()

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self.current_window, "Error", f"Database error: {e}")

        finally:
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patientRegister = QtWidgets.QWidget()
    ui = Ui_patientRegister()
    ui.setupUi(patientRegister)
    patientRegister.show()
    sys.exit(app.exec())
