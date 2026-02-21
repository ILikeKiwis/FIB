df::Int -> Int
df n 
    |   n <= 0 = 1
    |   otherwise = n * df (n-2)

sumd::Int -> Int 
sumd n
    |   n >= 10 = (mod n 10) + sumd (div n 10)
    |   otherwise = n

dup::[Int] -> [Int]
dup [] = []
dup (l:ls) = l:l:(dup ls)

pal::String -> Bool 
pal s = s == reverse s 

apply2::(a->a) -> a -> a
apply2 f = f . f