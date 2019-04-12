import pytesseract
import cv2
from ShowVideo import *
from ImageViewer import *
from main_window import *
from sub_window import *
import numpy

#===================================================
# MainWindow에서 실행할 함수 리스트
#===================================================

def openWindow(self, text):
    self.window=QtWidgets.QMainWindow()
    self.ui=Ui_SubWindow()
    self.ui.setupUi(self.window)
    self.ui.setText(text)
    self.window.show()

def addWidget(self, widget):
    self.horizontalLayout.addWidget(widget)

def onSig(self):
    self.onoffBtn.clicked.connect(vid.startVideo)

def capSig(self):
    self.capBtn.clicked.connect(vid.capPic)

def exitSig(self):
    self.exitBtn.clicked.connect(sys.exit)

def procOcr(self):
    image = cv2.imread("img1.png", cv2.IMREAD_COLOR)
    lang = self.langCbox.currentText()
    config = ('-l %s --oem 1 --psm 3' % lang)
    text = pytesseract.image_to_string(image, config=config)
    self.openWindow(text)

def foo1():
    pass

#===================================================
# ShowVideo에서 실행할 함수 리스트
#===================================================

# def capPic(self):
#     cv2.imwrite("img1.png",self.image, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
#     config = ('-l kor --oem 1 --psm 3')
#     im = cv2.imread("img1.png", cv2.IMREAD_COLOR)
#     text = pytesseract.image_to_string(im, config=config)
#     self.openWindow(text)

#self.langCbox.currentText()

def capPic(self):
    cv2.imwrite("img1.png",self.image, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
    self.ImageSignal.emit()

#===================================================
# SubWindow에서 실행할 함수 리스트
#===================================================

def setText(self, text):
    self.textLabel.setText(text)

#===================================================
# 클래스에 함수 추가
#===================================================

Ui_MainWindow.addWidget = addWidget
Ui_MainWindow.onSig = onSig
Ui_MainWindow.capSig = capSig
Ui_MainWindow.exitSig = exitSig
Ui_MainWindow.openWindow = openWindow
Ui_MainWindow.procOcr = procOcr

ShowVideo.capPic = capPic
ShowVideo.openWindow = openWindow

Ui_SubWindow.setText = setText

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # 비디오 촬영 스레드 생성
    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)

    # 이미지 뷰어 위젯 객체 생성
    image_viewer1 = ImageViewer()

    ui = Ui_MainWindow()

    # 시그널 연결
    vid.VideoSignal.connect(image_viewer1.setImage)
    vid.ImageSignal.connect(ui.procOcr)

    MainWindow = QtWidgets.QMainWindow()
    
    ui.setupUi(MainWindow)
    ui.addWidget(image_viewer1)
    ui.onSig()
    ui.capSig()
    ui.exitSig()
    MainWindow.show()
    sys.exit(app.exec_())
