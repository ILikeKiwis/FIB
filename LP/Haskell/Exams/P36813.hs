degree::Eq a => [(a,a)] -> a -> Int
degree [] v = 0
degree ((x, y):ls) v 
    |   v == x || v == y = 1 + degree ls v
    |   otherwise = degree ls v

