data LogicExpression
        = Or  LogicExpression LogicExpression
        | And LogicExpression LogicExpression
        | Not LogicExpression
        | Var String
        | Val Bool

instance Show LogicExpression where 
    show (Or e1 e2) = "(" ++ show e1 ++ " or " ++ show e2 ++ ")"
    show (And e1 e2) = "(" ++ show e1 ++ " and " ++ show e2 ++ ")"
    show (Not e1) = "(not " ++ show e1 ++ ")"
    show (Var s) = s
    show (Val False) = "0"
    show (Val True) = "1"

pushNegations :: LogicExpression -> LogicExpression
pushNegations (And a b) = And (pushNegations a) (pushNegations b)
pushNegations (Or  a b) = Or  (pushNegations a) (pushNegations b)
pushNegations (Not e) = case e of
    Val True -> Val False
    Val False ->  Val True
    Not x      -> pushNegations x
    And a b    -> Or  (pushNegations (Not a)) (pushNegations (Not b))
    Or  a b    -> And (pushNegations (Not a)) (pushNegations (Not b))
    Var _          -> Not (pushNegations e)
pushNegations e = e

bits::[[[Int]]] 
bits = iterate (\xs -> [b:bs | b <- [0,1], bs <- xs]) [[]]