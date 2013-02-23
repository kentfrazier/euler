--If we list all the natural numbers below 10 that are multiples of 3 
--or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
--
--Find the sum of all the multiples of 3 or 5 below 1000.

isMultiple :: (Integral a) => a -> a -> Bool
isMultiple number = (==0) . (`mod` number)

isMultipleOfMany :: (Integral a) => [a] -> a -> Bool
isMultipleOfMany numList n = or $ map ($ n) $ map isMultiple numList

sumMultiplesOfThreeOrFive :: (Integral a) => [a] -> a
sumMultiplesOfThreeOrFive = sum . filter (isMultipleOfMany [3, 5])

main :: IO ()
main = print $ sumMultiplesOfThreeOrFive [1..999]
