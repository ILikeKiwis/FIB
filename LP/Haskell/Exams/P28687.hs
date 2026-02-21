import Data.Ratio

fact::[Integer]
fact = scanl (*) 1 [1..]

termes_cosinus::Rational -> [Rational]
termes_cosinus r = [((-1)^n) * ((r ^(2*n)) / fromInteger (fact !! (2*n))) | n <- [0..]]

cosinus::Rational -> Rational -> Rational 
cosinus alpha epsilon = sum $ takeWhile (\t -> abs t >= epsilon) (termes_cosinus alpha)