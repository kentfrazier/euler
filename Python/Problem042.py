# The n^(th) term of the sequence of triangle numbers is given by,
# t_(n) = # (1/2)*n*(n+1); so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its 
# alphabetical position and adding these values we form a word value. For 
# example, the word value for SKY is 19 + 11 + 25 = 55 = t_(10). If the word 
# value is a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
# containing nearly two-thousand common English words, how many are triangle 
# words?

from Problem022 import char_values

def triangle(n):
    return (n * (n + 1)) // 2

def triangle_numbers(limit):
    for n in xrange(1,limit):
        yield triangle(n)

def word_value(word):
    return sum([ char_values[letter] for letter in word ])

def word_list(filename):
    f = open(filename)
    words = eval( '[' + f.read() + ']' )
    f.close()

    return words

def triangle_words(word_list):
    max_num = 26 * max([ len(word) for word in word_list ])

    triangles = list(triangle_numbers(max_num))

    return [ word for word in word_list if word_value(word) in triangles ]

if __name__ == "__main__":
    words = word_list('words.txt')
    print len(triangle_words(words))
