from readPDF import *

# Simple PDF without any issues
def test_simple():
    pdf_path = r"C:\Users\hiand\Documents\UChicago\Interview\K1X\Files\Test_Document_1.pdf"
    total_sum = read_and_sum("Test Simple PDF", pdf_path)
    assert total_sum == 179

# Simple PDF without any issues
def test_different_line_name():
    pdf_path = r"C:\Users\hiand\Documents\UChicago\Interview\K1X\Files\Test_Document_2.pdf"
    total_sum = read_and_sum("Test Different Line Name", pdf_path)
    assert total_sum == 179

# Simple PDF without any issues
def test_non_numeric_values():
    pdf_path = r"C:\Users\hiand\Documents\UChicago\Interview\K1X\Files\Test_Document_3.pdf"
    total_sum = read_and_sum("Test Non-Numeric Values After 'Line'", pdf_path)
    assert total_sum == 109

if __name__ == "__main__":
    test_simple()
    test_different_line_name()
    test_non_numeric_values()
    print("Everything Passed!")