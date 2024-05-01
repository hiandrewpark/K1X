import pdfplumber
import re

def read_and_sum(test_name, pdf_path):
    print(test_name)
    number_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    # If the names of the line item is no longer "Line" but still follows the general rule of "Name x. ####"
                    print(line)

                    if re.match(r'Form \d+$', line.strip()):
                        continue

                    # If it no longer follows the general rule above and has a mix of string and number in the values
                    # If there are multiple numbers in one line
                    found_numbers = re.findall(r'\b\d+\b', line)  
                    if found_numbers:
                        # Check if there is a number after the 'line'. If there is, disregard that number. If not, continue
                        if re.match(r'\w+ \d+\.', line.strip()):
                            number_lines.extend(map(int, found_numbers[1:]))
                        else:
                            number_lines.extend(map(int, found_numbers))

    total_sum = sum(number_lines)
    print("\nTotal sum of values in PDF: " + str(total_sum) + "\n----------------------------")

    return total_sum