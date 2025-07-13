# config/file_config.py
# File system and file handling settings

ASSETS_DIR = "assets/"
OUTPUT_DIR = "output/"  # Where processed files are saved
SUPPORTED_IMAGE_FORMATS = (".png", ".jpg", ".jpeg", ".bmp")
SUPPORTED_PDF_FORMATS = (".pdf",)
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB max file size
MAX_IMAGE_SIZE = (5000, 5000)  # Max dimensions for images (width, height)

ERROR_MESSAGES = {
    "file_not_found": "Selected file not found.",
    "unsupported_format": "File format not supported.",
    "file_too_large": "File exceeds maximum size limit (100 MB).",
    "image_too_large": "Image dimensions exceed limit (5000x5000).",
    "permission_denied": "Storage permission denied. Please grant access."
}