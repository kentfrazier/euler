module Primes
( primeFactors
, primes
, isPrime
) where

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

primes :: (Integral a) => [a]
primes = (:) 2 $ filter isPrime [3,5..]

isPrime :: (Integral a) => a -> Bool
isPrime num = all ((/=0) . (mod num)) possibilities
    where limit = floor . sqrt $ fromIntegral num
          possibilities = takeWhile (<= limit) primes
