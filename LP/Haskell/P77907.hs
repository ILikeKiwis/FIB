
absValue:: Integer-> Integer
absValue x = abs(x) 

power:: Int -> Int -> Int
power n p = n^p

isPrime:: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime x = not (teDivisor x 2)

teDivisor:: Int -> Int -> Bool
teDivisor x div 
    |   div * div > x = False
    |   mod x div == 0 = True
    |   otherwise = teDivisor x (div+1)

slowFib:: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2)

quickFib:: Int -> Int
quickFib n = quickFibA 0 1 n

quickFibA:: Int -> Int -> Int-> Int
quickFibA a b 0 = a 
quickFibA a b n = quickFibA b (a+b) (n-1)
