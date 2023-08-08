# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"

def anagram_check(str1,str2) :
    str1 = str1.lower()
    str2 = str2.lower()

    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    if(sorted_str1 == sorted_str2) :
        return True
    else :
        return False
    
str1 = "Cinema"
str2 = "Iceman"

ans = anagram_check(str1,str2)

print(ans)

