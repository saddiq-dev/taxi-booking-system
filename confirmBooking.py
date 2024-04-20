# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmBooking.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import adminServices

conn = sqlite3.connect('taxi.db')    # creates the actual database
c = conn.cursor()   # The cursor to take data to and from the database.


class Ui_confirmBookingScreen_Dialog(object):

        def __init__(self, Dialog):   # creation of a constructor
                self.Dialog = QtWidgets.QDialog()    # this class has one attribute
                self.confirmBookingScreen_setupUi(self.Dialog)     # attribute is need to setup the ui

        def its_showtime(self):    # used to show the dialog
                self.Dialog.show()

        def its_closetime(self):    # used to close the dialog
                self.Dialog.close()

        def back_clicked(self):    # goes back to the Customer Services Screen.
                self.dialog = QtWidgets.QDialog()
                aS = adminServices.Ui_adminPortal_Dialog(self.dialog)
                aS.its_showtime()
                self.its_closetime()

        def get_booking_info(self):
                c.execute("SELECT * FROM Booking WHERE bookingId=:bookingId",
                          {'bookingId': self.bookingIdLineEdit.text()})
                return c.fetchall()  # returns the record from the database

        def selectBooking_clicked(self):
            if self.bookingIdLineEdit.text() and \
               self.bookingIdLineEdit.text() in self.get_booking_info().__str__():
                self.viewall()
                self.bookingIdLineEdit.setEnabled(False)
                self.selectBookingBtn.setEnabled(False)
                self.correct_bookingID_msg("Congratulations, the booking was successfully found, "
                                           "you may now update the booking!")
            else:
               self.wrongBookingID("Sorry, the BookingID is not Valid.")

        def viewall(self):
                List = self.get_booking_info()
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

        def confirmNow_clicked(self):
            if self.bookingIdLineEdit.text() and \
               self.bookingIdLineEdit.text() in self.get_booking_info().__str__():
                self.update_record()
                self.showdialog("The Booking was Successfully updated.")
                self.confirmNowBtn.setEnabled(False)   #disable the  confirmNowBtn
                self.customerIdLineEdit.setEnabled(False)  # disables the customerIdLineEdit
                self.adminIdLineEdit.setEnabled(False)     # disables the adminIdLineEdit
                self.driverIdLineEdit.setEnabled(False)    # disables the driverIdLineEdit
                self.bookingStatusLineEdit.setEnabled(False)     # disables the bookingStatusLineEdit
                self.dateBookedLineEdit.setEnabled(False)     # disables the dateBookedLineEdit
                self.pickUpAddressLineEdit.setEnabled(False)     # disables the pickUpAddressLineEdit
                self.dropOffAddressLineEdit.setEnabled(False)   # disables the dropOffAddressLineEdit
                self.pickUpTimeLineEdit.setEnabled(False)   # disables the pickUpTimeLineEdit
                self.pickUpDateLineEdit.setEnabled(False)     # disables the pickUpDateLineEdit
                self.costOfTripLineEdit.setEnabled(False)   # disables the costOfTripLineEdit
                self.paidLineEdit.setEnabled(False)   # disables the paidLineEdit
            else:
               self.wrongBookingID("Sorry, the BookingID is not Valid.")

        def update_record(self):
                with conn:
                        c.execute("""UPDATE Booking SET bookingId= :bookingId, customerId= :customerId, adminId= :adminId, 
                             driverId= :driverId, bookingStatus= :bookingStatus, dateBooked= :dateBooked, 
                             pickUpAddress= :pickUpAddress, dropOffAddress= :dropOffAddress, pickUpTime= :pickUpTime, 
                             pickUpDate= :pickUpDate, costOfTrip= :costOfTrip, paid= :paid WHERE bookingId = :bookingId """,
                                  {'bookingId': self.bookingIdLineEdit.text(),
                                   'customerId': self.customerIdLineEdit.text(),
                                   'adminId': self.adminIdLineEdit.text(),
                                   'driverId': self.driverIdLineEdit.text(),
                                   'bookingStatus': self.bookingStatusLineEdit.text(),
                                   'dateBooked': self.dateBookedLineEdit.text(),
                                   'pickUpAddress': self.pickUpAddressLineEdit.text(),
                                   'dropOffAddress': self.dropOffAddressLineEdit.text(),
                                   'pickUpTime': self.pickUpTimeLineEdit.text(),
                                   'pickUpDate': self.pickUpDateLineEdit.text(),
                                   'costOfTrip': self.costOfTripLineEdit.text(),
                                   'paid': self.paidLineEdit.text()})

        def showdialog(self, message):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Confirmation")
                msg.setInformativeText(message)
                msg.setWindowTitle("Booking Updated")
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

        def correct_bookingID_msg(self, message):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Valid BookingID.")
                msg.setInformativeText(message)
                msg.setWindowTitle("Notification")
                msg.setDetailedText("The details are as follows:" + message)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()

        def confirmBookingScreen_setupUi(self, confirmBookingScreen_Dialog):
                confirmBookingScreen_Dialog.setObjectName("confirmBookingScreen_Dialog")
                confirmBookingScreen_Dialog.resize(671, 460)
                self.confirmABookingScreen = QtWidgets.QWidget(confirmBookingScreen_Dialog)
                self.confirmABookingScreen.setGeometry(QtCore.QRect(10, 10, 651, 441))
                self.confirmABookingScreen.setStyleSheet("border: 8px solid black;\n"
        "background-color:qlineargradient(spread:pad, x1:0.0511364, y1:1, x2:0, y2:0, stop:0 rgba(251, 255, 0, 255), "
        "stop:0.98 rgba(0, 61, 255, 255), stop:1 rgba(0, 0, 0, 0));\n""")
                self.confirmABookingScreen.setObjectName("confirmABookingScreen")
                self.confirm_txt = QtWidgets.QLabel(self.confirmABookingScreen)
                self.confirm_txt.setGeometry(QtCore.QRect(210, 10, 241, 41))
                self.confirm_txt.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 24px;\n"
        "border: none;\n"
        "background-color: none;\n"
        "color: yellow;\n""")
                self.confirm_txt.setObjectName("confirm_txt")
                self.backBtn = QtWidgets.QPushButton(self.confirmABookingScreen,
                                                       clicked=lambda: self.back_clicked())
                self.backBtn.setGeometry(QtCore.QRect(540, 400, 91, 31))
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
                self.confirmNowBtn = QtWidgets.QPushButton(self.confirmABookingScreen,
                                                       clicked=lambda: self.confirmNow_clicked())
                self.confirmNowBtn.setGeometry(QtCore.QRect(340, 340, 131, 31))
                self.confirmNowBtn.setStyleSheet("background: blue;\n"
        "border: 2px solid rgb(255, 0, 127);\n"
        "box-sizing: border-box;\n"
        "border-radius: 10px;\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: white;")
                self.confirmNowBtn.setObjectName("confirmNowBtn")
                self.label = QtWidgets.QLabel(self.confirmABookingScreen)
                self.label.setGeometry(QtCore.QRect(0, 0, 651, 61))
                self.label.setStyleSheet("background-color: black;\n"
        "border-bottom: 2px solid black;")
                self.label.setText("")
                self.label.setObjectName("label")
                self.dateBookedLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.dateBookedLabel.setGeometry(QtCore.QRect(40, 290, 91, 21))
                self.dateBookedLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.dateBookedLabel.setObjectName("dateBookedLabel")
                self.dropOffAddresslLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.dropOffAddresslLabel.setGeometry(QtCore.QRect(340, 170, 121, 21))
                self.dropOffAddresslLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.dropOffAddresslLabel.setObjectName("dropOffAddresslLabel")
                self.pickUpDateLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.pickUpDateLabel.setGeometry(QtCore.QRect(340, 230, 91, 21))
                self.pickUpDateLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpDateLabel.setObjectName("pickUpDateLabel")
                self.pickUpAddressLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.pickUpAddressLabel.setGeometry(QtCore.QRect(340, 140, 111, 21))
                self.pickUpAddressLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpAddressLabel.setObjectName("pickUpAddressLabel")
                self.pickUpTimeLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.pickUpTimeLabel.setGeometry(QtCore.QRect(340, 200, 101, 21))
                self.pickUpTimeLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpTimeLabel.setObjectName("pickUpTimeLabel")
                self.driverIdLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.driverIdLineEdit.setGeometry(QtCore.QRect(140, 230, 151, 20))
                self.driverIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.driverIdLineEdit.setObjectName("driverIdLineEdit")
                self.adminIdLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.adminIdLineEdit.setGeometry(QtCore.QRect(140, 200, 151, 20))
                self.adminIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.adminIdLineEdit.setObjectName("adminIdLineEdit")
                self.blueBackground = QtWidgets.QLabel(self.confirmABookingScreen)
                self.blueBackground.setGeometry(QtCore.QRect(30, 130, 591, 261))
                self.blueBackground.setStyleSheet("border: 2px solid rgb(255, 0, 127);\n"
        "background-color: rgb(149, 200, 255);")
                self.blueBackground.setText("")
                self.blueBackground.setObjectName("blueBackground")
                self.confirmSlogan = QtWidgets.QLabel(self.confirmABookingScreen)
                self.confirmSlogan.setGeometry(QtCore.QRect(20, 60, 611, 71))
                self.confirmSlogan.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 15px;\n"
        "text-align: center;\n"
        "border: none;\n"
        "color: white;\n"
        "background-color: none;\n""")
                self.confirmSlogan.setObjectName("confirmSlogan")
                self.bookingStatusLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.bookingStatusLineEdit.setGeometry(QtCore.QRect(140, 260, 151, 20))
                self.bookingStatusLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.bookingStatusLineEdit.setObjectName("bookingStatusLineEdit")
                self.customerIdLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.customerIdLineEdit.setGeometry(QtCore.QRect(140, 170, 151, 20))
                self.customerIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.customerIdLineEdit.setObjectName("customerIdLineEdit")
                self.bookingIdLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.bookingIdLabel.setGeometry(QtCore.QRect(40, 140, 91, 21))
                self.bookingIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.bookingIdLabel.setObjectName("bookingIdLabel")
                self.bookingIdLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.bookingIdLineEdit.setGeometry(QtCore.QRect(140, 140, 151, 20))
                self.bookingIdLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.bookingIdLineEdit.setObjectName("bookingIdLineEdit")
                self.pickUpAddressLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.pickUpAddressLineEdit.setGeometry(QtCore.QRect(460, 140, 151, 20))
                self.pickUpAddressLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpAddressLineEdit.setObjectName("pickUpAddressLineEdit")
                self.dropOffAddressLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.dropOffAddressLineEdit.setGeometry(QtCore.QRect(460, 170, 151, 20))
                self.dropOffAddressLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dropOffAddressLineEdit.setObjectName("dropOffAddressLineEdit")
                self.dateBookedLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.dateBookedLineEdit.setGeometry(QtCore.QRect(140, 290, 151, 20))
                self.dateBookedLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dateBookedLineEdit.setObjectName("dateBookedLineEdit")
                self.pickUpTimeLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.pickUpTimeLineEdit.setGeometry(QtCore.QRect(460, 200, 151, 20))
                self.pickUpTimeLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpTimeLineEdit.setObjectName("pickUpTimeLineEdit")
                self.costOfTripLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.costOfTripLineEdit.setGeometry(QtCore.QRect(460, 260, 151, 20))
                self.costOfTripLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.costOfTripLineEdit.setObjectName("costOfTripLineEdit")
                self.pickUpDateLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.pickUpDateLineEdit.setGeometry(QtCore.QRect(460, 230, 151, 20))
                self.pickUpDateLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpDateLineEdit.setObjectName("pickUpDateLineEdit")
                self.paidLineEdit = QtWidgets.QLineEdit(self.confirmABookingScreen)
                self.paidLineEdit.setGeometry(QtCore.QRect(460, 290, 151, 20))
                self.paidLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.paidLineEdit.setObjectName("paidLineEdit")
                self.customerIdLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.customerIdLabel.setGeometry(QtCore.QRect(40, 170, 91, 21))
                self.customerIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.customerIdLabel.setObjectName("customerIdLabel")
                self.bookingStatusLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.bookingStatusLabel.setGeometry(QtCore.QRect(40, 260, 101, 21))
                self.bookingStatusLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.bookingStatusLabel.setObjectName("bookingStatusLabel")
                self.costOfTripLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.costOfTripLabel.setGeometry(QtCore.QRect(340, 260, 91, 21))
                self.costOfTripLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.costOfTripLabel.setObjectName("costOfTripLabel")
                self.driverIdLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.driverIdLabel.setGeometry(QtCore.QRect(40, 230, 71, 21))
                self.driverIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.driverIdLabel.setObjectName("driverIdLabel")
                self.adminIdLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.adminIdLabel.setGeometry(QtCore.QRect(40, 200, 71, 21))
                self.adminIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.adminIdLabel.setObjectName("adminIdLabel")
                self.paidLabel = QtWidgets.QLabel(self.confirmABookingScreen)
                self.paidLabel.setGeometry(QtCore.QRect(340, 290, 31, 21))
                self.paidLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.paidLabel.setObjectName("paidLabel")
                self.selectBookingBtn = QtWidgets.QPushButton(self.confirmABookingScreen,
                                                       clicked=lambda: self.selectBooking_clicked())
                self.selectBookingBtn.setGeometry(QtCore.QRect(190, 340, 131, 31))
                self.selectBookingBtn.setStyleSheet("background: blue;\n"
        "border: 2px solid rgb(255, 0, 127);\n"
        "box-sizing: border-box;\n"
        "border-radius: 10px;\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: white;")
                self.selectBookingBtn.setObjectName("selectBookingBtn")
                self.logo = QtWidgets.QLabel(self.confirmABookingScreen)
                self.logo.setGeometry(QtCore.QRect(40, 0, 61, 61))
                self.logo.setStyleSheet("background-color: none;\n"
        "border: none;\n"
        "padding: 3px 1px;")
                self.logo.setText("")
                self.logo.setPixmap(QtGui.QPixmap("../Sketch imgs/official-taxi-logo.png"))
                self.logo.setScaledContents(True)
                self.logo.setObjectName("logo")
                self.blueBackground.raise_()
                self.label.raise_()
                self.backBtn.raise_()
                self.confirmNowBtn.raise_()
                self.confirm_txt.raise_()
                self.dateBookedLabel.raise_()
                self.dropOffAddresslLabel.raise_()
                self.pickUpDateLabel.raise_()
                self.pickUpAddressLabel.raise_()
                self.pickUpTimeLabel.raise_()
                self.driverIdLineEdit.raise_()
                self.adminIdLineEdit.raise_()
                self.confirmSlogan.raise_()
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
                self.costOfTripLabel.raise_()
                self.driverIdLabel.raise_()
                self.adminIdLabel.raise_()
                self.paidLabel.raise_()
                self.selectBookingBtn.raise_()
                self.logo.raise_()

                self.retranslateUi(confirmBookingScreen_Dialog)
                QtCore.QMetaObject.connectSlotsByName(confirmBookingScreen_Dialog)

        def retranslateUi(self, confirmBookingScreen_Dialog):
                _translate = QtCore.QCoreApplication.translate
                confirmBookingScreen_Dialog.setWindowTitle(_translate("confirmBookingScreen_Dialog", "Dialog"))
                self.confirm_txt.setText(_translate("confirmBookingScreen_Dialog", "CONFIRM BOOKING"))
                self.backBtn.setText(_translate("confirmBookingScreen_Dialog", "BACK"))
                self.confirmNowBtn.setText(_translate("confirmBookingScreen_Dialog", "CONFIRM NOW"))
                self.dateBookedLabel.setText(_translate("confirmBookingScreen_Dialog", "Date Booked"))
                self.dropOffAddresslLabel.setText(_translate("confirmBookingScreen_Dialog", "Drop Off Address"))
                self.pickUpDateLabel.setText(_translate("confirmBookingScreen_Dialog", "Pick Up Date"))
                self.pickUpAddressLabel.setText(_translate("confirmBookingScreen_Dialog", "Pick Up Address"))
                self.pickUpTimeLabel.setText(_translate("confirmBookingScreen_Dialog", "Pick Up Time"))
                self.confirmSlogan.setText(_translate("confirmBookingScreen_Dialog",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">"
                "To Confirm a Booking, enter the Booking ID for the Booking you want to Confirm,<br/>then click "
                "the Select Booking button, then proceed to make the neccessary<br/>changes then click Confirm Now."
                " </span></p></body></html>"))
                self.bookingIdLabel.setText(_translate("confirmBookingScreen_Dialog", "Booking ID"))
                self.customerIdLabel.setText(_translate("confirmBookingScreen_Dialog", "Customer ID"))
                self.bookingStatusLabel.setText(_translate("confirmBookingScreen_Dialog", "Booking Status"))
                self.costOfTripLabel.setText(_translate("confirmBookingScreen_Dialog", "Cost of Trip"))
                self.driverIdLabel.setText(_translate("confirmBookingScreen_Dialog", "Driver ID"))
                self.adminIdLabel.setText(_translate("confirmBookingScreen_Dialog", "Admin ID"))
                self.paidLabel.setText(_translate("confirmBookingScreen_Dialog", "Paid"))
                self.selectBookingBtn.setText(_translate("confirmBookingScreen_Dialog", "SELECT BOOKING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmBookingScreen_Dialog = QtWidgets.QDialog()
    ui = Ui_confirmBookingScreen_Dialog()
    ui.confirmBookingScreen_setupUi(confirmBookingScreen_Dialog)
    confirmBookingScreen_Dialog.show()
    sys.exit(app.exec_())
