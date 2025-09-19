data Queue a = Queue [a] [a]
    deriving (Show)

create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push n (Queue l r) = Queue l (n:r) 

pop :: Queue a -> Queue a
pop (Queue [] []) = Queue [] []
pop (Queue [] rs) = Queue (reverse (init rs)) []
pop (Queue (l:ls) r) = Queue ls r

top :: Queue a -> a
top (Queue (l:ls) r) = l
top (Queue [] r) = last r

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty (Queue l r) = False 

instance Eq a => Eq (Queue a)
    where
        (Queue [] []) == (Queue [] []) = True
        (Queue l1 l2) == (Queue r1 r2) = l1 ++ reverse l2 == r1 ++ reverse r2 

