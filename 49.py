import cv2
import pytesseract

# If on Windows, specify Tesseract path:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = "image.jpg"

# Read image
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OCR extraction
text = pytesseract.image_to_string(gray)

print("Detected Text:")
print(text)