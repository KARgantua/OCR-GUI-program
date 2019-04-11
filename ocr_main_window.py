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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 797, 318))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.langLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.langLabel.setMaximumSize(QtCore.QSize(200, 30))
        self.langLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.langLabel.setObjectName("langLabel")
        self.horizontalLayout.addWidget(self.langLabel)
        self.langSel = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.langSel.setMaximumSize(QtCore.QSize(100, 30))
        self.langSel.setObjectName("langSel")
        self.langSel.addItem("")
        self.langSel.addItem("")
        self.horizontalLayout.addWidget(self.langSel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.engLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.engLabel.setMaximumSize(QtCore.QSize(200, 30))
        self.engLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.engLabel.setObjectName("engLabel")
        self.horizontalLayout_3.addWidget(self.engLabel)
        self.engSel = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.engSel.setMaximumSize(QtCore.QSize(250, 30))
        self.engSel.setObjectName("engSel")
        self.engSel.addItem("")
        self.engSel.addItem("")
        self.engSel.addItem("")
        self.engSel.addItem("")
        self.horizontalLayout_3.addWidget(self.engSel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.camBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.camBtn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.camBtn.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.camBtn.setObjectName("camBtn")
        self.horizontalLayout_2.addWidget(self.camBtn)
        self.exitBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitBtn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.exitBtn.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout_2.addWidget(self.exitBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.langLabel.setText(_translate("MainWindow", "Select Language: "))
        self.langSel.setItemText(0, _translate("MainWindow", "eng"))
        self.langSel.setItemText(1, _translate("MainWindow", "kor"))
        self.engLabel.setText(_translate("MainWindow", "Select Engine: "))
        self.engSel.setItemText(0, _translate("MainWindow", "0    Original Tesseract only"))
        self.engSel.setItemText(1, _translate("MainWindow", "1    Neural nets LSTM only"))
        self.engSel.setItemText(2, _translate("MainWindow", "2    Tesseract + LSTM."))
        self.engSel.setItemText(3, _translate("MainWindow", "3    Default, based on what is available"))
        self.camBtn.setText(_translate("MainWindow", "Cam"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
