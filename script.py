import cv2
import pytesseract
import sys

image_name = sys.argv[1]

img = cv2.imread(image_name)

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

def ocr(image):
    text=pytesseract.image_to_string(image)
    return text

def grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

def noise_removal(image):
    return cv2.medianBlur(image,5)

def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

img= grayscale(img)
img= noise_removal(img)
img=threshold(img)

text = ocr(img)
print(text)