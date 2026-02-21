main::IO()
main = do 
    contents <- getContents
    let enters = words contents
        n = map read enters
    print . sum $ n