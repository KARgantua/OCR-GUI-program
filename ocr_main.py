# OCR 동작 부분

from ocr_main_window import *
from ocr_cam_window import *

def openWindow(self):
    self.window=QtWidgets.QMainWindow()
    self.ui=Ui_CamWindow()
    self.ui.setupUi(self.window)
    self.window.show()

def camera(self):
    self.camBtn.clicked.connect(self.openWindow)

Ui_MainWindow.camera = camera
Ui_MainWindow.openWindow = openWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.camera()
    MainWindow.show()
    sys.exit(app.exec_())
