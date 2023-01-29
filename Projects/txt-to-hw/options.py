import cv2
from sys import argv
import pytesseract as pt


filename = 'cap-2_1.pdf'

pt.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

try:
    img = cv2.imread(argv[1])
    result = pt.image_to_string(img)
    print(result)
except IndexError:
    print("No file entered. Using default file...")
    img = cv2.imread(filename)
    result = pt.image_to_string(img)
    print(result)
except FileNotFoundError:
    print("Could not find file. Using default file...")
    txt=open(filename, "r")  
