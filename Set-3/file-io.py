# **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"



with open('./input.txt', 'r') as file:
    content = file.read()

words = content.split()

with open('./output.txt', 'a') as file:
    file.write(f"Number of words: {len(words)}\n")
