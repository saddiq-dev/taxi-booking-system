# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customerLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import register
import customerServices
import forgotPasswordScreen
import homePage

conn = sqlite3.connect('taxi.db')    # creates the actual database
c = conn.cursor()      # The cursor to take data to and from the database.

class Ui_customerLoginScreen_Dialog(object):
    def __init__(self, Dialog):   # creation of a constructor
        self.Dialog = QtWidgets.QDialog()    # this class has one attribute
        self.customerLoginScreen_setupUi(self.Dialog)    # attribute is need to setup the ui

    def its_showtime(self):  # used to show the dialog
        self.Dialog.show()

    def its_closetime(self):  # used to close the dialog
        self.Dialog.close()

    def customerBack_clicked(self):
        self.dialog = QtWidgets.QDialog()     # goes back to the Home Page
        hP = homePage.Ui_homeScreen_Dialog(self.dialog)
        hP.its_showtime()
        self.its_closetime()

    def get_customer_info(self):
        c.execute("SELECT * FROM Customer WHERE email=:email",
                  {'email': self.customerEmail_txt.text(),
                   'password': self.customerPassword_txt.text})
        return c.fetchall()  # returns the password from the database

    def customerLogin_clicked(self):
        if self.customerPassword_txt.text() and self.customerEmail_txt.text() == \
           self.customerEmail_txt.text() in self.get_customer_info().__str__() and \
           self.customerPassword_txt.text() in self.get_customer_info().__str__():
           self.successfull_login_msg("Congratulations, your login credentials is correct. Enjoy!!")
           self.dialog = QtWidgets.QDialog()     # open the Customer Services screen for positive login.
           cS = customerServices.Ui_CustomerPortal(self.dialog)
           cS.its_showtime()
           self.its_closetime()
        else:
            self.failed_login_message("Incorrect Login Credentials!")

    def successfull_login_msg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Notification.")
        msg.setInformativeText(message)
        msg.setWindowTitle("Congratulations")
        msg.setDetailedText("The details are as follows:" + message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def failed_login_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Notification.")
        msg.setInformativeText(message)
        msg.setWindowTitle("Notification")
        msg.setDetailedText("The details are as follows:" + message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def register_button_click(self):
        self.dialog = QtWidgets.QDialog()
        r = register.Ui_registerScreen_Dialog(self.dialog)
        r.its_showtime()
        self.its_closetime()

    def forgotPassword_button_click(self):
        self.dialog = QtWidgets.QDialog()
        fP = forgotPasswordScreen.Ui_forgotPasswordScreen_Dialog(self.dialog)
        fP.its_showtime()
        self.its_closetime()

    def customerLoginScreen_setupUi(self, customerLoginScreen_Dialog):
        customerLoginScreen_Dialog.setObjectName("customerLoginScreen_Dialog")
        customerLoginScreen_Dialog.resize(671, 459)
        self.customerLoginScreen = QtWidgets.QWidget(customerLoginScreen_Dialog)
        self.customerLoginScreen.setGeometry(QtCore.QRect(10, 10, 651, 441))
        self.customerLoginScreen.setStyleSheet("border: 8px solid black;\n"
    "background-color:qlineargradient(spread:pad, x1:0.0511364, y1:1, x2:0, y2:0, stop:0 rgba(251, 255, 0, 255), "
    "stop:0.98 rgba(0, 61, 255, 255), stop:1 rgba(0, 0, 0, 0));\n""")
        self.customerLoginScreen.setObjectName("customerLoginScreen")
        self.customerRegisterBtn = QtWidgets.QPushButton(self.customerLoginScreen,
                                                         clicked=lambda: self.register_button_click())
        self.customerRegisterBtn.setGeometry(QtCore.QRect(20, 390, 231, 31))
        self.customerRegisterBtn.setStyleSheet("background: #FFFFFF;\n"
    "border: 2px solid red;\n"
    "box-sizing: border-box;\n"
    "border-radius: 15px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 12px;\n"
    "text-align: center;")
        self.customerRegisterBtn.setObjectName("customerRegisterBtn")
        self.customerLoginBtn = QtWidgets.QPushButton(self.customerLoginScreen,
                                                      clicked=lambda: self.customerLogin_clicked())
        self.customerLoginBtn.setGeometry(QtCore.QRect(290, 300, 101, 31))
        self.customerLoginBtn.setStyleSheet("background-color: rgb(255, 0, 127);\n"
    "border: 3px solid #0029FF;\n"
    "box-sizing: border-box;\n"
    "border-radius: 15px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 12px;\n"
    "text-align: center;\n"
    "color: white;")
        self.customerLoginBtn.setObjectName("customerLoginBtn")
        self.customerEmail_txt = QtWidgets.QLineEdit(self.customerLoginScreen)
        self.customerEmail_txt.setGeometry(QtCore.QRect(260, 240, 211, 20))
        self.customerEmail_txt.setStyleSheet("background: #C4C4C4;\n"
    "border: 2px solid blue;")
        self.customerEmail_txt.setObjectName("customerEmail_txt")
        self.customerPassword_txt = QtWidgets.QLineEdit(self.customerLoginScreen)
        self.customerPassword_txt.setGeometry(QtCore.QRect(260, 270, 211, 20))
        self.customerPassword_txt.setStyleSheet("background: #C4C4C4;\n"
    "border: 2px solid blue;")
        self.customerPassword_txt.setObjectName("customerPassword_txt")
        self.customerPassword_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.email_label = QtWidgets.QLabel(self.customerLoginScreen)
        self.email_label.setGeometry(QtCore.QRect(160, 240, 51, 16))
        self.email_label.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 15px;\n"
    "text-align: center;\n"
    "color: #000000;\n"
    "border: none;\n"
    "background-color:none;")
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(self.customerLoginScreen)
        self.password_label.setGeometry(QtCore.QRect(160, 270, 81, 16))
        self.password_label.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 15px;\n"
    "text-align: center;\n"
    "color: #000000;\n"
    "border: none;\n"
    "background-color:none;")
        self.password_label.setObjectName("password_label")
        self.customerLoginLabel = QtWidgets.QLabel(self.customerLoginScreen)
        self.customerLoginLabel.setGeometry(QtCore.QRect(240, 190, 191, 21))
        self.customerLoginLabel.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 18px;\n"
    "text-align: center;\n"
    "border: none;\n"
    "background-color:none;\n""")
        self.customerLoginLabel.setObjectName("customerLoginLabel")
        self.customerForgotPasswordbtn = QtWidgets.QPushButton(self.customerLoginScreen,
                                                               clicked=lambda: self.forgotPassword_button_click())
        self.customerForgotPasswordbtn.setGeometry(QtCore.QRect(470, 340, 121, 21))
        self.customerForgotPasswordbtn.setStyleSheet("background: red;\n"
    "border: 2px solid blue;\n"
    "box-sizing: border-box;\n"
    "border-radius: 15px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 12px;\n"
    "text-align: center;\n"
    "color: white;\n""")
        self.customerForgotPasswordbtn.setObjectName("customerForgotPasswordbtn")
        self.customerBackBtn = QtWidgets.QPushButton(self.customerLoginScreen,
                                                      clicked=lambda: self.customerBack_clicked())
        self.customerBackBtn.setGeometry(QtCore.QRect(540, 390, 91, 31))
        self.customerBackBtn.setStyleSheet("background: red;\n"
    "border: 3px solid blue;\n"
    "box-sizing: border-box;\n"
    "border-radius: 15px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 13px;\n"
    "text-align: center;\n"
    "color: white;")
        self.customerBackBtn.setObjectName("customerBackBtn")
        self.border = QtWidgets.QLabel(self.customerLoginScreen)
        self.border.setGeometry(QtCore.QRect(50, 170, 551, 201))
        self.border.setStyleSheet("border: 3.5px dotted red;\n"
    "background-color:none;\n""")
        self.border.setText("")
        self.border.setObjectName("border")
        self.slogan = QtWidgets.QLabel(self.customerLoginScreen)
        self.slogan.setGeometry(QtCore.QRect(110, 120, 441, 31))
        self.slogan.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 14px;\n"
    "text-align: center;\n"
    "border: none;\n"
    "color: white;\n"
    "background-color:none;\n""")
        self.slogan.setObjectName("slogan")
        self.logo = QtWidgets.QLabel(self.customerLoginScreen)
        self.logo.setGeometry(QtCore.QRect(270, 10, 111, 101))
        self.logo.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Sketch imgs/official-taxi-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.border.raise_()
        self.customerRegisterBtn.raise_()
        self.customerLoginBtn.raise_()
        self.customerEmail_txt.raise_()
        self.customerPassword_txt.raise_()
        self.email_label.raise_()
        self.password_label.raise_()
        self.customerLoginLabel.raise_()
        self.customerForgotPasswordbtn.raise_()
        self.customerBackBtn.raise_()
        self.slogan.raise_()
        self.logo.raise_()

        self.retranslateUi(customerLoginScreen_Dialog)
        QtCore.QMetaObject.connectSlotsByName(customerLoginScreen_Dialog)

    def retranslateUi(self, customerLoginScreen_Dialog):
        _translate = QtCore.QCoreApplication.translate
        customerLoginScreen_Dialog.setWindowTitle(_translate("customerLoginScreen_Dialog", "Dialog"))
        self.customerRegisterBtn.setText(_translate("customerLoginScreen_Dialog", "Don\'t have an account? REGISTER"))
        self.customerLoginBtn.setText(_translate("customerLoginScreen_Dialog", "LOGIN"))
        self.email_label.setText(_translate("customerLoginScreen_Dialog", "Email"))
        self.password_label.setText(_translate("customerLoginScreen_Dialog", "Password"))
        self.customerLoginLabel.setText(_translate("customerLoginScreen_Dialog",
        "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">CUSTOMER LOGIN"
        "</span></p></body></html>"))
        self.customerForgotPasswordbtn.setText(_translate("customerLoginScreen_Dialog", "Forgot Password"))
        self.customerBackBtn.setText(_translate("customerLoginScreen_Dialog", "BACK"))
        self.slogan.setText(_translate("customerLoginScreen_Dialog",
        "<html><head/><body><p align=\"center\">We strive for excellence with each and every interaction."
        "<br> The best customer service. Period</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customerLoginScreen_Dialog = QtWidgets.QDialog()
    ui = Ui_customerLoginScreen_Dialog()
    ui.customerLoginScreen_setupUi(customerLoginScreen_Dialog)
    customerLoginScreen_Dialog.show()
    sys.exit(app.exec_())
