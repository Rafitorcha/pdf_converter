# PDFConverter
## _Convert your images to PDF, viceversa_

![Powered by Python](https://img.shields.io/badge/Powered_by-Python-blue?logo=python)

Convert your images to PDF without needing wifi connection and a lot of resources.

- Drag and drop your images or PDFs to the folder
- See the results in CLI
- ✨Magic ✨

## 🚀 Features

- Import images folders and watch it magically convert to PDF
- Import PDF files and watch it magically convert to images with their respective folders
- Export images and PDF files without losing quality

## Tech

- [Python] - Programming language
- img2pdf(>=0.6.1)
- pdf2image(>=1.17.0)
- pyinstaller(>=6.14.2)

## 📦 Installation

Download from releases section (not yet).

## Development

Install the dependencies.

```sh
cd pdf_converter
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to use

1. **Run the program** and select the 3rd option to automatically create the required folders

2. **For PDF conversion:**
   - Drag and drop PDF files into the `pdf_to_convert` folder

3. **For image conversion:**
   - Drag and drop images into the `images/images_to_convert` folder

#### Building for source

Compile.
```sh
pyinstaller --onefile --name PDFConverter.exe --target-arch win64 creator.py
```

## Structure

📦 PDFConverter
├── 📂 images/
│   ├── 📂 extracted_images      # 🖼️ Images from PDFs
│   └── 📂 images_to_convert     # ⏳ Queue for conversion
├── 📂 pdf_to_convert/
│   ├── 📄 a.pdf                # Sample document
│   └── 📄 sample-local-pdf.pdf
├── 🐍 creator.py               # Main script
├── 📖 README.md
└── 📝 requirements.txt

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [python]: <http://python.org>
