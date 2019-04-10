# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../pyqt_ui/ocr_main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 130, 801, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.langLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.langLabel.setMaximumSize(QtCore.QSize(200, 30))
        self.langLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.langLabel.setObjectName("langLabel")
        self.horizontalLayout.addWidget(self.langLabel)
        self.langSel = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.langSel.setMaximumSize(QtCore.QSize(100, 30))
        self.langSel.setObjectName("langSel")
        self.langSel.addItem("")
        self.langSel.addItem("")
        self.horizontalLayout.addWidget(self.langSel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 260, 801, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pictBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pictBtn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pictBtn.setObjectName("pictBtn")
        self.horizontalLayout_2.addWidget(self.pictBtn)
        self.exitBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.exitBtn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout_2.addWidget(self.exitBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SubWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.langLabel.setText(_translate("MainWindow", "Select Language: "))
        self.langSel.setItemText(0, _translate("MainWindow", "eng"))
        self.langSel.setItemText(1, _translate("MainWindow", "kor"))
        self.pictBtn.setText(_translate("MainWindow", "Cam"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
