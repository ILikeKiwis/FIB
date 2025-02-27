eql:: [Int] -> [Int] -> Bool
eql [] [] = True
eql _ [] = False
eql [] _ = False 
eql xs ys = (length xs == length ys) && all (==True) (zipWith (==) xs ys)