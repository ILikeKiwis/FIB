myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl _ a [] = a
myFoldl f a (b:bs) = myFoldl f (f a b) (bs)

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr _ b [] = b
myFoldr f b (a:as) = f a (myFoldr f b as)

myIterate :: (a -> a) -> a -> [a]
myIterate f a = a:(myIterate f (f a)) 

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil p f a 
    |   p a == True = a 
    |   otherwise = myUntil p f (f a)

myMap :: (a -> b) -> [a] -> [b]
myMap f a = myFoldr (\x y -> (f x):y) [] a

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f a = myFoldr (\ x y -> if f x then x:y else y) [] a

myAll:: (a->Bool) -> [a] -> Bool
myAll f a = myFoldr (\x y -> (f x) && y) True a

myAny:: (a->Bool) -> [a] -> Bool
myAny f a = myFoldr (\x y -> (f x) || y) False a
 
myZip:: [a] -> [b] -> [(a,b)]
myZip _ [] = []
myZip [] _ = []
myZip (a:as) (b:bs) = [(a,b)] ++ (myZip as bs)

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f a b = myFoldr (\(x, y) i -> (f x y):i) [] (myZip a b) 