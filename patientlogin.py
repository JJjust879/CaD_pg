from PyQt6 import QtCore, QtGui, QtWidgets
import PatientLoginRegisterbuttons
import sqlite3
import sys
import subprocess

class Ui_PatientLogin(object):
    def setupUi(self, PatientLogin):
        PatientLogin.setObjectName("PatientLogin")
        PatientLogin.resize(800, 500)
        PatientLogin.setMinimumSize(QtCore.QSize(800, 500))
        PatientLogin.setMaximumSize(QtCore.QSize(800, 500))
        PatientLogin.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        PatientLogin.setWindowTitle("Call A Doctor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=PatientLogin)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.patientPic = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.patientPic.setMinimumSize(QtCore.QSize(300, 300))
        self.patientPic.setMaximumSize(QtCore.QSize(300, 300))
        self.patientPic.setText("")
        self.patientPic.setPixmap(QtGui.QPixmap("patientPic.png"))
        self.patientPic.setScaledContents(True)
        self.patientPic.setObjectName("patientPic")
        self.horizontalLayout_2.addWidget(self.patientPic)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.gridLayout_2.addWidget(self.Login, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.Password = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.gridLayout_2.addWidget(self.Password, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 5, 0, 1, 1)
        self.Username = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.gridLayout_2.addWidget(self.Username, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
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
        self.gridLayout_2.addWidget(self.Back, 4, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 3, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)

        self.retranslateUi(PatientLogin)
        QtCore.QMetaObject.connectSlotsByName(PatientLogin)

        # Connect the Back button to the openPatientLoginRegisterbuttons method
        self.Back.clicked.connect(self.openPatientLoginRegisterbuttons)
        self.current_window = PatientLogin  # Set the current window attribute

        # Connect the checkbox state change signal to the handler
        self.checkBox.stateChanged.connect(self.toggle_password_visibility)

        # Connect the Login button to the login_patient method
        self.Login.clicked.connect(self.login_patient)

    def retranslateUi(self, PatientLogin):
        _translate = QtCore.QCoreApplication.translate
        self.Login.setText(_translate("PatientLogin", "Login"))
        self.Password.setText(_translate("PatientLogin", "Password:"))
        self.Username.setText(_translate("PatientLogin", "Email:"))
        self.Back.setText(_translate("PatientLogin", "Back"))
        self.checkBox.setText(_translate("PatientLogin", "Show Password"))

    def toggle_password_visibility(self, state):
        if state == QtCore.Qt.CheckState.Checked.value:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def openPatientLoginRegisterbuttons(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = PatientLoginRegisterbuttons.Ui_PatientLoginRegisterbuttons()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def login_patient(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                SELECT Patient_ID FROM Patient 
                WHERE Patient_Email = ? AND Patient_Password = ?
            ''', (email, password))
            patient = cursor.fetchone()

            if patient:
                self.patient_id = patient[0]
                QtWidgets.QMessageBox.information(self.current_window, "Success", "Login successful")
                self.open_appointv1()
            else:
                QtWidgets.QMessageBox.warning(self.current_window, "Error", "Invalid email or password")

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self.current_window, "Error", f"Database error: {e}")

        finally:
            conn.close()
        
    def open_appointv1(self):
        try:
            print("Launching Appoint_v1.py with patient ID:", self.patient_id)
            subprocess.Popen([sys.executable, "Appoint_v1.py", str(self.patient_id)])
            self.current_window.close()
        except Exception as e:
            print("Failed to launch Appoint_v1.py:", e)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatientLogin = QtWidgets.QWidget()
    ui = Ui_PatientLogin()
    ui.setupUi(PatientLogin)
    PatientLogin.show()
    sys.exit(app.exec())
