import Distribution.Simple.BuildToolDepends (getAllInternalToolDependencies)
data Temps = Temps Int Int
data Arbre a = Arbre a [Arbre a]

instance Show Temps where 
    show (Temps a b) = mos a ++ ":" ++ mos b
        where 
            mos x = if x < 10 then '0':show x else show x 

suma::Temps->Temps->Temps
suma (Temps h1 m1) (Temps h2 m2) = Temps (mod (h1+h2 + div (m1+m2) 60 ) 100 ) (mod (m1+m2) 60)

sumes::[Temps]->Temps
sumes = foldr suma (Temps 0 0) 

sumesArbre::Arbre Temps -> Temps
sumesArbre (Arbre (Temps h m) l)= suma (Temps h m) (sumes (map sumesArbre l))


main::IO()
main = do 
    line <- getLine 
    let temps = map parseTemps (words line)
    print (sumes temps)

parseTemps::String -> Temps
parseTemps s = 
    let (hStr, _:mStr) = span (/= ':') s
    in Temps (read hStr) (read mStr)