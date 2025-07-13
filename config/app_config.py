# config/app_config.py
# General app metadata and Android-specific settings

APP_NAME = "SmallPDF Clone"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Harsh Dadiya"

ANDROID_PERMISSIONS = ["READ_EXTERNAL_STORAGE", "WRITE_EXTERNAL_STORAGE", "CAMERA"]

BUILD_SETTINGS = {
    "orientation": "portrait",
    "icon": "assets/icon.png",
    "requirements": [
        "kivy==2.3.0",
        "kivymd==1.2.0",
        "pypdf2==3.0.1",
        "pikepdf==9.3.0",
        "reportlab==4.2.2",
        "pillow==10.4.0",
        "opencv-python==4.10.0.84",
        "pytesseract==0.3.13",
        "pdf2image==1.17.0",
        "plyer==2.1.0"
    ]
}