# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lesson5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(20, 20, 351, 451))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("img/beagle.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.beagle = QtWidgets.QPushButton(self.centralwidget)
        self.beagle.setGeometry(QtCore.QRect(40, 490, 112, 34))
        self.beagle.setObjectName("beagle")
        self.doggo = QtWidgets.QPushButton(self.centralwidget)
        self.doggo.setGeometry(QtCore.QRect(230, 490, 112, 34))
        self.doggo.setObjectName("doggo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.beagle.clicked.connect(self.show_beagle)
        self.doggo.clicked.connect(self.show_doggo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.beagle.setText(_translate("MainWindow", "Beagle"))
        self.doggo.setText(_translate("MainWindow", "Doggos"))

    def show_beagle(self):
        self.photo.setPixmap(QtGui.QPixmap("img/beagle.jpg"))
    
    def show_doggo(self):
        self.photo.setPixmap(QtGui.QPixmap("img/doggo.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

