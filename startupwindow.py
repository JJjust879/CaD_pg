from PyQt6 import QtCore, QtGui, QtWidgets
import adminlogin
import PatientLoginRegisterbuttons
import ClinicLoginRegisterbuttons
import doctorlogin
import database
db=database

class Ui_StartupWindow(object):
    def setupUi(self, StartupWindow):
        StartupWindow.setObjectName("StartupWindow")
        StartupWindow.resize(800, 500)
        StartupWindow.setMinimumSize(QtCore.QSize(800, 500))
        StartupWindow.setMaximumSize(QtCore.QSize(800, 500))
        StartupWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        StartupWindow.setWindowTitle("Call A Doctor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=StartupWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.CadPic1 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.CadPic1.setMinimumSize(QtCore.QSize(400, 400))
        self.CadPic1.setMaximumSize(QtCore.QSize(400, 400))
        self.CadPic1.setText("")
        self.CadPic1.setPixmap(QtGui.QPixmap("MainPic.jpg"))
        self.CadPic1.setScaledContents(True)
        self.CadPic1.setObjectName("CadPic1")
        self.horizontalLayout_2.addWidget(self.CadPic1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem3, 4, 1, 1, 1)
        self.AdminButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdminButton.sizePolicy().hasHeightForWidth())
        self.AdminButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AdminButton.setFont(font)
        self.AdminButton.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.AdminButton.setObjectName("AdminButton")
        self.gridLayout_2.addWidget(self.AdminButton, 7, 1, 1, 1)
        self.PatientButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PatientButton.sizePolicy().hasHeightForWidth())
        self.PatientButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PatientButton.setFont(font)
        self.PatientButton.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.PatientButton.setObjectName("PatientButton")
        self.gridLayout_2.addWidget(self.PatientButton, 1, 1, 1, 1)
        self.ClinicButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClinicButton.sizePolicy().hasHeightForWidth())
        self.ClinicButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ClinicButton.setFont(font)
        self.ClinicButton.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.ClinicButton.setObjectName("ClinicButton")
        self.gridLayout_2.addWidget(self.ClinicButton, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        self.DoctorButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DoctorButton.sizePolicy().hasHeightForWidth())
        self.DoctorButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DoctorButton.setFont(font)
        self.DoctorButton.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"}")
        self.DoctorButton.setObjectName("DoctorButton")
        self.gridLayout_2.addWidget(self.DoctorButton, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem6, 6, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem7, 8, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(spacerItem8, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.retranslateUi(StartupWindow)
        QtCore.QMetaObject.connectSlotsByName(StartupWindow)

        # Connect buttons to the respective methods
        self.AdminButton.clicked.connect(self.openAdminWindow)
        self.PatientButton.clicked.connect(self.openPatientWindow)
        self.ClinicButton.clicked.connect(self.openClinicWindow)
        self.DoctorButton.clicked.connect(self.openDoctorWindow)

        self.current_window = StartupWindow

    def retranslateUi(self, StartupWindow):
        _translate = QtCore.QCoreApplication.translate
        self.AdminButton.setText(_translate("StartupWindow", "Admin"))
        self.PatientButton.setText(_translate("StartupWindow", "Patient"))
        self.ClinicButton.setText(_translate("StartupWindow", "Clinic"))
        self.DoctorButton.setText(_translate("StartupWindow", "Doctor"))

    def openAdminWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = adminlogin.Ui_AdminLogin()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def openPatientWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = PatientLoginRegisterbuttons.Ui_PatientLoginRegisterbuttons()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def openClinicWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = ClinicLoginRegisterbuttons.Ui_ClinicLoginRegisterbuttons()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

    def openDoctorWindow(self):
        self.new_window = QtWidgets.QWidget()
        self.ui = doctorlogin.Ui_DoctorLogin()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        self.current_window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartupWindow = QtWidgets.QWidget()
    ui = Ui_StartupWindow()
    ui.setupUi(StartupWindow)
    StartupWindow.show()
    sys.exit(app.exec())
