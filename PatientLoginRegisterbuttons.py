from PyQt6 import QtCore, QtGui, QtWidgets
import startupwindow, patientlogin, patientregister

class Ui_PatientLoginRegisterbuttons(object):
    def setupUi(self, PatientLoginRegisterbuttons):
        PatientLoginRegisterbuttons.setObjectName("PatientLoginRegisterbuttons")
        PatientLoginRegisterbuttons.resize(800, 500)
        PatientLoginRegisterbuttons.setMinimumSize(QtCore.QSize(800, 500))
        PatientLoginRegisterbuttons.setMaximumSize(QtCore.QSize(800, 500))
        PatientLoginRegisterbuttons.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        PatientLoginRegisterbuttons.setWindowTitle("Call A Doctor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=PatientLoginRegisterbuttons)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.patientPic = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.patientPic.setMinimumSize(QtCore.QSize(450, 450))
        self.patientPic.setMaximumSize(QtCore.QSize(450, 450))
        self.patientPic.setText("")
        self.patientPic.setPixmap(QtGui.QPixmap("patientPic.png"))
        self.patientPic.setScaledContents(True)
        self.patientPic.setObjectName("patientPic")
        self.horizontalLayout_2.addWidget(self.patientPic)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Register = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Register.sizePolicy().hasHeightForWidth())
        self.Register.setSizePolicy(sizePolicy)
        self.Register.setMinimumSize(QtCore.QSize(250, 100))
        self.Register.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Register.setFont(font)
        self.Register.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.Register.setObjectName("Register")
        self.gridLayout_2.addWidget(self.Register, 1, 0, 1, 1)
        self.Login = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy)
        self.Login.setMinimumSize(QtCore.QSize(250, 100))
        self.Login.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Login.setFont(font)
        self.Login.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.Login.setObjectName("Login")
        self.gridLayout_2.addWidget(self.Login, 0, 0, 1, 1)
        self.Back = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Back.sizePolicy().hasHeightForWidth())
        self.Back.setSizePolicy(sizePolicy)
        self.Back.setMinimumSize(QtCore.QSize(250, 100))
        self.Back.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Back.setFont(font)
        self.Back.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.Back.setObjectName("Back")
        self.gridLayout_2.addWidget(self.Back, 2, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.retranslateUi(PatientLoginRegisterbuttons)
        QtCore.QMetaObject.connectSlotsByName(PatientLoginRegisterbuttons)

        # Connect the Back button to the openStartupWindow method
        self.Back.clicked.connect(self.openStartupWindow)
        self.Login.clicked.connect(self.openLoginWindow)
        self.Register.clicked.connect(self.openRegisterindow)
        self.current_window = PatientLoginRegisterbuttons  # Set the current window attribute

    def retranslateUi(self, PatientLoginRegisterbuttons):
        _translate = QtCore.QCoreApplication.translate
        self.Register.setText(_translate("PatientLoginRegisterbuttons", "Register"))
        self.Login.setText(_translate("PatientLoginRegisterbuttons", "Login"))
        self.Back.setText(_translate("PatientLoginRegisterbuttons", "Back"))

    def openStartupWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = startupwindow.Ui_StartupWindow()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def openLoginWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = patientlogin.Ui_PatientLogin()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def openRegisterindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = patientregister.Ui_patientRegister()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatientLoginRegisterbuttons = QtWidgets.QWidget()
    ui = Ui_PatientLoginRegisterbuttons()
    ui.setupUi(PatientLoginRegisterbuttons)
    PatientLoginRegisterbuttons.show()
    sys.exit(app.exec())
