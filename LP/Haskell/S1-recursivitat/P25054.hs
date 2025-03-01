myLength:: [Int] -> Int
myLength [] = 0                     
myLength l = 1 + myLength(tail l) 

myMaximum::[Int] -> Int
myMaximum[a] = a 
myMaximum(p:s:l) 
    |   p > s = myMaximum (p:l)
    |   otherwise = myMaximum (s:l)

average:: [Int] -> Float
average l = fromIntegral(sum l) / fromIntegral(length l)

buildPalindrome:: [Int] -> [Int]
buildPalindrome l = reverse l ++ l

remove:: [Int] -> [Int] -> [Int]
remove [] b = []
remove (p:l) b 
    |   elem p b = remove l b
    |   otherwise = p : (remove l b)

flatten:: [[Int]] -> [Int]
flatten [] = []
flatten (p:l) = p ++ flatten l

oddsNEvens::[Int] -> ([Int], [Int])
oddsNEvens [] = ([],[])
oddsNEvens (p:r) 
    |   even p = (fst l, p: snd l)
    |   otherwise = (p: fst l, snd l)
    where l = oddsNEvens r

primeDivisors:: Int -> [Int]
primeDivisors 1 = []
primeDivisors n = [div | div <- [1..n], mod n div == 0, isPrime div]   



isPrime:: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime x = not (teDivisor x 2)

teDivisor:: Int -> Int -> Bool
teDivisor x div 
    |   div * div > x = False
    |   mod x div == 0 = True
    |   otherwise = teDivisor x (div+1)



