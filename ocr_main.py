# OCR 동작 부분

from ocr_main_window import *
from ocr_cam_window import *
import pytesseract

#===========================================
# Main Window 에서 실행할 함수 리스트
#===========================================

# Cam Window 실행
def openWindow(self):
    self.window=QtWidgets.QMainWindow()
    self.ui=Ui_CamWindow()
    self.ui.setupUi(self.window)
    self.ui.captureSig()
    self.window.show()

# camera 버튼 시그널
def cameraSig(self):
    self.camBtn.clicked.connect(self.openWindow)

#===========================================
# Cam Window에서 실행할 함수 리스트
#===========================================

CAM_ID = 0
def capture(self, camid = CAM_ID):
    cam = cv2.VideoCapture(camid)
    imPath = "ocr1.png"
    if cam.isOpened() == False:
        print ('cant open the cam (%d)' % camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print ('frame is not exist')
        return None
    
    # png로 압축 없이 영상 저장 
    cv2.imwrite(imPath,frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
    cam.release()

    return imPath

# 현재 Cam Label에서 보여주는 이미지 read 후 tesseract 를 사용해서 텍스트로 변환
def readImage(self):
    imPath = self.capture()
    print(imPath)
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    config = ('-l kor --oem 1 --psm 3')
    self.text = pytesseract.image_to_string(im, config=config)
    self.camLabel.setText(self.text)

# capture 버튼 시그널
def captureSig(self):
    self.capBtn.clicked.connect(self.readImage)

Ui_MainWindow.cameraSig = cameraSig
Ui_MainWindow.openWindow = openWindow

Ui_CamWindow.captureSig = captureSig
Ui_CamWindow.capture = capture
Ui_CamWindow.readImage = readImage

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.cameraSig()
    MainWindow.show()
    sys.exit(app.exec_())
