import PyPDF
# Open the PDF file
pdf_file = open('example.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF.PdfReader(pdf_file)

# Initialize an empty string to hold the text
pdf_text = ""

# Loop through all the pages and extract text
for page in pdf_reader.pages:
    pdf_text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(pdf_text)

import pdfplumber

# Open the PDF file
with pdfplumber.open('example.pdf') as pdf:
    # Initialize an empty string to hold the text
    pdf_text = ""

    # Loop through each page and extract text
    for page in pdf.pages:
        pdf_text += page.extract_text()

# Print the extracted text
print(pdf_text)
