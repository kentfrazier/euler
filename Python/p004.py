def find_largest_palindrome(digit_length):
    if digit_length < 1:
        raise Exception('Digit length too short!')

    palindromes = []

    for i in xrange((10**digit_length)-1,(10**(digit_length-1))+1,-1):
        for j in xrange(i,(10**(digit_length-1))+1,-1):
            product = i * j
            if list(str(product)) == list(reversed(str(product))):
                palindromes.append(product)
    
    return max(palindromes)

if __name__ == '__main__':
    print find_largest_palindrome(3)
