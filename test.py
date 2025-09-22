def calculate_sum(a,b): # Missing space after comma
    result = a+b  # No spaces around operator
    unused_variable=42 # Unused variable, no space after equals
      extra_indent=1  # Incorrect indentation
    if result>0  # Missing colon and spaces
        print("Sum is positive")  # Inconsistent quotes
    else:
        print('Sum is zero or negative') # Mixed quotes, trailing whitespace 
    return result # This is fine but let's add a long line to trigger line length warning
# This line is intentionally too long to trigger a line length error in flake8, which typically enforces a maximum line length of 79 or 88 characters per PEP 8 guidelines.