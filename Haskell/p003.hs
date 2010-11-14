--The prime factors of 13195 are 5, 7, 13 and 29.
--
--What is the largest prime factor of the number 600851475143 ?

import Primes

largestPrimeFactor :: (Integral a, Ord a) => a -> Maybe a
largestPrimeFactor num =
    if factors == []
        then Nothing
        else Just largest
    where factors = primeFactors num
          largest = foldl max 0 factors

main :: IO ()
main = print $ largestPrimeFactor 600851475143
