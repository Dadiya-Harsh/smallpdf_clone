# config/ocr_config.py
# OCR-related settings

TESSERACT_CONFIG = r"--oem 3 --psm 6"  # Default Tesseract OCR configuration
OCR_LANGUAGES = ["eng"]  # Default language for OCR, can be extended

ERROR_MESSAGES = {
    "ocr_failed": "Text extraction failed. Try a higher quality image."
}