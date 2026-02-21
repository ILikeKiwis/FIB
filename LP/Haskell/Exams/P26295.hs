import Data.List 

main::IO()
main = do
    contents <- getContents
    let paraules = words contents
        compte = map (\ps -> (head ps, length ps)) . group . sort $ paraules
    mapM_ (\(p, n) -> putStrLn (p ++ " " ++ show n)) compte

