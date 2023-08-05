def checkPrime (num) :
    count = 0
    for i in range(num) :
        if(num % (i+1) == 0) :
            count += 1
    if(count == 2) :
        return True
    else :
        return False
    
num = 13

ans = checkPrime(num)

if(ans) :
    print(num, "is a Prime Number")
else :
    print(num, "is not a Prime Number")