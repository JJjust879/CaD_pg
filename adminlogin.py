from PyQt6 import QtCore, QtGui, QtWidgets
import startupwindow
import admin


class Ui_AdminLogin(object):
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
        self.mainPic = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.mainPic.setMinimumSize(QtCore.QSize(300, 300))
        self.mainPic.setMaximumSize(QtCore.QSize(300, 300))
        self.mainPic.setText("")
        self.mainPic.setPixmap(QtGui.QPixmap("MainPic.jpg"))
        self.mainPic.setScaledContents(True)
        self.mainPic.setObjectName("mainPic")
        self.horizontalLayout_2.addWidget(self.mainPic)
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
        self.gridLayout_2.addWidget(self.Login, 3, 2, 1, 1)
        
        self.confirmpasswordline = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.confirmpasswordline.setMinimumSize(QtCore.QSize(0, 30))
        self.confirmpasswordline.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confirmpasswordline.setFont(font)
        self.confirmpasswordline.setObjectName("confirmpasswordline")
        self.confirmpasswordline.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Hide the password
        self.gridLayout_2.addWidget(self.confirmpasswordline, 2, 1, 1, 1)
        
        self.Password_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password_2.setFont(font)
        self.Password_2.setObjectName("Password_2")
        self.gridLayout_2.addWidget(self.Password_2, 2, 0, 1, 1)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout_2.addItem(spacerItem3, 4, 0, 1, 1)
        
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
        self.Back.clicked.connect(self.openStartupWindow)
        self.gridLayout_2.addWidget(self.Back, 3, 0, 1, 1)
        
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.retranslateUi(patientRegister)
        QtCore.QMetaObject.connectSlotsByName(patientRegister)

        self.current_window = patientRegister  # Set the current window attribute

        self.Login.clicked.connect(self.login_admin)  # Connect the login button to the login method

    def retranslateUi(self, patientRegister):
        _translate = QtCore.QCoreApplication.translate
        self.Login.setText(_translate("patientRegister", "Login"))
        self.Password_2.setText(_translate("patientRegister", "Password:"))
        self.Back.setText(_translate("patientRegister", "Back"))

    def openStartupWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = startupwindow.Ui_StartupWindow()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def login_admin(self):
        password = self.confirmpasswordline.text()
        if password == "admin":
            self.new_window = QtWidgets.QWidget()
            self.ui = admin.Ui_Admin()  # Initialize your admin window class
            self.ui.setupUi(self.new_window)
            self.new_window.show()
            self.current_window.close()
        else:
            QtWidgets.QMessageBox.warning(self.current_window, "Error", "Incorrect password")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patientRegister = QtWidgets.QWidget()
    ui = Ui_AdminLogin()
    ui.setupUi(patientRegister)
    patientRegister.show()
    sys.exit(app.exec())
