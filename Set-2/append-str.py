import math

s1 = "Ault"
s2 = "Kelly"
s1a = ""
s1b = ""

for i in range(0, math.floor(len(s1)/2)) :
    s1a = s1a + s1[i]

for i in range(math.floor(len(s1)/2), len(s1)) :
    s1b = s1b + s1[i]

s3 = s1a+s2+s1b
print(s3)