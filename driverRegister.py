# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driverRegister.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import adminServices

#conn = sqlite3.connect(':memory:')  # testing in memory
conn = sqlite3.connect('taxi.db')   # creates the actual database
c = conn.cursor()     # The cursor to take data to and from the database.
c.execute("""CREATE TABLE if not exists Driver (
                   driverId INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name text,
                   last_name text,
                   email text,
                   password text,
                   address text,
                   telephone_no text,
                   license_plate text
                   )""")   # creates the table associated with the text field aka line edits

class Ui_driverRegisterScreen_Dialog(object):

        def __init__(self, Dialog):    # creation of a constructor
                self.Dialog = QtWidgets.QDialog()   # this class has one attribute
                self.driverRegisterScreen_setupUi(self.Dialog)   # attribute is need to setup the ui

        def its_showtime(self):    # used to show the dialog
                self.Dialog.show()

        def its_closetime(self):    # used to close the dialog
                self.Dialog.close()

        def back_button_click(self):
                self.dialog = QtWidgets.QDialog()    # goes back to the Admin Services Screen
                aS = adminServices.Ui_adminPortal_Dialog(self.dialog)
                aS.its_showtime()
                self.its_closetime()

        def registerAsDriver_button_click(self):
                self.insert_record()   # inserts the user data
                conn.commit()   # commits the data to the database
                conn.close()   # closes the database connection
                self.disable_fields_and_Buttons()   # function that disables fields and button.
                self.showdialog("Congratulations, you have successfully been registered!")

        def insert_record(self):
                with conn:
                        c.execute(
                                "INSERT INTO Driver VALUES (NULL, :first_name, :last_name, :email, :password, "
                                ":address, :telephone_no, :license_plate)",

                                {'driverId': self.dDriverIDLineEdit.text(),
                                 'first_name': self.dFirstNameLineEdit.text(),
                                 'last_name': self.dLastNameLineEdit.text(),
                                 'email': self.dEmailLineEdit.text(),
                                 'password': self.dPasswordLineEdit.text(),
                                 'address': self.dAddressLineEdit.text(),
                                 'telephone_no': self.dTelephoneNoLineEdit.text(),
                                 'license_plate': self.dLicencePlateLineEdit.text()})

        def disable_fields_and_Buttons(self):
                self.dFirstNameLineEdit.setEnabled(False)     # disable the firstName field
                self.dLastNameLineEdit.setEnabled(False)      # disable the LastName field
                self.dEmailLineEdit.setEnabled(False)         # disable the email field
                self.dPasswordLineEdit.setEnabled(False)      # disable the password field
                self.dAddressLineEdit.setEnabled(False)       # disable the address field
                self.dTelephoneNoLineEdit.setEnabled(False)   # disable the telephoneNo field
                self.dLicencePlateLineEdit.setEnabled(False)  # disable the LicencePlate field
                self.registerAsDriverBtn.setEnabled(False)    # disable the registerAsDriverBtn

        def showdialog(self, message):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("This is a confirmation message.")
                msg.setInformativeText(message)
                msg.setWindowTitle("Confirmation")
                msg.setDetailedText("The details are as follows:" + message)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()

        def driverRegisterScreen_setupUi(self, driverRegisterScreen_Dialog):
                driverRegisterScreen_Dialog.setObjectName("driverRegisterScreen_Dialog")
                driverRegisterScreen_Dialog.resize(671, 460)
                self.driverRegisterScreen = QtWidgets.QWidget(driverRegisterScreen_Dialog)
                self.driverRegisterScreen.setGeometry(QtCore.QRect(10, 10, 651, 441))
                self.driverRegisterScreen.setStyleSheet("border: 8px solid black;\n"
        "background-color:qlineargradient(spread:pad, x1:0.0511364, y1:1, x2:0, y2:0, stop:0 rgba(251, 255, 0, 255),"
        " stop:0.98 rgba(0, 61, 255, 255), stop:1 rgba(0, 0, 0, 0));\n""")
                self.driverRegisterScreen.setObjectName("driverRegisterScreen")
                self.register_txt = QtWidgets.QLabel(self.driverRegisterScreen)
                self.register_txt.setGeometry(QtCore.QRect(190, 20, 291, 21))
                self.register_txt.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 24px;\n"
        "border: none;\n"
        "background-color: none;\n"
        "color: yellow;\n"
        "")
                self.register_txt.setObjectName("register_txt")
                self.backBtn = QtWidgets.QPushButton(self.driverRegisterScreen,
                                                           clicked=lambda: self.back_button_click())
                self.backBtn.setGeometry(QtCore.QRect(530, 390, 91, 31))
                self.backBtn.setStyleSheet("background: red;\n"
        "border: 3px solid blue;\n"
        "box-sizing: border-box;\n"
        "border-radius: 15px;\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: white;")
                self.backBtn.setObjectName("backBtn")
                self.registerAsDriverBtn = QtWidgets.QPushButton(self.driverRegisterScreen,
                                                           clicked=lambda: self.registerAsDriver_button_click())
                self.registerAsDriverBtn.setGeometry(QtCore.QRect(250, 310, 161, 31))
                self.registerAsDriverBtn.setStyleSheet("background: blue;\n"
        "border: 2px solid rgb(255, 0, 127);\n"
        "box-sizing: border-box;\n"
        "border-radius: 10px;\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: white;")
                self.registerAsDriverBtn.setObjectName("registerAsDriverBtn")
                self.label = QtWidgets.QLabel(self.driverRegisterScreen)
                self.label.setGeometry(QtCore.QRect(0, 0, 651, 61))
                self.label.setStyleSheet("background-color: black;\n"
        "border-bottom: 2px solid black;")
                self.label.setText("")
                self.label.setObjectName("label")
                self.firstNameLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.firstNameLabel.setGeometry(QtCore.QRect(50, 200, 91, 21))
                self.firstNameLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.firstNameLabel.setObjectName("firstNameLabel")
                self.emailLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.emailLabel.setGeometry(QtCore.QRect(50, 260, 91, 21))
                self.emailLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.emailLabel.setObjectName("emailLabel")
                self.addressLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.addressLabel.setGeometry(QtCore.QRect(330, 200, 91, 21))
                self.addressLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.addressLabel.setObjectName("addressLabel")
                self.telephoneNoLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.telephoneNoLabel.setGeometry(QtCore.QRect(330, 230, 101, 21))
                self.telephoneNoLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.telephoneNoLabel.setObjectName("telephoneNoLabel")
                self.ccNumberLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.ccNumberLabel.setGeometry(QtCore.QRect(330, 260, 91, 21))
                self.ccNumberLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.ccNumberLabel.setObjectName("ccNumberLabel")
                self.LastNameLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.LastNameLabel.setGeometry(QtCore.QRect(50, 230, 91, 21))
                self.LastNameLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.LastNameLabel.setObjectName("LastNameLabel")
                self.passwordLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.passwordLabel.setGeometry(QtCore.QRect(330, 170, 91, 21))
                self.passwordLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.passwordLabel.setObjectName("passwordLabel")
                self.dTelephoneNoLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dTelephoneNoLineEdit.setGeometry(QtCore.QRect(440, 230, 161, 20))
                self.dTelephoneNoLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dTelephoneNoLineEdit.setObjectName("dTelephoneNoLineEdit")
                self.dAddressLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dAddressLineEdit.setGeometry(QtCore.QRect(440, 200, 161, 20))
                self.dAddressLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dAddressLineEdit.setObjectName("dAddressLineEdit")
                self.dPasswordLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dPasswordLineEdit.setGeometry(QtCore.QRect(440, 170, 161, 20))
                self.dPasswordLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dPasswordLineEdit.setObjectName("dPasswordLineEdit")
                self.dEmailLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dEmailLineEdit.setGeometry(QtCore.QRect(130, 260, 161, 20))
                self.dEmailLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dEmailLineEdit.setObjectName("dEmailLineEdit")
                self.dLastNameLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dLastNameLineEdit.setGeometry(QtCore.QRect(130, 230, 161, 20))
                self.dLastNameLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dLastNameLineEdit.setObjectName("dLastNameLineEdit")
                self.dFirstNameLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dFirstNameLineEdit.setGeometry(QtCore.QRect(130, 200, 161, 20))
                self.dFirstNameLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dFirstNameLineEdit.setText("")
                self.dFirstNameLineEdit.setObjectName("dFirstNameLineEdit")
                self.dLicencePlateLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dLicencePlateLineEdit.setGeometry(QtCore.QRect(440, 260, 161, 20))
                self.dLicencePlateLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dLicencePlateLineEdit.setObjectName("dLicencePlateLineEdit")
                self.label_11 = QtWidgets.QLabel(self.driverRegisterScreen)
                self.label_11.setGeometry(QtCore.QRect(40, 140, 571, 211))
                self.label_11.setStyleSheet("border: 2px solid rgb(255, 0, 127);\n"
        "background-color: rgb(149, 200, 255);")
                self.label_11.setText("")
                self.label_11.setObjectName("label_11")
                self.registerSlogan = QtWidgets.QLabel(self.driverRegisterScreen)
                self.registerSlogan.setGeometry(QtCore.QRect(120, 90, 401, 16))
                self.registerSlogan.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 15px;\n"
        "text-align: center;\n"
        "border: none;\n"
        "color: white;\n"
        "background-color: none;\n""")
                self.registerSlogan.setObjectName("registerSlogan")
                self.dDriverIDLineEdit = QtWidgets.QLineEdit(self.driverRegisterScreen)
                self.dDriverIDLineEdit.setGeometry(QtCore.QRect(130, 170, 161, 20))
                self.dDriverIDLineEdit.setStyleSheet("background: red;\n"
        "border: 1px solid blue;")
                self.dDriverIDLineEdit.setText("")
                self.dDriverIDLineEdit.setEnabled(False)
                self.dDriverIDLineEdit.setObjectName("dDriverIDLineEdit")
                self.customerIDLabel = QtWidgets.QLabel(self.driverRegisterScreen)
                self.customerIDLabel.setGeometry(QtCore.QRect(50, 170, 91, 21))
                self.customerIDLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: red;\n"
        "border: none;\n"
        "background-color: none;")
                self.customerIDLabel.setObjectName("customerIDLabel")
                self.label_3 = QtWidgets.QLabel(self.driverRegisterScreen)
                self.label_3.setGeometry(QtCore.QRect(170, 170, 91, 20))
                self.label_3.setStyleSheet("background-color: none;\n"
        "border: none;")
                self.label_3.setObjectName("label_3")
                self.logo_2 = QtWidgets.QLabel(self.driverRegisterScreen)
                self.logo_2.setGeometry(QtCore.QRect(40, 360, 101, 61))
                self.logo_2.setStyleSheet("background-color: none;\n"
        "border: none;")
                self.logo_2.setText("")
                self.logo_2.setPixmap(QtGui.QPixmap("../Sketch imgs/registerNow.png"))
                self.logo_2.setScaledContents(True)
                self.logo_2.setObjectName("logo_2")
                self.logo = QtWidgets.QLabel(self.driverRegisterScreen)
                self.logo.setGeometry(QtCore.QRect(50, 0, 61, 61))
                self.logo.setStyleSheet("background-color: none;\n"
        "border: none;\n"
        "padding: 3px 0px;")
                self.logo.setText("")
                self.logo.setPixmap(QtGui.QPixmap("../Sketch imgs/official-taxi-logo.png"))
                self.logo.setScaledContents(True)
                self.logo.setObjectName("logo")
                self.label.raise_()
                self.label_11.raise_()
                self.backBtn.raise_()
                self.registerAsDriverBtn.raise_()
                self.register_txt.raise_()
                self.firstNameLabel.raise_()
                self.emailLabel.raise_()
                self.addressLabel.raise_()
                self.telephoneNoLabel.raise_()
                self.ccNumberLabel.raise_()
                self.LastNameLabel.raise_()
                self.passwordLabel.raise_()
                self.dTelephoneNoLineEdit.raise_()
                self.dAddressLineEdit.raise_()
                self.dPasswordLineEdit.raise_()
                self.dEmailLineEdit.raise_()
                self.dLastNameLineEdit.raise_()
                self.dFirstNameLineEdit.raise_()
                self.dLicencePlateLineEdit.raise_()
                self.registerSlogan.raise_()
                self.dDriverIDLineEdit.raise_()
                self.customerIDLabel.raise_()
                self.label_3.raise_()
                self.logo_2.raise_()
                self.logo.raise_()

                self.retranslateUi(driverRegisterScreen_Dialog)
                QtCore.QMetaObject.connectSlotsByName(driverRegisterScreen_Dialog)

        def retranslateUi(self, driverRegisterScreen_Dialog):
                _translate = QtCore.QCoreApplication.translate
                driverRegisterScreen_Dialog.setWindowTitle(_translate("driverRegisterScreen_Dialog", "Dialog"))
                self.register_txt.setText(_translate("driverRegisterScreen_Dialog", "DRIVER REGISTRATION"))
                self.backBtn.setText(_translate("driverRegisterScreen_Dialog", "BACK"))
                self.registerAsDriverBtn.setText(_translate("driverRegisterScreen_Dialog", "Register as Driver"))
                self.firstNameLabel.setText(_translate("driverRegisterScreen_Dialog", "First Name"))
                self.emailLabel.setText(_translate("driverRegisterScreen_Dialog", "Email"))
                self.addressLabel.setText(_translate("driverRegisterScreen_Dialog", "Address"))
                self.telephoneNoLabel.setText(_translate("driverRegisterScreen_Dialog", "Telephone No"))
                self.ccNumberLabel.setText(_translate("driverRegisterScreen_Dialog", "License Plate"))
                self.LastNameLabel.setText(_translate("driverRegisterScreen_Dialog", "Last Name"))
                self.passwordLabel.setText(_translate("driverRegisterScreen_Dialog", "Password"))
                self.registerSlogan.setText(_translate("driverRegisterScreen_Dialog",
                 "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">REGISTER NOW &amp;"
                 " BE PART OF THE TAXI COMPANY!!</span></p></body></html>"))
                self.customerIDLabel.setText(_translate("driverRegisterScreen_Dialog", "Driver ID"))
                self.label_3.setText(_translate("driverRegisterScreen_Dialog", "Auto Generated"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    driverRegisterScreen_Dialog = QtWidgets.QDialog()
    ui = Ui_driverRegisterScreen_Dialog()
    ui.driverRegisterScreen_setupUi(driverRegisterScreen_Dialog)
    driverRegisterScreen_Dialog.show()
    sys.exit(app.exec_())