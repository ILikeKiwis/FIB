def myLength(L):
    x = 0
    for i in L:
        x += 1
    return x

def myMaximum(L):
    a = L[0]
    for i in L:
        a = a if a > i else i
    return a

def average(L):
    a = 0
    for i in L:
        a += i
    return a / len(L)

def buildPalindrome(L):
    res = []
    for i in L:
        res.insert(0, i)
    
    return res + L

def remove(L1, L2):
    res = []
    for i in L1:
        if i not in L2:
            res.append(i)
        
    return res

def flatten(L):
    res = []
    for i in L:
        if isinstance(i, list):
            res += (flatten(i))
        else :
            res.append(i)
    return res

def oddsNevens(L):
    o = []
    e = []
    for i in L:
        if i % 2 == 0:
            e.append(i)
        else :
            o.append(i)
    return o, e

def isPrime(x):
    if x in range(2):
        return False
    for i in range (2, x // 2 + 1):
        if x % i == 0: 
            return False 
    return True

def primeDivisors(n):
    res = []
    for i in range(2, n // 2 + 1) :
        if n % i == 0:
            if isPrime(i):
                res.append(i)
    if isPrime(n):
        res.append(n)
    return res 