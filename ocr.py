import easyocr
import json

def extract_text(image_path):
    # Initialize the EasyOCR Reader for English and Hindi
    reader = easyocr.Reader(['en', 'hi'])  # You can add more languages if needed

    # Perform OCR on the image
    results = reader.readtext(image_path)

    # Extract text from results
    extracted_text = []
    for (bbox, text, prob) in results:
        extracted_text.append(text)

    return json.dumps({"extracted_text": " ".join(extracted_text)})
