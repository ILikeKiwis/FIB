--Tree
data LTree a = Leaf a | Node (LTree a) (LTree a) 

instance Show a => Show (LTree a) where 
    show (Leaf a) = "{" ++ show a ++ "}"
    show (Node l r) = "<" ++ show l ++ "," ++ show r ++ ">"

build:: [a] -> LTree a
build [x] = Leaf x 
build x = Node (build e) (build d) 
    where 
        m = length x 
        n = (div m 2) + (mod m 2)
        (e,d) = splitAt n x
