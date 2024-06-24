from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(800, 500)
        Admin.setMinimumSize(QtCore.QSize(800, 500))
        Admin.setMaximumSize(QtCore.QSize(800, 500))
        Admin.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        Admin.setWindowTitle("Call A Doctor")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Admin)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 502))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 400))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 50)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 200)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 350)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.setColumnWidth(4, 70)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Back = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Back.setObjectName("Back")
        self.horizontalLayout.addWidget(self.Back)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Update = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Update.setObjectName("Update")
        self.horizontalLayout.addWidget(self.Update)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

        # Connect the buttons to their functions
        self.Back.clicked.connect(self.openStartupWindow)
        self.Update.clicked.connect(self.updateApprovalStatus)

        # Load clinic data into the table
        self.loadClinicData()

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Admin", "Clinic ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Admin", "Clinic Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Admin", "Clinic Location"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Admin", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Admin", "Approval"))
        self.Back.setText(_translate("Admin", "Back"))
        self.Update.setText(_translate("Admin", "Update"))

    def loadClinicData(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Clinic_ID, Clinic_Name, Clinic_Location, Clinic_Approval FROM Clinic")
        clinics = cursor.fetchall()
        self.tableWidget.setRowCount(len(clinics))
        for row_num, clinic in enumerate(clinics):
            for col_num, data in enumerate(clinic):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center align the text
                self.tableWidget.setItem(row_num, col_num, item)
            # Add checkbox for approval status
            status_checkbox = QtWidgets.QCheckBox()
            status_checkbox.setChecked(clinic[3] == "Approved")
            self.tableWidget.setCellWidget(row_num, 4, self.centerWidget(status_checkbox))
        conn.close()

    def centerWidget(self, widget):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(widget, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        container = QtWidgets.QWidget()
        container.setLayout(layout)
        return container

    def updateApprovalStatus(self):
        conn = sqlite3.connect('CallADoctor.db')
        cursor = conn.cursor()
        for row in range(self.tableWidget.rowCount()):
            clinic_id = self.tableWidget.item(row, 0).text()
            approval_status = self.tableWidget.cellWidget(row, 4).findChild(QtWidgets.QCheckBox).isChecked()
            approval_text = "Approved" if approval_status else "Pending"
            cursor.execute("UPDATE Clinic SET Clinic_Approval = ? WHERE Clinic_ID = ?", (approval_text, clinic_id))
        conn.commit()
        conn.close()
        self.loadClinicData()  # Reload data to reflect updates

    def openStartupWindow(self):
        from startupwindow import Ui_StartupWindow  # Assuming this is the correct import
        self.new_window = QtWidgets.QWidget()
        self.ui = Ui_StartupWindow()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()  # Close current window


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec())
