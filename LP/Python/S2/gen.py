def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a+b
    
def roots(x):
    a = x 
    while True: 
        yield a
        a = 1/2 * (a + x/a)

def isPrime(x):
    if x in range(2):
        return False
    for i in range (2, x // 2 + 1):
        if x % i == 0: 
            return False 
    return True

def primes():
    a = 2
    yield a 
    while True: 
        a += 1
        if isPrime(a):
            yield a 

def isHammings(x):
    if x == 1:
        return True
    elif x % 2 == 0:
        return isHammings(x/2)
    elif x % 3 == 0:
        return isHammings(x/3)
    elif x % 5 == 0:
        return isHammings(x/5)

    return False

def hammings():
    a = 1
    while True:    
        if isHammings(a):
            yield a
        a += 1