# Text Extractor Django

## Overview

Text Extractor Django is a Django web application that extracts key-value pairs from PDF documents and saves the data into a CSV file. The application is capable of handling both header data and tabular data in PDFs, including those containing scanned images.

## Installation

```bash
pip install -r requirements.txt
```


# Text Extractor Django

## Overview

Text Extractor Django is a Django web application that extracts key-value pairs from PDF documents and saves the data into a CSV file. The application is capable of handling both header data and tabular data in PDFs, including those containing scanned images.

## Installation

```bash
pip install -r requirements.txt
```
Usage
Run migrations:
```
python manage.py migrate
```


Start the Django development server:
```
python manage.py runserver
```
Visit [http://127.0.0.1:8000/api/text_extractor](http://127.0.0.1:8000/api/extracted_text/)  in your web browser to access the application.

- Upload a Image file using the provided form.
- The application extracts key-value pairs and displays the results.
-The extracted data is saved to a CSV file in the data/save directory.

# Project Structure
text_extractor: Django app containing the main functionality.

# Functions
extract_and_save_csv: Extracts key-value pairs from Image and saves to CSV.
extract_text_from_scanned_images: Extracts text from scanned images within the PDF.

# Note
Ensure Tesseract OCR is installed and available in your system PATH for accurate text extraction from images.

Author
Shubham Athawane

