# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../pyqt_ui/sub_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("SubWindow")
        SubWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.textLabel.setObjectName("textLabel")
        SubWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SubWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        SubWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SubWindow)
        self.statusbar.setObjectName("statusbar")
        SubWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubWindow)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

    def retranslateUi(self, SubWindow):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("SubWindow", "MainWindow"))
        self.textLabel.setText(_translate("SubWindow", "TextLabel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubWindow = QtWidgets.QMainWindow()
    ui = Ui_SubWindow()
    ui.setupUi(SubWindow)
    SubWindow.show()
    sys.exit(app.exec_())
