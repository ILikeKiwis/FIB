countIf :: (Int -> Bool) -> [Int] -> Int 
countIf f xs = length (filter f xs)

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam _ [] = []
pam xs (f:fs) = (map f xs) : pam xs fs 

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 xs fs = map (\x -> map ($ x) fs) xs

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int 
filterFoldl p f b xs = foldl f b (filter p xs)

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int] 
insert f xs n = takeWhile (\x -> f x n) xs ++ [n] ++ dropWhile (\x -> f x n) xs

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int] 
insertionSort f [] = []
insertionSort f (x:xs) = insert f (insertionSort f xs) x