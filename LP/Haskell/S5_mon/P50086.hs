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

instance Functor Queue 
    where 
        fmap f (Queue l r) = Queue (fmap f l) (fmap f r)

translation :: Num b => b -> Queue b -> Queue b 
translation n q = fmap (+n) q

q2l :: Queue a -> [a]
q2l (Queue l r) = l ++ reverse r

uQ :: Queue a -> Queue a -> Queue a
uQ (Queue al ar) (Queue bl br) = Queue (al ++ reverse ar ++ bl) br

instance Applicative Queue
    where 
        pure l = Queue [l] []
        qf <*> q = Queue (q2l qf <*> q2l q) []

instance Monad Queue
    where 
        return = pure
        q >>= f = Queue l []
            where 
                l = q2l q >>= (q2l . f)

kfilter :: (p -> Bool) -> Queue p -> Queue p 
kfilter f q = do 
    x <- q
    if f x then return x else create 