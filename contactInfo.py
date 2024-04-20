# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import homePage



class Ui_contactInfoScreen_Dialog(object):
    def __init__(self, Dialog):
                self.Dialog = QtWidgets.QDialog()
                self.contactInfoScreen_setupUi(self.Dialog)

    def its_showtime(self):
                self.Dialog.show()

    def its_closetime(self):
                self.Dialog.close()

    def contactInfoBack_clicked(self):
                self.dialog = QtWidgets.QDialog()
                hP = homePage.Ui_homeScreen_Dialog(self.dialog)
                hP.its_showtime()
                self.its_closetime()
    def contactInfoScreen_setupUi(self, contactInfoScreen_Dialog):
        contactInfoScreen_Dialog.setObjectName("contactInfoScreen_Dialog")
        contactInfoScreen_Dialog.resize(671, 460)
        self.contactInfoScreen = QtWidgets.QWidget(contactInfoScreen_Dialog)
        self.contactInfoScreen.setGeometry(QtCore.QRect(10, 10, 651, 441))
        self.contactInfoScreen.setStyleSheet("border: 8px solid black;\n"
    "background-color: rgb(123, 125, 255);\n""")
        self.contactInfoScreen.setObjectName("contactInfoScreen")
        self.contactInfo_txt = QtWidgets.QLabel(self.contactInfoScreen)
        self.contactInfo_txt.setGeometry(QtCore.QRect(250, 20, 161, 21))
        self.contactInfo_txt.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 24px;\n"
    "border: none;\n"
    "background-color: none;\n"
    "color: yellow;")
        self.contactInfo_txt.setObjectName("contactInfo_txt")
        self.address_label = QtWidgets.QLabel(self.contactInfoScreen)
        self.address_label.setGeometry(QtCore.QRect(430, 180, 71, 16))
        self.address_label.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 14px;\n"
    "text-align: center;\n"
    "color: #000000;\n"
    "border: none;\n"
    "background-color: none;")
        self.address_label.setObjectName("address_label")
        self.email_label = QtWidgets.QLabel(self.contactInfoScreen)
        self.email_label.setGeometry(QtCore.QRect(430, 260, 191, 21))
        self.email_label.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 14px;\n"
    "text-align: center;\n"
    "color: #000000;\n"
    "border: none;\n"
    "background-color: none;")
        self.email_label.setObjectName("email_label")
        self.contactInfoBackBtn = QtWidgets.QPushButton(self.contactInfoScreen,
                                                      clicked=lambda: self.contactInfoBack_clicked())
        self.contactInfoBackBtn.setGeometry(QtCore.QRect(540, 400, 91, 31))
        self.contactInfoBackBtn.setStyleSheet("background: red;\n"
    "border: 3px solid blue;\n"
    "box-sizing: border-box;\n"
    "border-radius: 15px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 13px;\n"
    "text-align: center;\n"
    "color: white;")
        self.contactInfoBackBtn.setObjectName("contactInfoBackBtn")
        self.label = QtWidgets.QLabel(self.contactInfoScreen)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 61))
        self.label.setStyleSheet("background-color: balck;\n"
    "border-bottom: 2px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.contactNo_label = QtWidgets.QLabel(self.contactInfoScreen)
        self.contactNo_label.setGeometry(QtCore.QRect(430, 220, 121, 16))
        self.contactNo_label.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 14px;\n"
    "text-align: center;\n"
    "color: #000000;\n"
    "border: none;\n"
    "background-color: none;")
        self.contactNo_label.setObjectName("contactNo_label")
        self.location_icon = QtWidgets.QLabel(self.contactInfoScreen)
        self.location_icon.setGeometry(QtCore.QRect(390, 180, 21, 21))
        self.location_icon.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.location_icon.setText("")
        self.location_icon.setPixmap(QtGui.QPixmap("../Sketch imgs/location.png"))
        self.location_icon.setScaledContents(True)
        self.location_icon.setObjectName("location_icon")
        self.phone_icon = QtWidgets.QLabel(self.contactInfoScreen)
        self.phone_icon.setGeometry(QtCore.QRect(390, 220, 21, 21))
        self.phone_icon.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.phone_icon.setText("")
        self.phone_icon.setPixmap(QtGui.QPixmap("../Sketch imgs/phone.png"))
        self.phone_icon.setScaledContents(True)
        self.phone_icon.setObjectName("phone_icon")
        self.email_icon = QtWidgets.QLabel(self.contactInfoScreen)
        self.email_icon.setGeometry(QtCore.QRect(390, 260, 21, 21))
        self.email_icon.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.email_icon.setText("")
        self.email_icon.setPixmap(QtGui.QPixmap("../Sketch imgs/email.png"))
        self.email_icon.setScaledContents(True)
        self.email_icon.setObjectName("email_icon")
        self.heart = QtWidgets.QLabel(self.contactInfoScreen)
        self.heart.setGeometry(QtCore.QRect(320, 80, 21, 21))
        self.heart.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.heart.setText("")
        self.heart.setPixmap(QtGui.QPixmap("../Sketch imgs/heart1.png"))
        self.heart.setScaledContents(True)
        self.heart.setObjectName("heart")
        self.twitter_icon = QtWidgets.QLabel(self.contactInfoScreen)
        self.twitter_icon.setGeometry(QtCore.QRect(440, 350, 21, 21))
        self.twitter_icon.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.twitter_icon.setText("")
        self.twitter_icon.setPixmap(QtGui.QPixmap("../Sketch imgs/twitter.png"))
        self.twitter_icon.setScaledContents(True)
        self.twitter_icon.setObjectName("twitter_icon")
        self.gmail_icon = QtWidgets.QLabel(self.contactInfoScreen)
        self.gmail_icon.setGeometry(QtCore.QRect(470, 350, 21, 21))
        self.gmail_icon.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.gmail_icon.setText("")
        self.gmail_icon.setPixmap(QtGui.QPixmap("../Sketch imgs/gmail.png"))
        self.gmail_icon.setScaledContents(True)
        self.gmail_icon.setObjectName("gmail_icon")
        self.instagram_icon = QtWidgets.QLabel(self.contactInfoScreen)
        self.instagram_icon.setGeometry(QtCore.QRect(500, 350, 21, 21))
        self.instagram_icon.setStyleSheet("background-color: none;\n"
    "border: none;")
        self.instagram_icon.setText("")
        self.instagram_icon.setPixmap(QtGui.QPixmap("../Sketch imgs/ig.png"))
        self.instagram_icon.setScaledContents(True)
        self.instagram_icon.setObjectName("instagram_icon")
        self.logo = QtWidgets.QLabel(self.contactInfoScreen)
        self.logo.setGeometry(QtCore.QRect(40, 0, 61, 61))
        self.logo.setStyleSheet("background-color: none;\n"
    "border: none;\n"
    "padding: 3px 1px;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Sketch imgs/official-taxi-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.nameLineEdit = QtWidgets.QLineEdit(self.contactInfoScreen)
        self.nameLineEdit.setGeometry(QtCore.QRect(30, 170, 281, 31))
        self.nameLineEdit.setStyleSheet("border: 1px solid blue;\n"
    "background-color: white;\n"
    "color: grey;\n"
    "padding: 5px;")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.messageLineEdit = QtWidgets.QLineEdit(self.contactInfoScreen)
        self.messageLineEdit.setGeometry(QtCore.QRect(30, 250, 281, 91))
        self.messageLineEdit.setStyleSheet("border: 1px solid blue;\n"
    "background-color: white;\n"
    "color: grey;\n"
    "padding: 5px;")
        self.messageLineEdit.setObjectName("messageLineEdit")
        self.emailLineEdit = QtWidgets.QLineEdit(self.contactInfoScreen)
        self.emailLineEdit.setGeometry(QtCore.QRect(30, 210, 281, 31))
        self.emailLineEdit.setStyleSheet("border: 1px solid blue;\n"
    "background-color: white;\n"
    "color: grey;\n"
    "padding: 5px;")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.sendBtn = QtWidgets.QPushButton(self.contactInfoScreen)
        self.sendBtn.setGeometry(QtCore.QRect(130, 350, 91, 31))
        self.sendBtn.setStyleSheet("background-color: rgb(255, 0, 127);\n"
    "border: 3px solid #0029FF;\n"
    "box-sizing: border-box;\n"
    "border-radius: 15px;\n"
    "font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 12px;\n"
    "text-align: center;\n"
    "color: white;")
        self.sendBtn.setObjectName("sendBtn")
        self.label_2 = QtWidgets.QLabel(self.contactInfoScreen)
        self.label_2.setGeometry(QtCore.QRect(230, 80, 91, 16))
        self.label_2.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 17px;\n"
    "text-align: center;\n"
    "border: none;\n"
    "color: white;\n"
    "background-color:none;")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.contactInfoScreen)
        self.label_7.setGeometry(QtCore.QRect(350, 80, 71, 16))
        self.label_7.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 17px;\n"
    "text-align: center;\n"
    "border: none;\n"
    "color: white;\n"
    "background-color:none;")
        self.label_7.setObjectName("label_7")
        self.slogan = QtWidgets.QLabel(self.contactInfoScreen)
        self.slogan.setGeometry(QtCore.QRect(80, 110, 501, 16))
        self.slogan.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 14px;\n"
    "text-align: center;\n"
    "border: none;\n"
    "color: white;\n"
    "background-color:none;\n""")
        self.slogan.setObjectName("slogan")
        self.label_13 = QtWidgets.QLabel(self.contactInfoScreen)
        self.label_13.setGeometry(QtCore.QRect(20, 160, 611, 231))
        self.label_13.setStyleSheet("background-color: none;\n"
    "border: 3px solid rgb(255, 0, 127);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.slogan1 = QtWidgets.QLabel(self.contactInfoScreen)
        self.slogan1.setGeometry(QtCore.QRect(350, 310, 251, 31))
        self.slogan1.setStyleSheet("font-family: Roboto;\n"
    "font-style: normal;\n"
    "font-weight: 900;\n"
    "font-size: 13px;\n"
    "text-align: center;\n"
    "border: none;\n"
    "color: rgb(0, 0, 127);\n"
    "background-color:none;\n""")
        self.slogan1.setObjectName("slogan1")
        self.label_13.raise_()
        self.label.raise_()
        self.contactInfo_txt.raise_()
        self.address_label.raise_()
        self.email_label.raise_()
        self.contactInfoBackBtn.raise_()
        self.contactNo_label.raise_()
        self.location_icon.raise_()
        self.phone_icon.raise_()
        self.email_icon.raise_()
        self.heart.raise_()
        self.twitter_icon.raise_()
        self.gmail_icon.raise_()
        self.instagram_icon.raise_()
        self.logo.raise_()
        self.nameLineEdit.raise_()
        self.messageLineEdit.raise_()
        self.emailLineEdit.raise_()
        self.sendBtn.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.slogan.raise_()
        self.slogan1.raise_()

        self.retranslateUi(contactInfoScreen_Dialog)
        QtCore.QMetaObject.connectSlotsByName(contactInfoScreen_Dialog)

    def retranslateUi(self, contactInfoScreen_Dialog):
        _translate = QtCore.QCoreApplication.translate
        contactInfoScreen_Dialog.setWindowTitle(_translate("contactInfoScreen_Dialog", "Dialog"))
        self.contactInfo_txt.setText(_translate("contactInfoScreen_Dialog", "CONTACT US"))
        self.address_label.setText(_translate("contactInfoScreen_Dialog", " Online"))
        self.email_label.setText(_translate("contactInfoScreen_Dialog", " HotelCompany@gmail.com"))
        self.contactInfoBackBtn.setText(_translate("contactInfoScreen_Dialog", "BACK"))
        self.contactNo_label.setText(_translate("contactInfoScreen_Dialog", " 1-868-472-7323"))
        self.nameLineEdit.setText(_translate("contactInfoScreen_Dialog", "Your name"))
        self.messageLineEdit.setText(_translate("contactInfoScreen_Dialog", "Message"))
        self.emailLineEdit.setText(_translate("contactInfoScreen_Dialog", "Email"))
        self.sendBtn.setText(_translate("contactInfoScreen_Dialog", "SEND"))
        self.label_2.setText(_translate("contactInfoScreen_Dialog", "We would"))
        self.label_7.setText(_translate("contactInfoScreen_Dialog", "to help!"))
        self.slogan.setText(_translate("contactInfoScreen_Dialog",
        "We like to create with fun, open minded people. Feel free so say Hello!"))
        self.slogan1.setText(_translate("contactInfoScreen_Dialog",
         "<html><head/><body><p align=\"center\">Feel free to conatct us on all platforms <br/>@HotelCompany"
         "</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    contactInfoScreen_Dialog = QtWidgets.QDialog()
    ui = Ui_contactInfoScreen_Dialog()
    ui.contactInfoScreen_setupUi(contactInfoScreen_Dialog)
    contactInfoScreen_Dialog.show()
    sys.exit(app.exec_())
