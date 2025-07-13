# config/pdf_config.py
# PDF processing settings

DEFAULT_DPI = 300  # Default resolution for PDF-to-image and image-to-PDF
COMPRESSION_LEVELS = {
    "low": 0,    # Minimal compression (best quality)
    "medium": 1, # Balanced quality and size
    "high": 2    # Maximum compression (smallest size)
}
DEFAULT_COMPRESSION = "medium"

ERROR_MESSAGES = {
    "pdf_encrypted": "PDF is encrypted. Please unlock first.",
    "compression_failed": "Compression failed. Try a different level."
}