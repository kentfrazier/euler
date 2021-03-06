-- By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
-- that the 6^(th) prime is 13.
--
-- What is the 10001^(st) prime number?

import qualified Primes

nthPrime :: (Integral a) => a -> a
nthPrime n = Primes.primes!!(fromEnum $ n - 1)

main :: IO ()
main = print $ nthPrime 10001
