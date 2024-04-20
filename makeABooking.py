# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'makeABooking.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from PyQt5.QtWidgets import QMessageBox
import customerServices

#conn = sqlite3.connect(':memory:') # testing in memory
conn = sqlite3.connect('taxi.db')  # creates the actual database
c = conn.cursor()   # The cursor to take data to and from the database.
c.execute("""CREATE TABLE if not exists Booking (
                   bookingId INTEGER NOT NULL PRIMARY KEY,
                   customerId INTEGER NOT NULL,
                   adminId INTEGER  NULL,
                   driverId INTEGER NULL,
                   bookingStatus text NULL DEFAULT 'Pending',
                   dateBooked text NOT NULL, 
                   pickUpAddress text NOT NULL, 
                   dropOffAddress text NOT NULL, 
                   pickUpTime text NOT NULL, 
                   pickUpDate text NOT NULL,
                   costOfTrip text,
                   paid text NULL,
                   FOREIGN KEY (customerId) REFERENCES Customer (customerId),
                   FOREIGN KEY (adminId) REFERENCES Admin (adminId),
                   FOREIGN KEY (driverId) REFERENCES Driver (driverId)     
                   )""")      # creates the table associated with the text field aka line edits

class Ui_makeBookingScreen_Dialog(object):

        def __init__(self, Dialog):      # creation of a constructor
                self.Dialog = QtWidgets.QDialog()      # this class has one attribute
                self.makeBookingScreen_setupUi(self.Dialog)     # attribute is need to setup the ui

        def its_showtime(self):   # used to show the dialog
                self.Dialog.show()

        def its_closetime(self):    # used to close the dialog
                self.Dialog.close()

        def back_button_click(self):    # goes back to the Customer Services Screen
                self.dialog = QtWidgets.QDialog()
                cS = customerServices.Ui_CustomerPortal(self.dialog)
                cS.its_showtime()
                self.its_closetime()

        def get_customerID(self):
            c.execute("SELECT * FROM Customer WHERE customerId=:customerId",  # Gets the CustomerID from the Customer table.
                      {'customerId': self.customerLineEdit.text(),
                       'email': self.getEmailAddressLineEdit.text()})
            return c.fetchall()  # returns the record from the database

        def bookNow_button_click(self):   #Buttoon to make a Booking.
            if self.customerLineEdit.text() and \
               self.customerLineEdit.text() in self.get_customerID().__str__():
                self.insert_record()   # inserts the user data
                conn.commit()      # commits the data to the database
                conn.close()       # closes the database connection
                self.disable_fields_and_Buttons()    # function that disables fields and button.
                self.showdialog("Congratulations, your booking was successfully created!")
            else:
                self.showdialog("Customer ID entered does not match any CustomerId in the Customer table.")

        def insert_record(self):
                with conn:
                        c.execute(
                                "INSERT INTO Booking VALUES (:bookingId, :customerId, '', '', 'Pending',  "
                                ":dateBooked,"" :pickUpAddress, :dropOffAddress, :pickUpTime, :pickUpDate, '', '')",
                                {'bookingId': self.bookingIdNoLabel.text(),
                                 'customerId': self.customerLineEdit.text(),
                                 'dateBooked': self.dateBookedLineEdit.text(),
                                 'pickUpAddress': self.PickUpAddressLineEdit.text(),
                                 'dropOffAddress': self.dropOffAddressLineEdit.text(),
                                 'pickUpTime': self.pickUpTimeLineEdit.text(),
                                 'pickUpDate': self.pickUpDateLineEdit.text()})

        def get_customerID_Verification(self):
                c.execute("SELECT * FROM Customer WHERE email=:email",  #Gets the email from the customer table.
                          {'email': self.getEmailAddressLineEdit.text(),
                          'customerId': self.customerLineEdit.text()})
                return c.fetchall()  # returns the record from the database

        def viewall(self):
                if self.getEmailAddressLineEdit.text() and \
                   self.getEmailAddressLineEdit.text() in self.get_customerID_Verification().__str__():
                 List = self.get_customerID_Verification()
                 self.showdialog("Congratulations, your CustomerID was successfully found, you may now view your Customer ID!")
                 self.getEmailAddressLineEdit.setEnabled(False)
                 self.bookNowBtn_2.setEnabled(False)
                 self.getCustomerIdLineEdit.setText(str(List[0][0]))
                else:
                     self.wrongCustomerID("Sorry, your Email was not found in the Customer table.")


        def disable_fields_and_Buttons(self):
                self.customerLineEdit.setEnabled(False)        # disable the customer field
                self.dateBookedLineEdit.setEnabled(False)   # disable the datebooked field
                self.PickUpAddressLineEdit.setEnabled(False)   # disable the PickUpAddress field
                self.dropOffAddressLineEdit.setEnabled(False)  # disable the dropOffAddress field
                self.pickUpTimeLineEdit.setEnabled(False)   # disable the pickUpTime field
                self.pickUpDateLineEdit.setEnabled(False)   # disable the pickUpDate field
                self.bookNowBtn.setEnabled(False)    # disable the bookNowBtn

        def wrongCustomerID(self, message):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Invalid Email.")
                msg.setInformativeText(message)
                msg.setWindowTitle("Notification")
                msg.setDetailedText("The details are as follows:" + message)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()

        def showdialog(self, message):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Please Note!")
                msg.setInformativeText(message)
                msg.setWindowTitle("Confirmation")
                msg.setDetailedText("The details are as follows:" + message)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()

        def makeBookingScreen_setupUi(self, makeBookingScreen_Dialog):
                makeBookingScreen_Dialog.setObjectName("makeBookingScreen_Dialog")
                makeBookingScreen_Dialog.resize(671, 460)
                self.makeABookingScreen = QtWidgets.QWidget(makeBookingScreen_Dialog)
                self.makeABookingScreen.setGeometry(QtCore.QRect(10, 10, 651, 441))
                self.makeABookingScreen.setStyleSheet("border: 8px solid black;\n"
        "background-color:qlineargradient(spread:pad, x1:0.0511364, y1:1, x2:0, y2:0, "
        "stop:0 rgba(251, 255, 0, 255), stop:0.98 rgba(0, 61, 255, 255), stop:1 rgba(0, 0, 0, 0));\n""")
                self.makeABookingScreen.setObjectName("makeABookingScreen")
                self.make_txt = QtWidgets.QLabel(self.makeABookingScreen)
                self.make_txt.setGeometry(QtCore.QRect(220, 10, 221, 51))
                self.make_txt.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 24px;\n"
        "border: none;\n"
        "background-color: none;\n"
        "color: yellow;\n""")
                self.make_txt.setObjectName("make_txt")
                self.backBtn = QtWidgets.QPushButton(self.makeABookingScreen,
                                                     clicked=lambda: self.back_button_click())
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
                self.bookNowBtn = QtWidgets.QPushButton(self.makeABookingScreen,
                                                        clicked=lambda: self.bookNow_button_click())
                self.bookNowBtn.setGeometry(QtCore.QRect(170, 340, 141, 31))
                self.bookNowBtn.setStyleSheet("background: blue;\n"
        "border: 2px solid rgb(255, 0, 127);\n"
        "box-sizing: border-box;\n"
        "border-radius: 10px;\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: white;")
                self.bookNowBtn.setObjectName("bookNowBtn")
                self.label = QtWidgets.QLabel(self.makeABookingScreen)
                self.label.setGeometry(QtCore.QRect(0, 0, 651, 71))
                self.label.setStyleSheet("background-color: black;\n"
        "border-bottom: 2px solid black;")
                self.label.setText("")
                self.label.setObjectName("label")
                self.dateBookedLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.dateBookedLabel.setGeometry(QtCore.QRect(40, 270, 91, 21))
                self.dateBookedLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.dateBookedLabel.setObjectName("dateBookedLabel")
                self.dropOffAddresslLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.dropOffAddresslLabel.setGeometry(QtCore.QRect(330, 240, 131, 21))
                self.dropOffAddresslLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.dropOffAddresslLabel.setObjectName("dropOffAddresslLabel")
                self.pickUpDateLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.pickUpDateLabel.setGeometry(QtCore.QRect(330, 300, 91, 21))
                self.pickUpDateLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpDateLabel.setObjectName("pickUpDateLabel")
                self.pickUpAddressLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.pickUpAddressLabel.setGeometry(QtCore.QRect(40, 300, 121, 21))
                self.pickUpAddressLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpAddressLabel.setObjectName("pickUpAddressLabel")
                self.pickUpTimeLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.pickUpTimeLabel.setGeometry(QtCore.QRect(330, 270, 101, 21))
                self.pickUpTimeLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.pickUpTimeLabel.setObjectName("pickUpTimeLabel")
                self.dropOffAddressLineEdit = QtWidgets.QLineEdit(self.makeABookingScreen)
                self.dropOffAddressLineEdit.setGeometry(QtCore.QRect(450, 240, 161, 20))
                self.dropOffAddressLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dropOffAddressLineEdit.setObjectName("dropOffAddressLineEdit")
                self.PickUpAddressLineEdit = QtWidgets.QLineEdit(self.makeABookingScreen)
                self.PickUpAddressLineEdit.setGeometry(QtCore.QRect(150, 300, 161, 20))
                self.PickUpAddressLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.PickUpAddressLineEdit.setObjectName("PickUpAddressLineEdit")
                self.label_11 = QtWidgets.QLabel(self.makeABookingScreen)
                self.label_11.setGeometry(QtCore.QRect(30, 120, 591, 261))
                self.label_11.setStyleSheet("border: 2px solid rgb(255, 0, 127);\n"
        "background-color: rgb(149, 200, 255);")
                self.label_11.setText("")
                self.label_11.setObjectName("label_11")
                self.makeSlogan = QtWidgets.QLabel(self.makeABookingScreen)
                self.makeSlogan.setGeometry(QtCore.QRect(120, 79, 411, 31))
                self.makeSlogan.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 15px;\n"
        "text-align: center;\n"
        "border: none;\n"
        "color:white;\n"
        "background-color: none;\n""")
                self.makeSlogan.setObjectName("makeSlogan")
                self.pickUpTimeLineEdit = QtWidgets.QTimeEdit(self.makeABookingScreen)
                self.pickUpTimeLineEdit.setGeometry(QtCore.QRect(450, 270, 161, 22))
                self.pickUpTimeLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpTimeLineEdit.setObjectName("pickUpTimeLineEdit")
                self.pickUpDateLineEdit = QtWidgets.QDateEdit(self.makeABookingScreen)
                self.pickUpDateLineEdit.setGeometry(QtCore.QRect(450, 300, 161, 22))
                self.pickUpDateLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.pickUpDateLineEdit.setObjectName("pickUpDateLineEdit")
                self.dateBookedLineEdit = QtWidgets.QDateEdit(self.makeABookingScreen)
                self.dateBookedLineEdit.setGeometry(QtCore.QRect(150, 270, 161, 22))
                self.dateBookedLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.dateBookedLineEdit.setObjectName("dateBookedLineEdit")
                self.bookingIdLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.bookingIdLabel.setGeometry(QtCore.QRect(50, 190, 91, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(-1)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(62)
                self.bookingIdLabel.setFont(font)
                self.bookingIdLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.bookingIdLabel.setObjectName("bookingIdLabel")
                self.bookingIdNoLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.bookingIdNoLabel.setGeometry(QtCore.QRect(140, 190, 41, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(-1)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(62)
                self.bookingIdNoLabel.setFont(font)
                self.bookingIdNoLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.bookingIdNoLabel.setObjectName("bookingIdNoLabel")
                self.label_2 = QtWidgets.QLabel(self.makeABookingScreen)
                self.label_2.setGeometry(QtCore.QRect(40, 180, 151, 41))
                self.label_2.setStyleSheet("background-color: rgb(255, 0, 127);\n"
        "border: 2px solid yellow;")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.customerLineEdit = QtWidgets.QLineEdit(self.makeABookingScreen)
                self.customerLineEdit.setGeometry(QtCore.QRect(150, 240, 161, 20))
                self.customerLineEdit.setStyleSheet("background: #C4C4C4;\n"
        "border: 1px solid blue;")
                self.customerLineEdit.setObjectName("customerLineEdit")
                self.emailAddressLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.emailAddressLabel.setGeometry(QtCore.QRect(40, 240, 101, 21))
                self.emailAddressLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.emailAddressLabel.setObjectName("emailAddressLabel")
                self.logo = QtWidgets.QLabel(self.makeABookingScreen)
                self.logo.setGeometry(QtCore.QRect(40, 10, 51, 51))
                self.logo.setStyleSheet("background-color: none;\n"
        "border: none;")
                self.logo.setText("")
                self.logo.setPixmap(QtGui.QPixmap("../Sketch imgs/official-taxi-logo.png"))
                self.logo.setScaledContents(True)
                self.logo.setObjectName("logo")
                self.logo_2 = QtWidgets.QLabel(self.makeABookingScreen)
                self.logo_2.setGeometry(QtCore.QRect(20, 390, 101, 41))
                self.logo_2.setStyleSheet("background-color: none;\n"
        "border: none;")
                self.logo_2.setText("")
                self.logo_2.setPixmap(QtGui.QPixmap("../Sketch imgs/makeABooking.png"))
                self.logo_2.setScaledContents(True)
                self.logo_2.setObjectName("logo_2")
                self.makeInstruction = QtWidgets.QLabel(self.makeABookingScreen)
                self.makeInstruction.setGeometry(QtCore.QRect(60, 120, 531, 51))
                self.makeInstruction.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: 900;\n"
        "font-size: 15px;\n"
        "text-align: center;\n"
        "border: none;\n"
        "color:black;\n"
        "background-color: none;\n""")
                self.makeInstruction.setObjectName("makeInstruction")
                self.getCustomerIDLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.getCustomerIDLabel.setGeometry(QtCore.QRect(440, 190, 91, 16))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(-1)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(62)
                self.getCustomerIDLabel.setFont(font)
                self.getCustomerIDLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.getCustomerIDLabel.setObjectName("getCustomerIDLabel")
                self.getCustomerIdLineEdit = QtWidgets.QLineEdit(self.makeABookingScreen)
                self.getCustomerIdLineEdit.setGeometry(QtCore.QRect(540, 190, 61, 21))
                self.getCustomerIdLineEdit.setStyleSheet("background: rgb(255, 170, 255);\n"
        "border: 1.5px solid red;\n""")
                self.getCustomerIdLineEdit.setObjectName("getCustomerIdLineEdit")
                self.getCustomerIdLineEdit.setEnabled(False)
                self.getEmailLabel = QtWidgets.QLabel(self.makeABookingScreen)
                self.getEmailLabel.setGeometry(QtCore.QRect(260, 190, 41, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(-1)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(62)
                self.getEmailLabel.setFont(font)
                self.getEmailLabel.setStyleSheet("font-family: Roboto;\n"
        "font-style:normal;\n"
        "font-weight:500;\n"
        "font-size: 14px;\n"
        "text-align: center;\n"
        "color: #000000;\n"
        "border: none;\n"
        "background-color: none;")
                self.getEmailLabel.setObjectName("getEmailLabel")
                self.getEmailAddressLineEdit = QtWidgets.QLineEdit(self.makeABookingScreen)
                self.getEmailAddressLineEdit.setGeometry(QtCore.QRect(310, 190, 121, 21))
                self.getEmailAddressLineEdit.setStyleSheet("background: rgb(255, 170, 255);\n"
        "border: 1.5px solid red;\n""")
                self.getEmailAddressLineEdit.setText("")
                self.getEmailAddressLineEdit.setObjectName("getEmailAddressLineEdit")
                self.label_3 = QtWidgets.QLabel(self.makeABookingScreen)
                self.label_3.setGeometry(QtCore.QRect(250, 180, 361, 41))
                self.label_3.setStyleSheet("background-color: rgb(255, 0, 127);\n"
        "border: 2px solid yellow;")
                self.label_3.setText("")
                self.label_3.setObjectName("label_3")
                self.bookNowBtn_2 = QtWidgets.QPushButton(self.makeABookingScreen,
                                                clicked=lambda: self.viewall())
                self.bookNowBtn_2.setGeometry(QtCore.QRect(330, 340, 141, 31))
                self.bookNowBtn_2.setStyleSheet("background: blue;\n"
        "border: 2px solid rgb(255, 0, 127);\n"
        "box-sizing: border-box;\n"
        "border-radius: 10px;\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight:500;\n"
        "font-size: 13px;\n"
        "text-align: center;\n"
        "color: white;")
                self.bookNowBtn_2.setObjectName("bookNowBtn_2")
                self.label_11.raise_()
                self.label_3.raise_()
                self.dateBookedLineEdit.raise_()
                self.label_2.raise_()
                self.label.raise_()
                self.backBtn.raise_()
                self.bookNowBtn.raise_()
                self.make_txt.raise_()
                self.dateBookedLabel.raise_()
                self.dropOffAddresslLabel.raise_()
                self.pickUpDateLabel.raise_()
                self.pickUpAddressLabel.raise_()
                self.pickUpTimeLabel.raise_()
                self.dropOffAddressLineEdit.raise_()
                self.PickUpAddressLineEdit.raise_()
                self.makeSlogan.raise_()
                self.pickUpTimeLineEdit.raise_()
                self.pickUpDateLineEdit.raise_()
                self.bookingIdLabel.raise_()
                self.bookingIdNoLabel.raise_()
                self.customerLineEdit.raise_()
                self.emailAddressLabel.raise_()
                self.logo.raise_()
                self.logo_2.raise_()
                self.makeInstruction.raise_()
                self.getCustomerIDLabel.raise_()
                self.getCustomerIdLineEdit.raise_()
                self.getEmailLabel.raise_()
                self.getEmailAddressLineEdit.raise_()
                self.bookNowBtn_2.raise_()

                self.retranslateUi(makeBookingScreen_Dialog)
                QtCore.QMetaObject.connectSlotsByName(makeBookingScreen_Dialog)

        def retranslateUi(self, makeBookingScreen_Dialog):
                _translate = QtCore.QCoreApplication.translate
                makeBookingScreen_Dialog.setWindowTitle(_translate("makeBookingScreen_Dialog", "Dialog"))
                self.make_txt.setText(_translate("makeBookingScreen_Dialog", "MAKE A BOOKING"))
                self.backBtn.setText(_translate("makeBookingScreen_Dialog", "BACK"))
                self.bookNowBtn.setText(_translate("makeBookingScreen_Dialog", "BOOK NOW"))
                self.dateBookedLabel.setText(_translate("makeBookingScreen_Dialog", "Date Booked"))
                self.dropOffAddresslLabel.setText(_translate("makeBookingScreen_Dialog", "Drop Off Address"))
                self.pickUpDateLabel.setText(_translate("makeBookingScreen_Dialog", "Pick Up Date"))
                self.pickUpAddressLabel.setText(_translate("makeBookingScreen_Dialog", "Pick Up Address"))
                self.pickUpTimeLabel.setText(_translate("makeBookingScreen_Dialog", "Pick Up Time"))
                self.makeSlogan.setText(_translate("makeBookingScreen_Dialog",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Book Now &amp; Travel "
                " Securely With Us. AVAILABLE 24/7</span></p></body></html>"))
                self.bookingIdLabel.setToolTip(_translate("makeBookingScreen_Dialog", "Trip ID is Auto Generated"))
                self.bookingIdLabel.setText(_translate("makeBookingScreen_Dialog", "Booking ID :"))
                #self.bookingIdNoLabel.setText(_translate("makeBookingScreen_Dialog", "0000"))
                self.bookingIdNoLabel.setText(_translate("makeBookingScreen_Dialog", str(random.randint(1, 10000))))
                self.emailAddressLabel.setText(_translate("makeBookingScreen_Dialog", "Customer ID"))
                self.makeInstruction.setText(_translate("makeBookingScreen_Dialog",
                 "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">To get your CustomeID "
                 "enter your Email and click the Get CustomerID button. To<br/>  Make a booking, fill out the form "
                 "then click the Book Now button. </span></p></body></html>"))
                self.getCustomerIDLabel.setToolTip(_translate("makeBookingScreen_Dialog", "Trip ID is Auto Generated"))
                self.getCustomerIDLabel.setText(_translate("makeBookingScreen_Dialog", "Customer ID"))
                self.getEmailLabel.setToolTip(_translate("makeBookingScreen_Dialog", "Trip ID is Auto Generated"))
                self.getEmailLabel.setText(_translate("makeBookingScreen_Dialog", "Email "))
                self.bookNowBtn_2.setText(_translate("makeBookingScreen_Dialog", "GET CUSTOMER ID"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    makeBookingScreen_Dialog = QtWidgets.QDialog()
    ui = Ui_makeBookingScreen_Dialog()
    ui.makeBookingScreen_setupUi(makeBookingScreen_Dialog)
    makeBookingScreen_Dialog.show()
    sys.exit(app.exec_())
