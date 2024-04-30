import pdfplumber
import re

pdf_path = r'C:\Users\hiand\Documents\UChicago\Interview\K1X\Files\Test_Document.pdf'

number_lines = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'):
            # If the names of the line item is no longer "Line" but still follows the general rule of "Name x. ####"
            found_numbers = re.findall(r'\d+', line)
            if found_numbers:
                number_lines.extend(map(int, found_numbers[1:]))

numbers = [int(x) for x in number_lines]
total_sum = sum(numbers)

print("\nTotal sum of values in PDF: " + str(total_sum))