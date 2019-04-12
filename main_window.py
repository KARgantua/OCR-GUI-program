# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../pyqt_ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 270, 160, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.onoffBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.onoffBtn.setObjectName("onoffBtn")
        self.verticalLayout.addWidget(self.onoffBtn)
        self.capBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.capBtn.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(238, 238, 236);")
        self.capBtn.setObjectName("capBtn")
        self.verticalLayout.addWidget(self.capBtn)
        self.exitBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitBtn.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout.addWidget(self.exitBtn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(790, 170, 158, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.langLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.langLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.langLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.langLabel.setObjectName("langLabel")
        self.verticalLayout_2.addWidget(self.langLabel)
        self.langCbox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.langCbox.setObjectName("langCbox")
        self.langCbox.addItem("")
        self.langCbox.addItem("")
        self.verticalLayout_2.addWidget(self.langCbox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.onoffBtn.setText(_translate("MainWindow", "On"))
        self.capBtn.setText(_translate("MainWindow", "Capture"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.langLabel.setText(_translate("MainWindow", "언어 선택"))
        self.langCbox.setItemText(0, _translate("MainWindow", "eng"))
        self.langCbox.setItemText(1, _translate("MainWindow", "kor"))
    @QtCore.pyqtSlot(str)
    def foo2(self, str):
        pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
