from PyQt6 import QtCore, QtGui, QtWidgets
import startupwindow, cliniclogin, clinicregister

class Ui_ClinicLoginRegisterbuttons(object):
    def setupUi(self, ClinicLoginRegisterbuttons):
        ClinicLoginRegisterbuttons.setObjectName("ClinicLoginRegisterbuttons")
        ClinicLoginRegisterbuttons.resize(800, 500)
        ClinicLoginRegisterbuttons.setMinimumSize(QtCore.QSize(800, 500))
        ClinicLoginRegisterbuttons.setMaximumSize(QtCore.QSize(800, 500))
        ClinicLoginRegisterbuttons.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        ClinicLoginRegisterbuttons.setWindowTitle("Call A Doctor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=ClinicLoginRegisterbuttons)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clinicPic = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.clinicPic.setMinimumSize(QtCore.QSize(450, 450))
        self.clinicPic.setMaximumSize(QtCore.QSize(450, 450))
        self.clinicPic.setText("")
        self.clinicPic.setPixmap(QtGui.QPixmap("clinic.jpg"))
        self.clinicPic.setScaledContents(True)
        self.clinicPic.setObjectName("clinicPic")
        self.horizontalLayout_2.addWidget(self.clinicPic)
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

        self.retranslateUi(ClinicLoginRegisterbuttons)
        QtCore.QMetaObject.connectSlotsByName(ClinicLoginRegisterbuttons)

        # Connect the Back button to the method
        self.Back.clicked.connect(self.openStartupWindow)  # Connect Back button click event
        self.Login.clicked.connect(self.openLoginWindow)
        self.Register.clicked.connect(self.openRegisterindow)
        self.current_window = ClinicLoginRegisterbuttons  # Set the current window attribute

    def retranslateUi(self, ClinicLoginRegisterbuttons):
        _translate = QtCore.QCoreApplication.translate
        self.Register.setText(_translate("ClinicLoginRegisterbuttons", "Register"))
        self.Login.setText(_translate("ClinicLoginRegisterbuttons", "Login"))
        self.Back.setText(_translate("ClinicLoginRegisterbuttons", "Back"))

    def openStartupWindow(self):  # Define the method to open the StartupWindow
        self.new_window = QtWidgets.QWidget()
        self.ui = startupwindow.Ui_StartupWindow()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def openLoginWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = cliniclogin.Ui_ClinicLogin()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def openRegisterindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = clinicregister.Ui_clinicRegister()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicLoginRegisterbuttons = QtWidgets.QWidget()
    ui = Ui_ClinicLoginRegisterbuttons()
    ui.setupUi(ClinicLoginRegisterbuttons)
    ClinicLoginRegisterbuttons.show()
    sys.exit(app.exec())
