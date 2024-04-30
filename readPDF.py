import pdfplumber

pdf_path = r'C:\Users\hiand\Documents\UChicago\Interview\K1X\Files\filled_form_2.pdf'

number_lines = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'):
            if line.lower().startswith('line'):
                line_parts = line.split('.')
                line_number = line_parts[0].split(' ')[1]
                line_content = line_parts[1].strip()

                number_lines.append(line_content)
                print(f'Line {line_number}: {line_content}')