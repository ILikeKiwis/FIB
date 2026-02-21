eql:: [Int] -> [Int] -> Bool

eql xs ys = (length xs == length ys) && all (==True) (zipWith (==) xs ys)

prod:: [Int] -> Int

prod l = foldr (*) 1 l 


prodOfEvens:: [Int] -> Int
prodOfEvens l = prod (filter even l)

powersOf2:: [Int] 
powersOf2 = iterate (2*) 1

scalarProduct:: [Float] -> [Float] -> Float
scalarProduct xs ys = foldl1 (+) (zipWith (*) xs ys)
