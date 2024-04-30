import pdfplumber
import re

pdf_path = r'C:\Users\hiand\Documents\UChicago\Interview\K1X\Files\Test_Document.pdf'

number_lines = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            for line in text.split('\n'):
                # If the names of the line item is no longer "Line" but still follows the general rule of "Name x. ####"
                print(line)

                # If it no longer follows the general rule above and has a mix of string and number in the values
                # If there are multiple numbers in one line
                found_numbers = re.findall(r'\b\d+\b', line)  
                if found_numbers:
                    number_lines.extend(map(int, found_numbers[1:]))

total_sum = sum(number_lines)
print("\nTotal sum of values in PDF: " + str(total_sum))