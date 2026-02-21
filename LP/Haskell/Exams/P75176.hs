import Data.Ratio
import Control.Monad (forM_)

myUntil::(a->Bool)->(a->a)->a->a
myUntil p f = head . dropWhile (not . p) . iterate f

egypt::Rational -> [Rational]
egypt 0 = []
egypt r 
    |   r < 0 = (-1) % 1 : egypt (-r)       --Cambiar de signo
    |   otherwise = snd $ myUntil (\(resto, _) -> resto == 0) nextStep (r, []) 
            where 
                nextStep (x, acc) =
                    let u = ceiling (recip x) 
                        unit = 1 % u 
                    in (x - unit, acc ++ [unit])

main:: IO()
main = do 
    contents <- getContents
    let fracs = map (read :: String -> Rational) (lines contents) 
        results = map egypt fracs 
    forM_ results print 