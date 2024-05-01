from readPDF import *

# Simple PDF without any issues
def test_simple():
    pdf_path = r"WRITE LOCAL PATH HERE"
    total_sum = read_and_sum("Test Simple PDF", pdf_path)
    assert total_sum == 179, "test_simple failing"

# If the line no longer starts with 'line'
def test_different_line_name():
    pdf_path = r"WRITE LOCAL PATH HERE"
    total_sum = read_and_sum("Test Different Line Name", pdf_path)
    assert total_sum == 179, "test_different_line_name failing"

# If the numeric value contains a string component
def test_non_numeric_values():
    pdf_path = r"WRITE LOCAL PATH HERE"
    total_sum = read_and_sum("Test Non-Numeric Values After 'Line'", pdf_path)
    assert total_sum == 109, "test_non_numeric_values failing"

# If there are multiple numbers in one line
def test_multiple_numbers():
    pdf_path = r"WRITE LOCAL PATH HERE"
    total_sum = read_and_sum("Test Multiple Numbers in One Line", pdf_path)
    assert total_sum == 114, "test_multiple_numbers failing"

# All test mixed in one
def test_no_line_number():
    pdf_path = r"WRITE LOCAL PATH HERE"
    total_sum = read_and_sum("Test with No Line Number", pdf_path)
    assert total_sum == 116, "test_no_line_number failing"

# All test mixed in one
def test_all():
    pdf_path = r"WRITE LOCAL PATH HERE"
    total_sum = read_and_sum("Test All", pdf_path)
    assert total_sum == 116, "test_all failing"

if __name__ == "__main__":
    test_simple()
    test_different_line_name()
    test_non_numeric_values()
    test_multiple_numbers()
    test_no_line_number()
    test_all()
    print("Everything Passed!")