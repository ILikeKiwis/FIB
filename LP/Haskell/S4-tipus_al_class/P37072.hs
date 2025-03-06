data Tree a = Node a (Tree a) (Tree a) | Empty
    deriving (Show)

t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty 
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2

size::Tree a -> Int
size Empty = 0
size (Node _ lt rt) = 1 + size lt + size rt

height :: Tree a -> Int
height Empty = 0
height (Node _ lt rt) = 1 + max (height lt) (height lt) 

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty= True
equal _ Empty = False
equal Empty _ = False 
equal (Node n nlt nrt) (Node a alt art)
    |   n == a = (equal nlt alt && equal nrt art)  
    |   otherwise = False