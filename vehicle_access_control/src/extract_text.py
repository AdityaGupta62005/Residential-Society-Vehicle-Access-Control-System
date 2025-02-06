import pytesseract
import cv2

def extract_text(number_plate_region):
    # Preprocess for OCR
    gray_plate = cv2.cvtColor(number_plate_region, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_plate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Use Tesseract to extract text
    text = pytesseract.image_to_string(thresh, config='--psm 11')
    return text.strip().replace(" ", "")

