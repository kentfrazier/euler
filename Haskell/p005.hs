-- 2520 is the smallest number that can be divided by each of the numbers from 1 
-- to 10 without any remainder.
-- 
-- What is the smallest positive number that is evenly divisible by all of the 
-- numbers from 1 to 20?

import qualified Data.List as List
import qualified Data.Map as Map

import qualified Primes

factorMap :: (Integral a) => a -> Map.Map a Int
factorMap num = Map.fromList . pairs . List.group $ Primes.primeFactors num
    where makePair list@(n:_) = (n, length list)
          pairs = map makePair

smallestDivisibleByList :: (Integral a) => [a] -> a
smallestDivisibleByList list = product perfestPowerFactors
    where factorMaps = Map.unionsWith max $ map factorMap list
          perfestPowerFactors = [n ^ p | (n, p) <- (Map.toList factorMaps)]

smallestDivisibleByRange :: (Integral a) => a -> a -> a
smallestDivisibleByRange minNum maxNum =
    smallestDivisibleByList [minNum..maxNum]

main :: IO ()
main = print $ smallestDivisibleByRange 1 20
