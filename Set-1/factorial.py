def factorial (num) :
    fact = 1
    for i in range(num) :
        fact = fact * (i+1)
    return fact

ans = factorial(5)

print(ans)