# Using names.txt (right click and 'Save Link/Target As...'), a 46K
# text file containing over five-thousand first names, begin by sorting
# it into alphabetical order. Then working out the alphabetical value
# for each name, multiply this value by its alphabetical position in 
# the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the 
# list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?

f = open('names.txt')
names = [ name.strip('"') for name in f.read().split(',') ]
f.close()

names.sort()

char_values = dict([ (chr(n+64),n) for n in range(1,27) ])

total = 0

if __name__ == "__main__":
    for i in xrange(len(names)):
        name_val = sum([ char_values[c] for c in names[i] ])
        name_val *= i+1

        total += name_val

    print total    
