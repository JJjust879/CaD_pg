from PyQt6 import QtCore, QtGui, QtWidgets
import startupwindow
import Doctor
import sqlite3


class Ui_DoctorLogin(object):
    def setupUi(self, DoctorLogin):
        DoctorLogin.setObjectName("DoctorLogin")
        DoctorLogin.resize(800, 500)
        DoctorLogin.setMinimumSize(QtCore.QSize(800, 500))
        DoctorLogin.setMaximumSize(QtCore.QSize(800, 500))
        DoctorLogin.setWindowTitle("Call A Doctor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=DoctorLogin)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.doctorPic = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.doctorPic.setMinimumSize(QtCore.QSize(300, 300))
        self.doctorPic.setMaximumSize(QtCore.QSize(300, 300))
        self.doctorPic.setText("")
        self.doctorPic.setPixmap(QtGui.QPixmap("doctor.jpg"))
        self.doctorPic.setScaledContents(True)
        self.doctorPic.setObjectName("doctorPic")
        self.horizontalLayout_2.addWidget(self.doctorPic)
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
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Set initial EchoMode to Password
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

        self.retranslateUi(DoctorLogin)
        QtCore.QMetaObject.connectSlotsByName(DoctorLogin)

        # Connect checkbox state change to toggle_password_visibility method
        self.checkBox.stateChanged.connect(self.toggle_password_visibility)

        # Connect the Back button to the openStartupWindow method
        self.Back.clicked.connect(self.openStartupWindow)
        self.Login.clicked.connect(self.login)  # Connect the Login button to the login method

        self.current_window = DoctorLogin  # Set the current window attribute

    def retranslateUi(self, DoctorLogin):
        _translate = QtCore.QCoreApplication.translate
        self.Login.setText(_translate("DoctorLogin", "Login"))
        self.Password.setText(_translate("DoctorLogin", "Password:"))
        self.Username.setText(_translate("DoctorLogin", "Username:"))
        self.Back.setText(_translate("DoctorLogin", "Back"))
        self.checkBox.setText(_translate("DoctorLogin", "Show Password"))

    def toggle_password_visibility(self):
        if self.checkBox.isChecked():
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def openStartupWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = startupwindow.Ui_StartupWindow()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Connect to the database
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()

        # Check if the username and password are correct
        cursor.execute("SELECT * FROM Doctor WHERE Doctor_Name=? AND Doctor_ID=?", (username, password))
        result = cursor.fetchone()

        if result:
            QtWidgets.QMessageBox.information(self.current_window, "Login Successful", "You have successfully logged in.")
            # Proceed to the Doctor's dashboard or main window
            self.openDoctorDashboard()
        else:
            QtWidgets.QMessageBox.warning(self.current_window, "Login Failed", "Invalid username or password.")

        # Close the database connection
        conn.close()

    def openDoctorDashboard(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = Doctor.Ui_Form()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DoctorLogin = QtWidgets.QWidget()
    ui = Ui_DoctorLogin()
    ui.setupUi(DoctorLogin)
    DoctorLogin.show()
    sys.exit(app.exec())
