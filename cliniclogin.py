import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
import subprocess
import ClinicLoginRegisterbuttons

class Ui_ClinicLogin(object):
    def setupUi(self, ClinicLogin):
        ClinicLogin.setObjectName("ClinicLogin")
        ClinicLogin.resize(800, 500)
        ClinicLogin.setMinimumSize(QtCore.QSize(800, 500))
        ClinicLogin.setMaximumSize(QtCore.QSize(800, 500))
        ClinicLogin.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        ClinicLogin.setWindowTitle("Call A Doctor")

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=ClinicLogin)
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
        self.clinicPic.setPixmap(QtGui.QPixmap("clinic.jpg"))
        self.clinicPic.setScaledContents(True)
        self.clinicPic.setObjectName("clinicPic")

        self.horizontalLayout_2.addWidget(self.clinicPic)
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
        self.passwordLineInput = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.passwordLineInput.setMinimumSize(QtCore.QSize(0, 40))
        self.passwordLineInput.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLineInput.setFont(font)
        self.passwordLineInput.setObjectName("passwordLineInput")
        self.passwordLineInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.gridLayout_2.addWidget(self.passwordLineInput, 3, 1, 1, 1)
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
        self.Username.setObjectName("Clinicname")
        self.gridLayout_2.addWidget(self.Username, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        self.ClinicNameInput = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.ClinicNameInput.setMinimumSize(QtCore.QSize(0, 40))
        self.ClinicNameInput.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClinicNameInput.setFont(font)
        self.ClinicNameInput.setText("")
        self.ClinicNameInput.setObjectName("ClinicNameInput")
        self.gridLayout_2.addWidget(self.ClinicNameInput, 1, 1, 1, 1)
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

        self.retranslateUi(ClinicLogin)
        QtCore.QMetaObject.connectSlotsByName(ClinicLogin)

        # Connect the checkbox state change signal to the handler
        self.checkBox.stateChanged.connect(self.toggle_password_visibility)

        self.Back.clicked.connect(self.openClinicLoginRegisterbuttons)
        
        self.current_window = ClinicLogin  # Set the current window attribute

        self.Login.clicked.connect(self.login_clinic)

    def retranslateUi(self, ClinicLogin):
        _translate = QtCore.QCoreApplication.translate
        self.Login.setText(_translate("ClinicLogin", "Login"))
        self.Password.setText(_translate("ClinicLogin", "Password:"))
        self.Username.setText(_translate("ClinicLogin", "Clinic name:"))
        self.Back.setText(_translate("ClinicLogin", "Back"))
        self.checkBox.setText(_translate("ClinicLogin", "Show Password"))

    def toggle_password_visibility(self, state):
        if state == QtCore.Qt.CheckState.Checked.value:
            self.passwordLineInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.passwordLineInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def openClinicLoginRegisterbuttons(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = ClinicLoginRegisterbuttons.Ui_ClinicLoginRegisterbuttons()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def login_clinic(self):
        clinic_name = self.ClinicNameInput.text()
        password = self.passwordLineInput.text()

        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                SELECT * FROM Clinic 
                WHERE Clinic_Name = ? AND Clinic_Approval = ?
            ''', (clinic_name, "Approved"))
            clinic = cursor.fetchone()

            if clinic and clinic[4] == password:  # Check the password (assuming Clinic_Password is the 4th column)
                QtWidgets.QMessageBox.information(self.current_window, "Success", "Login successful")
                print("Login successful, clinic ID:", clinic[0])  # Debug message
                self.openClinicDashboard(clinic[0])  # Pass clinic ID to the dashboard
            else:
                QtWidgets.QMessageBox.warning(self.current_window, "Error", "Invalid credentials or clinic not approved")

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self.current_window, "Error", f"Database error: {e}")

        finally:
            conn.close()

    def openClinicDashboard(self, clinic_id):
        subprocess.Popen([sys.executable, 'clinic_dashboard.py', str(clinic_id)])
        self.current_window.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ClinicLogin = QtWidgets.QWidget()
    ui = Ui_ClinicLogin()
    ui.setupUi(ClinicLogin)
    ClinicLogin.show()
    sys.exit(app.exec())
