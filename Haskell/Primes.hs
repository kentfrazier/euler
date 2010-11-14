module Primes
( primeFactors
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
