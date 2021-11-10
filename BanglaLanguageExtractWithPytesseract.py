import cv2
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C://Users//User//AppData//Local//Programs//Tesseract-OCR//tesseract.exe"


#checking Bengali.traineddata exits in the directory
filenames = os.listdir('C:/Users/User/AppData/Local/Programs/Tesseract-OCR/tessdata')
print(filenames)

#input the image with the directory path
img = cv2.imread("E:/BanglaLanguageExtractFromImage/xxx_page1.png")

#Extract the Bangla Text from Image.
text= pytesseract.image_to_string(img, lang='Bengali')

print(text)