import cv2
import sys
import pytesseract

CAM_ID = 0
def capture(camid = CAM_ID):
    cam = cv2.VideoCapture(camid)
    if cam.isOpened() == False:
        print ('cant open the cam (%d)' % camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print ('frame is not exist')
        return None
    
    # png로 압축 없이 영상 저장 
    cv2.imwrite("img1.png",frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
    cam.release()

    return "img1.png"

if __name__ == '__main__':
 
    if len(sys.argv) < 2:
        print('Usage: python ocr_simple.py image.jpg')
        sys.exit(1)
    
    # 파일 경로 및 언어 선택
    imLang = sys.argv[1]
        
    if sys.argv[1] == 'eng':
        config = ('-l eng --oem 1 --psm 3')
    elif sys.argv[1] == 'kor':
        config = ('-l kor --oem 1 --psm 3')
    
    imPath = capture()
    

    # Read image from disk
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    
    # Run tesseract OCR on image
    text = pytesseract.image_to_string(im, config=config)
    
    # Print recognized text
    print(text)