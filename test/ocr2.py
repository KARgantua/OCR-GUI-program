import cv2
import sys
import pytesseract
 
if __name__ == '__main__':
 
    if len(sys.argv) < 2:
        print('Usage: python ocr_simple.py image.jpg')
        sys.exit(1)
    
    # 파일 경로 및 언어 선택
    imPath = sys.argv[1]
    imLang = sys.argv[2]
        
    if sys.argv[2] == 'eng':
        config = ('-l eng --oem 1 --psm 3')
    elif sys.argv[2] == 'kor':
        config = ('-l kor --oem 1 --psm 3')
    
    # Read image from disk
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    
    # Run tesseract OCR on image
    text = pytesseract.image_to_string(im, config=config)
    
    # Print recognized text
    print(text)