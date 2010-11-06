--The prime factors of 13195 are 5, 7, 13 and 29.
--
--What is the largest prime factor of the number 600851475143 ?

primeFactors :: (Integral a) => a -> [a]
primeFactors 1 = []
primeFactors 2 = [2]
primeFactors 3 = [3]
primeFactors num = if numIsPrime then [num] else factor:rest
    where limit = floor . sqrt $ fromIntegral num
          notMultiple = (/=0) . (mod num)
          options = dropWhile notMultiple $ 2:[3,5..limit]
          numIsPrime = options == []
          factor = head options
          rest = primeFactors $ div num factor

largestPrimeFactor :: (Integral a, Ord a) => a -> a
largestPrimeFactor num = foldl max 0 $ primeFactors num

main :: IO ()
main = print $ largestPrimeFactor 600851475143
