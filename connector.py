import sys

from PyQt5 import QtWidgets

import homePage

app = QtWidgets.QApplication(sys.argv)
homeScreen_Dialog = QtWidgets.QDialog()
hP = homePage.Ui_homeScreen_Dialog(QtWidgets.QDialog())
hP.its_showtime()
sys.exit(app.exec_())