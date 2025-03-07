data Tree a = Node a (Tree a) (Tree a) | Empty
    deriving (Show)

size::Tree a -> Int
size Empty = 0
size (Node _ lt rt) = 1 + size lt + size rt

height :: Tree a -> Int
height Empty = 0
height (Node _ lt rt) = 1 + max (height lt) (height rt) 

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty= True
equal _ Empty = False
equal Empty _ = False 
equal (Node n nlt nrt) (Node a alt art)
    |   n == a = (equal nlt alt && equal nrt art)  
    |   otherwise = False

isomorphic :: Eq a => Tree a -> Tree a -> Bool 
isomorphic Empty Empty = True
isomorphic _ Empty = False
isomorphic Empty _ = False
isomorphic (Node n nlt nrt) (Node a alt art)
    |   n == a = (isomorphic nlt alt && isomorphic nrt art) || (isomorphic nrt alt && isomorphic nlt art)
    |   otherwise = False;

preOrder :: Tree a -> [a] 
preOrder Empty = []
preOrder (Node n lt rt) = n:(preOrder lt ++ preOrder rt)

postOrder :: Tree a -> [a] 
postOrder Empty = []
postOrder (Node n lt rt) = (postOrder lt ++ postOrder rt) ++ [n]

inOrder :: Tree a -> [a] 
inOrder Empty = []
inOrder (Node n lt rt) = inOrder lt ++ [n] ++ inOrder rt

breadthFirst :: Tree a -> [a]
breadthFirst t = bf [t]
    where 
        bf [] = []
        bf (Empty:ts) = bf ts
        bf ((Node n lt rt):ts) = n:bf (ts ++ [lt,rt])

build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build (p:ps) is =
    let (lIn,_:rIn) = break (== p) is
        (lPr, rPr) = splitAt (length lIn) ps
    in Node p (build lPr lIn) (build rPr rIn)

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ t Empty = t
overlap _ Empty t = t
overlap f (Node n nl nr) (Node a al ar) = (Node (f n a) (overlap f nl al) (overlap f nr ar))