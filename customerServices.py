# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customerServices.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import homePage
import makeABooking
import  cancelABooking
import  viewABooking


class Ui_CustomerPortal(object):
    def __init__(self, Dialog):   # creation of a constructor
        self.Dialog = QtWidgets.QDialog()   # this class has one attribute
        self.CustomerPortal_setupUi(self.Dialog)   # attribute is need to setup the ui

    def its_showtime(self):   # used to show the dialog
        self.Dialog.show()

    def its_closetime(self):   # used to close the dialog
        self.Dialog.close()

    def logout_button_click(self):   # goes back to the Home Screen.
        self.dialog = QtWidgets.QDialog()
        hP = homePage.Ui_homeScreen_Dialog(self.dialog)
        hP.its_showtime()
        self.its_closetime()

    def makeBooking_button_click(self):   # open the Make Booking screen
        self.dialog = QtWidgets.QDialog()
        mB = makeABooking.Ui_makeBookingScreen_Dialog(self.dialog)
        mB.its_showtime()
        self.its_closetime()

    def cancelBooking_button_click(self):    # open the Cancel Booking screen
        self.dialog = QtWidgets.QDialog()
        cB = cancelABooking.Ui_cancelBookingScreen_Dialog(self.dialog)
        cB.its_showtime()
        self.its_closetime()

    def viewBooking_button_click(self):   # open the View Booking screen
        self.dialog = QtWidgets.QDialog()
        vB = viewABooking.Ui_viewBookingScreen_Dialog(self.dialog)
        vB.its_showtime()
        self.its_closetime()

    def CustomerPortal_setupUi(self, CustomerPortal):
        CustomerPortal.setObjectName("CustomerPortal")
        CustomerPortal.resize(671, 460)
        self.customerServices = QtWidgets.QWidget(CustomerPortal)
        self.customerServices.setGeometry(QtCore.QRect(10, 10, 651, 441))
        self.customerServices.setStyleSheet("border: 8px solid black;\n"
    "background-color:qlineargradient(spread:pad, x1:0.0511364, y1:1, x2:0, y2:0, stop:0 rgba(251, 255, 0, 255), "
    "stop:0.98 rgba(0, 61, 255, 255), stop:1 rgba(0, 0, 0, 0));\n""")
        self.customerServices.setObjectName("customerServices")
        self.cServices_txt = QtWidgets.QLabel(self.customerServices)
        self.cServices_txt.setGeometry(QtCore.QRect(210, 10, 271, 51))
        self.cServices_txt.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 24px;\n"
    "border: none;\n"
    "background-color: none;\n"
    "color: yellow;\n""")
        self.cServices_txt.setObjectName("cServices_txt")
        self.logoutBtn = QtWidgets.QPushButton(self.customerServices,
                                               clicked=lambda: self.logout_button_click())
        self.logoutBtn.setGeometry(QtCore.QRect(520, 400, 121, 31))
        self.logoutBtn.setStyleSheet("background: red;\n"
    "border: 3px solid blue;\n"
    "box-sizing: border-box;\n"
    "border-radius: 15px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 14px;\n"
    "text-align: center;\n"
    "color: white;")
        self.logoutBtn.setObjectName("logoutBtn")
        self.makeBookingBtn = QtWidgets.QPushButton(self.customerServices,
                                                    clicked=lambda: self.makeBooking_button_click())
        self.makeBookingBtn.setGeometry(QtCore.QRect(50, 230, 171, 141))
        self.makeBookingBtn.setStyleSheet("background: blue;\n"
    "border: 3px solid rgb(255, 0, 127);\n"
    "box-sizing: border-box;\n"
    "border-radius: 10px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 13px;\n"
    "text-align: center;\n"
    "color: white;\n"
    "padding-top: 100px;")
        self.makeBookingBtn.setObjectName("makeBookingBtn")
        self.viewBookingBtn = QtWidgets.QPushButton(self.customerServices,
                                                    clicked=lambda: self.viewBooking_button_click())
        self.viewBookingBtn.setGeometry(QtCore.QRect(240, 230, 171, 141))
        self.viewBookingBtn.setStyleSheet("background: blue;\n"
    "border: 3px solid rgb(255, 0, 127);\n"
    "box-sizing: border-box;\n"
    "border-radius: 10px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 13px;\n"
    "text-align: center;\n"
    "color: white;\n"
    "padding-top: 100px;")
        self.viewBookingBtn.setObjectName("viewBookingBtn")
        self.cancelBookingBtn = QtWidgets.QPushButton(self.customerServices,
                                                      clicked=lambda: self.cancelBooking_button_click())
        self.cancelBookingBtn.setGeometry(QtCore.QRect(430, 230, 171, 141))
        self.cancelBookingBtn.setStyleSheet("background: blue;\n"
    "border: 3px solid rgb(255, 0, 127);\n"
    "box-sizing: border-box;\n"
    "border-radius: 10px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 13px;\n"
    "text-align: center;\n"
    "color: white;\n"
    "padding-top: 100px;")
        self.cancelBookingBtn.setObjectName("cancelBookingBtn")
        self.label = QtWidgets.QLabel(self.customerServices)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 71))
        self.label.setStyleSheet("background-color: black;\n"
    "border-bottom: 2px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(self.customerServices)
        self.logo.setGeometry(QtCore.QRect(40, 0, 71, 71))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.logo.setStyleSheet("background-color: none;\n"
    "border: none;\n"
    "padding: 5px 3px;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Sketch imgs/official-taxi-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.confirmBookingIcon = QtWidgets.QLabel(self.customerServices)
        self.confirmBookingIcon.setGeometry(QtCore.QRect(470, 240, 101, 91))
        self.confirmBookingIcon.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.confirmBookingIcon.setText("")
        self.confirmBookingIcon.setPixmap(QtGui.QPixmap("../Sketch imgs/cancelbookingicon.png"))
        self.confirmBookingIcon.setScaledContents(True)
        self.confirmBookingIcon.setObjectName("confirmBookingIcon")
        self.confirmBookingIcon_2 = QtWidgets.QLabel(self.customerServices)
        self.confirmBookingIcon_2.setGeometry(QtCore.QRect(280, 240, 101, 81))
        self.confirmBookingIcon_2.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.confirmBookingIcon_2.setText("")
        self.confirmBookingIcon_2.setPixmap(QtGui.QPixmap("../Sketch imgs/viewbooking.png"))
        self.confirmBookingIcon_2.setScaledContents(True)
        self.confirmBookingIcon_2.setObjectName("confirmBookingIcon_2")
        self.confirmBookingIcon_3 = QtWidgets.QLabel(self.customerServices)
        self.confirmBookingIcon_3.setGeometry(QtCore.QRect(90, 240, 101, 91))
        self.confirmBookingIcon_3.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.confirmBookingIcon_3.setText("")
        self.confirmBookingIcon_3.setPixmap(QtGui.QPixmap("../Sketch imgs/create.png"))
        self.confirmBookingIcon_3.setScaledContents(True)
        self.confirmBookingIcon_3.setObjectName("confirmBookingIcon_3")
        self.welcome_2 = QtWidgets.QLabel(self.customerServices)
        self.welcome_2.setGeometry(QtCore.QRect(220, 80, 211, 91))
        self.welcome_2.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.welcome_2.setText("")
        self.welcome_2.setPixmap(QtGui.QPixmap("../Sketch imgs/welcomeAdmin.png"))
        self.welcome_2.setScaledContents(True)
        self.welcome_2.setObjectName("welcome_2")
        self.slogan = QtWidgets.QLabel(self.customerServices)
        self.slogan.setGeometry(QtCore.QRect(110, 170, 441, 41))
        self.slogan.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 14px;\n"
    "text-align: center;\n"
    "border: none;\n"
    "color: white;\n"
    "background-color:none;\n""")
        self.slogan.setObjectName("slogan")
        self.label.raise_()
        self.logoutBtn.raise_()
        self.makeBookingBtn.raise_()
        self.viewBookingBtn.raise_()
        self.cancelBookingBtn.raise_()
        self.cServices_txt.raise_()
        self.logo.raise_()
        self.confirmBookingIcon.raise_()
        self.confirmBookingIcon_2.raise_()
        self.confirmBookingIcon_3.raise_()
        self.welcome_2.raise_()
        self.slogan.raise_()

        self.retranslateUi(CustomerPortal)
        QtCore.QMetaObject.connectSlotsByName(CustomerPortal)

    def retranslateUi(self, CustomerPortal):
        _translate = QtCore.QCoreApplication.translate
        CustomerPortal.setWindowTitle(_translate("CustomerPortal", "Dialog"))
        self.cServices_txt.setText(_translate("CustomerPortal", "CUSTOMER SERVICES"))
        self.logoutBtn.setText(_translate("CustomerPortal", "LOGOUT"))
        self.makeBookingBtn.setText(_translate("CustomerPortal", "MAKE A BOOKING"))
        self.viewBookingBtn.setText(_translate("CustomerPortal", "VIEW BOOKING"))
        self.cancelBookingBtn.setText(_translate("CustomerPortal", "CANCEL BOOKING"))
        self.slogan.setText(_translate("CustomerPortal",
        "<html><head/><body><p align=\"center\">We strive for excellence with each and every interaction."
        "<br> The best customer service. Period</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomerPortal = QtWidgets.QDialog()
    ui = Ui_CustomerPortal()
    ui.CustomerPortal_setupUi(CustomerPortal)
    CustomerPortal.show()
    sys.exit(app.exec_())
