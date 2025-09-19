ones :: [Integer]
ones = 1:ones

nats :: [Integer]
nats = 0 : map (+1) nats

ints :: [Integer]
ints = iterate (\x -> if x > 0 then -x else -x+1) 0

triangulars :: [Integer]
triangulars = 0:scanl (+) 1 (iterate (+1) 2)

factorials :: [Integer]
factorials = scanl (*) 1 (iterate (+1) 1)
fibs :: [Integer]
fibs = scanl (+) 0 (1:fibs)
primes :: [Integer]
primes = garbell (iterate (+1) 2)
    where 
        garbell (p:xs) = p : garbell [x | x <- xs, mod x p /= 0]
hammings :: [Integer]
hammings = 1 : [x | x <- (iterate (+1) 2), even x  || mod x 3 == 0 || mod x 5 == 0]
