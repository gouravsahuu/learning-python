def countVowels (str) :
    vowelsCount = 0
    for char in str :
       if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u") :
           vowelsCount = vowelsCount + 1
    return vowelsCount
count = countVowels("hello")

print("Number of vowels : ",count)