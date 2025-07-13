# 📱 SmallPDF Clone (Offline Mobile PDF Tool)

This is a lightweight, fully offline mobile app (built using Python and Kivy) that replicates essential features of [Smallpdf](https://smallpdf.com/) for personal use. The app enables you to manage PDF documents directly from your phone—without internet access or subscription limits.

> ✅ Designed for **Android**
> 🧠 Built entirely using **Python**
> 🔐 No ads, no trackers, no cloud — your documents stay local.

---

## 🌟 Features

| Category         | Features                                                                |
|------------------|-------------------------------------------------------------------------|
| 📄 PDF Operations | Merge PDFs, Split PDFs, Compress PDFs, Reorder/Delete Pages             |
| 🖼️ Image Tools     | Convert Images to PDF, Scan via Camera                                 |
| 🔍 OCR            | Extract text from scanned images using Tesseract OCR                    |
| 🔐 Security       | Password protect or unlock PDFs                                         |
| ✍️ Editor         | Add text annotations (in development)                                  |
| 📤 Export         | Save to device, Share via Android file picker                           |

---

## 🧱 Folder Structure

```bash

smallpdf\_clone/
├── main.py                  # Entry point
├── buildozer.spec           # Android build config
├── requirements.txt         # Python dependencies
├── assets/                  # Icons, logos
├── utils/                   # Core PDF/OCR logic
├── screens/                 # Kivy UI screen files (.kv)
├── controllers/             # Backend logic for each screen
├── components/              # Reusable widgets/components
└── config/                  # Theme, global constants

````

---

## ⚙️ Requirements

> Works on Windows / Linux / WSL  
> For Android APK builds, Linux is recommended (or WSL on Windows)

### 📦 Python Dependencies

Install all Python dependencies:

```bash
pip install -r requirements.txt
````

**You must also install:**

### 🔧 Poppler (for pdf2image)

* **Windows**: [Download Poppler](https://github.com/oschwartz10612/poppler-windows/releases)
  Add `...\poppler\Library\bin` to your system PATH.

* **Linux (Ubuntu/WSL)**:

```bash
sudo apt install poppler-utils
```

### 🔧 Tesseract OCR

* **Windows**: [Download Tesseract](https://github.com/tesseract-ocr/tesseract)
* **Linux**:

```bash
sudo apt install tesseract-ocr
```

---

## 🚀 Run Locally (for testing)

```bash
python main.py
```

---

## 📲 Build for Android (with Buildozer)

> Buildozer runs only on Linux or WSL (not Windows natively)

### 1. Install Buildozer

```bash
sudo apt install -y build-essential python3-pip git
pip install buildozer
```

### 2. Initialize and Configure

```bash
buildozer init
# Edit buildozer.spec: add permissions, dependencies, etc.
```

### 3. Build APK

```bash
buildozer -v android debug
```

APK will be generated in the `bin/` directory.

---

## 📚 Libraries Used

| Library           | Purpose                               |
| ----------------- | ------------------------------------- |
| **Kivy**          | UI framework                          |
| **KivyMD**        | Material Design widgets               |
| **PyPDF2**        | Basic PDF merge/split                 |
| **pikepdf**       | Compress PDFs, add/remove passwords   |
| **pytesseract**   | OCR from images                       |
| **reportlab**     | Create PDFs from scratch (text/image) |
| **pdf2image**     | Convert PDF to images (with Poppler)  |
| **opencv-python** | Image enhancement for scanned docs    |
| **pillow**        | Image processing                      |
| **plyer**         | Android file pickers & device APIs    |

---

## ✍️ Author

**Harsh Dadiya**
📍 Gujarat, India
🔗 [GitHub](https://github.com/Dadiya-Harsh)

---

## 📌 License

This project is for **personal use** and **educational purposes** only.
Respect the licenses of third-party libraries used in this app.

---

## 📸 Screenshots

> Coming soon…

---

## 💬 Feedback & Ideas

Feel free to suggest improvements or request new features.
