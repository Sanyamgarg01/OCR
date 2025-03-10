import pytesseract
from PIL import Image

test_file="data/eq5.jpeg"
# noise_removed_test_file="temp/dilated_image.png"

img=Image.open(test_file)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ocr_result=pytesseract.image_to_string(img)

print(ocr_result)