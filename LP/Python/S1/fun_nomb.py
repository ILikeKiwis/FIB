def absValue(x):
    if x >= 0 : 
        return x
    else :
        return -x

def power(x,p):
    return x**p

def isPrime(x):
    if x in range(2):
        return False
    for i in range (2, x // 2 + 1):
        if x % i == 0: 
            return False 
    return True

def slowFib(n):
    if n == 0 or n == 1 :
        return n 
    else :
        return slowFib(n-1) + slowFib(n-2)
    
def quickFib(n): 
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x+y
    return x