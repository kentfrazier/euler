-- A palindromic number reads the same both ways. The largest palindrome made
-- from the product of two 2-digit numbers is 9009 = 91 × 99.
--
-- Find the largest palindrome made from the product of two 3-digit numbers.

isPalindrome :: (Ord a) => [a] -> Bool
isPalindrome [] = True
isPalindrome (begin:[]) = True
isPalindrome (begin:rest) =
    if match && isPalindrome middle
        then True
        else False
        where end = last rest
              match = begin == end
              middle = init rest

largestPalindrome :: (Integral a, Ord a) => a -> Maybe a
largestPalindrome len
    | len < 1 = error "Palindromes must have a positive length."
    | otherwise = if palindromes == []
        then Nothing
        else Just $ maximum palindromes
        where minNum = 10 ^ (len - 1)
              maxNum = (10 ^ len) - 1
              multiples = [x * y | x <- [minNum..maxNum], y <- [minNum..x]]
              palindromes = filter (isPalindrome . show) multiples

main :: IO ()
main = print $ largestPalindrome 3
