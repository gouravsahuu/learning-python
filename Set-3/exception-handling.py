#  **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def exception_handling(a, b):
    if b == 0:
        return "Cannot divide by zero."
    else:
        return a / b

# Example input
numerator = 5
denominator = 0

output = exception_handling(numerator, denominator)
print(output)
