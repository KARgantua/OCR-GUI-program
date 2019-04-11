# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../pyqt_ui/ocr_cam_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CamWindow(object):
    def setupUi(self, CamWindow):
        CamWindow.setObjectName("CamWindow")
        CamWindow.resize(700, 800)
        self.horizontalLayoutWidget = QtWidgets.QWidget(CamWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 700, 711, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.capBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.capBtn.setMaximumSize(QtCore.QSize(120, 120))
        self.capBtn.setObjectName("capBtn")
        self.horizontalLayout.addWidget(self.capBtn)
        self.vidLabel = QtWidgets.QLabel(CamWindow)
        self.vidLabel.setGeometry(QtCore.QRect(0, 0, 701, 691))
        self.vidLabel.setObjectName("vidLabel")

        self.retranslateUi(CamWindow)
        QtCore.QMetaObject.connectSlotsByName(CamWindow)

    def retranslateUi(self, CamWindow):
        _translate = QtCore.QCoreApplication.translate
        CamWindow.setWindowTitle(_translate("CamWindow", "Form"))
        self.capBtn.setText(_translate("CamWindow", "Capture"))
        self.vidLabel.setText(_translate("CamWindow", "Video"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CamWindow = QtWidgets.QWidget()
    ui = Ui_CamWindow()
    ui.setupUi(CamWindow)
    CamWindow.show()
    sys.exit(app.exec_())
