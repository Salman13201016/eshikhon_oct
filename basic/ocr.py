import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Open the image file
image = Image.open('1.jpg')
# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)
# Print the extracted text
print(text)