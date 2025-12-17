# scroll-scribe

📜 Overview
This repository provides a simple, reproducible workflow for turning non-searchable or “vectorized” PDFs into fully searchable documents using open-source tools:
	•	OCRmyPDF - automates the OCR process
	•	Tesseract OCR - recognizes the text
	•	Ghostscript - handles PDF rendering and cleanup
  
This is useful for:
	•	Conference programs
	•	Scientific abstract booklets
	•	Scanned articles or reports
	•	Digitized notes
	•	Photos of documents
	•	Archival material
If you can convert it to a PDF, this workflow can attempt to make it searchable.

📜 Features
	•	Runs OCR on every page, even if the PDF already contains a partial or broken text layer
	•	Supports multiple languages (via Tesseract language packs)
	•	Works on macOS, Windows, and Linux
	•	Generates a clean, searchable PDF with an embedded “hidden text” layer
	•	Fully open-source stack

📜 Requirements: macOS (Homebrew)

Before running the script, install:

brew install ocrmypdf tesseract ghostscript

Ubuntu / Linux

sudo apt update
sudo apt install -y ocrmypdf tesseract-ocr ghostscript

Windows (PowerShell via Chocolatey)

choco install ocrmypdf tesseract ghostscript --yes

📜 Limitations

Works extremely well for:
	•	Printed text
	•	High-resolution scans
	•	iPhone/phone photos of printed pages
	•	PDFs that have been “outlined” or exported without a text layer

Works partially for:
	•	Neat, modern handwriting
	•	Simple block lettering

Works poorly without specialized tools:
	•	Cursive handwriting
	•	Damaged manuscripts
	•	Ancient scrolls, papyri, non-Latin scripts
	•	Anything with inconsistent or ornate handwriting

📜 Contributing

Pull requests are welcome - improvements to documentation, Windows instructions, example workflows, or test files would help.
