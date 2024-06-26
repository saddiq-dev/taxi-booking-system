# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driverViewBooking.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import driverServices

conn = sqlite3.connect('taxi.db')   # creates the actual database
c = conn.cursor()   # The cursor to take data to and from the database.

class Ui_driverViewBookingScreen_Dialog(object):

        def __init__(self, Dialog):   # creation of a constructor
                self.Dialog = QtWidgets.QDialog()    # this class has one attribute
                self.driverViewBookingScreen_setupUi(self.Dialog)    # attribute is need to setup the ui

        def its_showtime(self):   # used to show the dialog
                self.Dialog.show()

        def its_closetime(self):   # used to close the dialog
                self.Dialog.close()

        def back_button_click(self):  # goes back to the Driver Services Screen.
                self.dialog = QtWidgets.QDialog()
                dS = driverServices.Ui_driverScreen_Dialog(self.dialog)
                dS.its_showtime()
                self.its_closetime()

        def get_customer_info(self):
                c.execute("SELECT * FROM Booking WHERE bookingId=:bookingId",
                          {'bookingId': self.bookingIdLineEdit.text()})
                return c.fetchall()  # returns the record from the database

        def viewall(self):
                if self.bookingIdLineEdit.text() and \
                    self.bookingIdLineEdit.text() in self.get_customer_info().__str__():
                 List = self.get_customer_info()
                 self.showdialog("Congratulations, your booking was successfully found, you may now view your booking!")
                 self.bookingIdLineEdit.setEnabled(False)    # Disables Booking Id field.
                 self.viewBookingBtn.setEnabled(False)      # Disables View Booking Btn.

                 self.bookingIdLineEdit.setText(str(List[0][0]))
                 self.customerIdLineEdit.setText(str(List[0][1]))
                 self.adminIdLineEdit.setText(str(List[0][2]))
                 self.driverIdLineEdit.setText(str(List[0][3]))
                 self.bookingStatusLineEdit.setText(List[0][4])
                 self.dateBookedLineEdit.setText(List[0][5])
                 self.pickUpAddressLineEdit.setText(List[0][6])
                 self.dropOffAddressLineEdit.setText(List[0][7])
                 self.pickUpTimeLineEdit.setText(List[0][8])
                 self.pickUpDateLineEdit.setText(List[0][9])
                 self.costOfTripLineEdit.setText(List[0][10])
                 self.paidLineEdit.setText(List[0][11])
                else:
                     self.wrongBookingID("Sorry, your BookingID is Invalid.")

        def showdialog(self, message):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("This is a confirmation message.")
                msg.setInformativeText(message)
                msg.setWindowTitle("Confirmation")
                msg.setDetailedText("The details are as follows:" + message)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()

        def wrongBookingID(self, message):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Invalid BookingID.")
                msg.setInformativeText(message)
                msg.setWindowTitle("Notification")
                msg.setDetailedText("The details are as follows:" + message)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()

        def driverViewBookingScreen_setupUi(self, driverViewBookingScreen_Dialog):
                driverViewBookingScreen_Dialog.setObjectName("driverViewBookingScreen_Dialog")
                driverViewBookingScreen_Dialog.resize(671, 460)
                self.driverViewBookingScreen = QtWidgets.QWidget(driverViewBookingScreen_Dialog)
                self.driverViewBookingScreen.setGeometry(QtCore.QRect(10, 10, 651, 441))
                self.driverViewBookingScreen.setStyleSheet("border: 8px solid black;\n"
        "background-color:qlineargradient(spread:pad, x1:0.0511364, y1:1, x2:0, y2:0, stop:0 rgba(251, 255, 0, 255), "
        "stop:0.98 rgba(0, 61, 255, 255), stop:1 rgba(0, 0, 0, 0));\n""")
                self.driverViewBookingScreen.setObjectName("driverViewBookingScreen")
                self.view_txt = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.view_txt.setGeometry(QtCore.QRect(170, 10, 301, 51))
                self.view_txt.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 24px;\n"
        "border: none;\n"
        "background-color: none;\n"
        "color: yellow;\n""")
                self.view_txt.setObjectName("view_txt")
                self.backBtn = QtWidgets.QPushButton(self.driverViewBookingScreen,
                                                     clicked=lambda: self.back_button_click())
                self.backBtn.setGeometry(QtCore.QRect(540, 390, 91, 31))
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
                self.label = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.label.setGeometry(QtCore.QRect(0, 0, 651, 71))
                self.label.setStyleSheet("background-color: black;\n"
        "border-bottom: 2px solid black;")
                self.label.setText("")
                self.label.setObjectName("label")
                self.dateBookedLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.dateBookedLabel.setGeometry(QtCore.QRect(30, 300, 91, 21))
                self.dateBookedLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.dateBookedLabel.setObjectName("dateBookedLabel")
                self.dropOffAddresslLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.dropOffAddresslLabel.setGeometry(QtCore.QRect(330, 180, 121, 21))
                self.dropOffAddresslLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.dropOffAddresslLabel.setObjectName("dropOffAddresslLabel")
                self.pickUpDateLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.pickUpDateLabel.setGeometry(QtCore.QRect(330, 240, 91, 21))
                self.pickUpDateLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpDateLabel.setObjectName("pickUpDateLabel")
                self.pickUpAddressLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.pickUpAddressLabel.setGeometry(QtCore.QRect(330, 150, 111, 21))
                self.pickUpAddressLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpAddressLabel.setObjectName("pickUpAddressLabel")
                self.pickUpTimeLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.pickUpTimeLabel.setGeometry(QtCore.QRect(330, 210, 101, 21))
                self.pickUpTimeLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpTimeLabel.setObjectName("pickUpTimeLabel")
                self.driverIdLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.driverIdLineEdit.setGeometry(QtCore.QRect(130, 240, 161, 20))
                self.driverIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.driverIdLineEdit.setObjectName("driverIdLineEdit")
                self.driverIdLineEdit.setEnabled(False)
                self.adminIdLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.adminIdLineEdit.setGeometry(QtCore.QRect(130, 210, 161, 20))
                self.adminIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.adminIdLineEdit.setObjectName("adminIdLineEdit")
                self.adminIdLineEdit.setEnabled(False)
                self.blueBackground = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.blueBackground.setGeometry(QtCore.QRect(20, 140, 611, 241))
                self.blueBackground.setStyleSheet("border: 2px solid rgb(255, 0, 127);\n"
        "background-color: rgb(149, 200, 255);")
                self.blueBackground.setText("")
                self.blueBackground.setObjectName("blueBackground")
                self.viewSlogan = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.viewSlogan.setGeometry(QtCore.QRect(50, 80, 541, 51))
                self.viewSlogan.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 15px;\n"
        "text-align: center;\n"
        "border: none;\n"
        "color: white;\n"
        "background-color: none;")
                self.viewSlogan.setObjectName("viewSlogan")
                self.bookingStatusLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.bookingStatusLineEdit.setGeometry(QtCore.QRect(130, 270, 161, 20))
                self.bookingStatusLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.bookingStatusLineEdit.setObjectName("bookingStatusLineEdit")
                self.bookingStatusLineEdit.setEnabled(False)
                self.customerIdLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.customerIdLineEdit.setGeometry(QtCore.QRect(130, 180, 161, 20))
                self.customerIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.customerIdLineEdit.setObjectName("customerIdLineEdit")
                self.customerIdLineEdit.setEnabled(False)
                self.bookingIdLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.bookingIdLabel.setGeometry(QtCore.QRect(30, 150, 91, 21))
                self.bookingIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.bookingIdLabel.setObjectName("bookingIdLabel")
                self.bookingIdLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.bookingIdLineEdit.setGeometry(QtCore.QRect(130, 150, 161, 20))
                self.bookingIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.bookingIdLineEdit.setObjectName("bookingIdLineEdit")
                self.pickUpAddressLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.pickUpAddressLineEdit.setGeometry(QtCore.QRect(460, 150, 161, 20))
                self.pickUpAddressLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpAddressLineEdit.setObjectName("pickUpAddressLineEdit")
                self.pickUpAddressLineEdit.setEnabled(False)
                self.dropOffAddressLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.dropOffAddressLineEdit.setGeometry(QtCore.QRect(460, 180, 161, 20))
                self.dropOffAddressLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dropOffAddressLineEdit.setObjectName("dropOffAddressLineEdit")
                self.dropOffAddressLineEdit.setEnabled(False)
                self.dateBookedLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.dateBookedLineEdit.setGeometry(QtCore.QRect(130, 300, 161, 20))
                self.dateBookedLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dateBookedLineEdit.setObjectName("dateBookedLineEdit")
                self.dateBookedLineEdit.setEnabled(False)
                self.pickUpTimeLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.pickUpTimeLineEdit.setGeometry(QtCore.QRect(460, 210, 161, 20))
                self.pickUpTimeLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpTimeLineEdit.setObjectName("pickUpTimeLineEdit")
                self.pickUpTimeLineEdit.setEnabled(False)
                self.costOfTripLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.costOfTripLineEdit.setGeometry(QtCore.QRect(460, 270, 161, 20))
                self.costOfTripLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.costOfTripLineEdit.setObjectName("costOfTripLineEdit")
                self.costOfTripLineEdit.setEnabled(False)
                self.pickUpDateLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.pickUpDateLineEdit.setGeometry(QtCore.QRect(460, 240, 161, 20))
                self.pickUpDateLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpDateLineEdit.setObjectName("pickUpDateLineEdit")
                self.pickUpDateLineEdit.setEnabled(False)
                self.paidLineEdit = QtWidgets.QLineEdit(self.driverViewBookingScreen)
                self.paidLineEdit.setGeometry(QtCore.QRect(460, 300, 161, 21))
                self.paidLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.paidLineEdit.setObjectName("paidLineEdit")
                self.paidLineEdit.setEnabled(False)
                self.customerIdLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.customerIdLabel.setGeometry(QtCore.QRect(30, 180, 91, 21))
                self.customerIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.customerIdLabel.setObjectName("customerIdLabel")
                self.bookingStatusLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.bookingStatusLabel.setGeometry(QtCore.QRect(30, 270, 101, 21))
                self.bookingStatusLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.bookingStatusLabel.setObjectName("bookingStatusLabel")
                self.costOfTripLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.costOfTripLabel.setGeometry(QtCore.QRect(330, 270, 91, 21))
                self.costOfTripLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.costOfTripLabel.setObjectName("costOfTripLabel")
                self.driverIdLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.driverIdLabel.setGeometry(QtCore.QRect(30, 240, 71, 21))
                self.driverIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.driverIdLabel.setObjectName("driverIdLabel")
                self.adminIdLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.adminIdLabel.setGeometry(QtCore.QRect(30, 210, 71, 21))
                self.adminIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.adminIdLabel.setObjectName("adminIdLabel")
                self.paidLabel = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.paidLabel.setGeometry(QtCore.QRect(330, 300, 31, 21))
                self.paidLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.paidLabel.setObjectName("paidLabel")
                self.viewBookingBtn = QtWidgets.QPushButton(self.driverViewBookingScreen,
                                                clicked=lambda: self.viewall())
                self.viewBookingBtn.setGeometry(QtCore.QRect(250, 340, 151, 31))
                self.viewBookingBtn.setStyleSheet("background: blue;\n"
        "border: 2px solid rgb(255, 0, 127);\n"
        "box-sizing: border-box;\n"
        "border-radius: 10px;\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: white;")
                self.viewBookingBtn.setObjectName("viewBookingBtn")
                self.logo = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.logo.setGeometry(QtCore.QRect(40, 0,71, 71))
                self.logo.setStyleSheet("background-color: none;\n"
        "border: none;\n"
        "padding: 5px 3px;")
                self.logo.setText("")
                self.logo.setPixmap(QtGui.QPixmap("../Sketch imgs/official-taxi-logo.png"))
                self.logo.setScaledContents(True)
                self.logo.setObjectName("logo")
                self.logo_2 = QtWidgets.QLabel(self.driverViewBookingScreen)
                self.logo_2.setGeometry(QtCore.QRect(30, 390, 81, 31))
                self.logo_2.setStyleSheet("background-color: none;\n"
        "border: none;")
                self.logo_2.setText("")
                self.logo_2.setPixmap(QtGui.QPixmap("../Sketch imgs/eye.png"))
                self.logo_2.setScaledContents(True)
                self.logo_2.setObjectName("logo_2")
                self.blueBackground.raise_()
                self.label.raise_()
                self.backBtn.raise_()
                self.view_txt.raise_()
                self.dateBookedLabel.raise_()
                self.dropOffAddresslLabel.raise_()
                self.pickUpDateLabel.raise_()
                self.pickUpAddressLabel.raise_()
                self.pickUpTimeLabel.raise_()
                self.driverIdLineEdit.raise_()
                self.adminIdLineEdit.raise_()
                self.viewSlogan.raise_()
                self.bookingStatusLineEdit.raise_()
                # self.emailLineEdit.raise_()
                self.customerIdLineEdit.raise_()
                self.bookingIdLabel.raise_()
                self.bookingIdLineEdit.raise_()
                self.pickUpAddressLineEdit.raise_()
                self.dropOffAddressLineEdit.raise_()
                self.dateBookedLineEdit.raise_()
                self.pickUpTimeLineEdit.raise_()
                self.costOfTripLineEdit.raise_()
                self.pickUpDateLineEdit.raise_()
                self.paidLineEdit.raise_()
                self.customerIdLabel.raise_()
                self.bookingStatusLabel.raise_()
                # self.emailLabel.raise_()
                self.costOfTripLabel.raise_()
                self.driverIdLabel.raise_()
                self.adminIdLabel.raise_()
                self.paidLabel.raise_()
                self.viewBookingBtn.raise_()
                self.logo.raise_()
                self.logo_2.raise_()

                self.retranslateUi(driverViewBookingScreen_Dialog)
                QtCore.QMetaObject.connectSlotsByName(driverViewBookingScreen_Dialog)

        def retranslateUi(self, driverViewBookingScreen_Dialog):
                _translate = QtCore.QCoreApplication.translate
                driverViewBookingScreen_Dialog.setWindowTitle(_translate("driverViewBookingScreen_Dialog", "Dialog"))
                self.view_txt.setText(_translate("driverViewBookingScreen_Dialog", "DRIVER VIEW BOOKING"))
                self.backBtn.setText(_translate("driverViewBookingScreen_Dialog", "BACK"))
                self.dateBookedLabel.setText(_translate("driverViewBookingScreen_Dialog", "Date Booked"))
                self.dropOffAddresslLabel.setText(_translate("driverViewBookingScreen_Dialog", "Drop Off Address"))
                self.pickUpDateLabel.setText(_translate("driverViewBookingScreen_Dialog", "Pick Up Date"))
                self.pickUpAddressLabel.setText(_translate("driverViewBookingScreen_Dialog", "Pick Up Address"))
                self.pickUpTimeLabel.setText(_translate("driverViewBookingScreen_Dialog", "Pick Up Time"))
                self.viewSlogan.setText(_translate("driverViewBookingScreen_Dialog",
                "<html><head/><body><p align=\"center\">To View a Booking, enter the Booking ID for the Booking "
                "you want to<br/> View, then click the View Booking button to View the Booking.</p></body></html>"))
                self.bookingIdLabel.setText(_translate("driverViewBookingScreen_Dialog", "Booking ID"))
                self.customerIdLabel.setText(_translate("driverViewBookingScreen_Dialog", "Customer ID"))
                self.bookingStatusLabel.setText(_translate("driverViewBookingScreen_Dialog", "Booking Status"))
                self.costOfTripLabel.setText(_translate("driverViewBookingScreen_Dialog", "Cost of Trip"))
                self.driverIdLabel.setText(_translate("driverViewBookingScreen_Dialog", "Driver ID"))
                self.adminIdLabel.setText(_translate("driverViewBookingScreen_Dialog", "Admin ID"))
                self.paidLabel.setText(_translate("driverViewBookingScreen_Dialog", "Paid"))
                self.viewBookingBtn.setText(_translate("driverViewBookingScreen_Dialog", "VIEW BOOKING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    driverViewBookingScreen_Dialog = QtWidgets.QDialog()
    ui = Ui_driverViewBookingScreen_Dialog()
    ui.driverViewBookingScreen_setupUi(driverViewBookingScreen_Dialog)
    driverViewBookingScreen_Dialog.show()
    sys.exit(app.exec_())
