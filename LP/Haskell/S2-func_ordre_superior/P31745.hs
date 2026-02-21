flatten::[[Int]] -> [Int]
flatten [[]] = []
flatten l = foldl (++) [] l

myLength::String -> Int
myLength [] = 0
myLength s = foldl1 (+) (map (const 1) s)

myReverse::[Int] -> [Int]
myReverse [] = []
myReverse l = foldl (\xs x -> x:xs) [] l

countIn:: [[Int]] -> Int -> [Int] 
countIn [] _ = [0]
countIn l n = map (length) (map (filter (==n)) l)

firstWord:: String -> String 
firstWord [] = []
firstWord s = takeWhile (/= ' ') (dropWhile (== ' ') s)