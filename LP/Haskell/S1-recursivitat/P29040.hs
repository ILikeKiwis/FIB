insert:: [Int] -> Int -> [Int] 
insert [] n = [n]
insert (f:rest) n 
    |   f > n = n:(f:rest) 
    |   otherwise = f:(insert rest n)

isort:: [Int] -> [Int]
isort [one] = [one]
isort (first:second:rest)
    |   first <= second = first:(isort (second:rest))
    |   first > second = isort (insert (second:rest) first)

remove:: [Int] -> Int -> [Int]
remove (head:tail) n
    |   head == n = tail
    |   otherwise = head:(remove tail n)
 
ssort:: [Int] -> [Int]
ssort [] = []
ssort l = m:ssort(remove l m)
    where m = minimum l

merge:: [Int] -> [Int] -> [Int]
merge [] [] = []
merge [] l = l
merge l [] = l
merge (x:xs) (y:ys) 
    |   x <= y = x:(merge (xs) (y:ys))
    |   otherwise = y:(merge (x:xs) (ys))

msort:: [Int] -> [Int]
msort [] = []
msort [one] = [one]
msort list = merge (msort (fst l)) (msort (snd l))
    where 
        l = split list

split:: [Int] -> ([Int], [Int])
split [] = ([], [])
split list = (fh, sh)
    where 
        fh = take (div(length list)  2) list
        sh = drop (length fh) list 


qsort::[Int] -> [Int]
qsort [] = []
qsort [one] = [one]
qsort (pv:rest) = (qsort (menors pv rest)) ++ [pv] ++ (qsort (majors pv rest))

menors:: Ord a => a -> [a] -> [a]
menors _ [] = []
menors x l = [n | n <- l, n <= x]

majors:: Ord a => a -> [a] -> [a]
majors _ [] = []
majors x l = [n | n <- l, n > x]

genQsort:: Ord a => [a] -> [a]
genQsort [] = []
genQsort (pv:tail) = (genQsort (menors pv tail)) ++ [pv] ++ (genQsort (majors pv tail))
