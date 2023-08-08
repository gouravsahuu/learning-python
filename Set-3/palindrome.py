# **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

word = "madam"


def checkPalindrome(word) :
    rev_word = ""

    for char in word :
        rev_word = char + rev_word

    if (word == rev_word) :
        return True
    else :
        return False

ans = checkPalindrome(word)

if ans :
    print(f"The word {word} is a Palindrome.")
else :
    print(f"The word {word} is not a Palindrome.")
