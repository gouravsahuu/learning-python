str1 = "PyNaTive"

lower = ""
upper = ""

for char in str1 :
    if(char.islower()) :
        lower = lower + char
    elif(char.isupper()) :
        upper = upper + char

print(lower+upper)