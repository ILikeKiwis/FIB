data Stack a = Stack [a]

sta::a -> Stack a -> Stack a 
sta n (Stack []) = Stack [n]
sta n (Stack s) = Stack (n:s)

pop::Stack a -> Stack a 
pop (Stack []) = Stack []
pop (Stack (s:ss)) = Stack (ss)
 
eval::[String] -> Either Int String
eval s = Right 1

main::IO()
main = do 
    line <- getLine
    let elem = words line
    forM_ (eval elem) print