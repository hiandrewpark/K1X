This is a take-home assignment for K1X.

I am tasked with reading in a PDF from a local path and extracting the sum of the values in the displayed line items. The PDF follows the following format:

Form ####

Line #. x
Line #. x
Line #. x
etc.

I must extract the x values and disregard the form and line numbers.

I have added a few more edge cases to the code. The following lists the implemented edge cases:
1. The line item no longer starts with "Line" and can be anything
2. The x contains a mix of numbers and strings. If this is the case, this specific x will be counted towards the final sum as it is not a number.
3. There are multiple numbers in one line instead of one
4. There is no line number after "Line"