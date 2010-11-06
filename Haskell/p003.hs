--The prime factors of 13195 are 5, 7, 13 and 29.
--
--What is the largest prime factor of the number 600851475143 ?

primeFactors :: (Integral a) => a -> [a]
primeFactors 0 = []
primeFactors 1 = []
primeFactors num =
    if numIsPrime
        then [num]
        else factor:rest
    where options = dropWhile notMultiple $ 2:[3,5..limit]
              where notMultiple = (/=0) . (mod num)
                    limit = floor . sqrt $ fromIntegral num
          numIsPrime = options == []
          factor = head options
          rest = primeFactors $ div num factor

largestPrimeFactor :: (Integral a, Ord a) => a -> Maybe a
largestPrimeFactor num =
    if factors == []
        then Nothing
        else Just largest
    where factors = primeFactors num
          largest = foldl max 0 factors

main :: IO ()
main = print $ largestPrimeFactor 600851475143
