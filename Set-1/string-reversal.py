def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

input_string = "Hello"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)