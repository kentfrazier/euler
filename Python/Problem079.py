# A common security method used for online banking is to ask the user for 
# three random characters from a passcode. For example, if the passcode was 
# 531278, they may asked for the 2nd, 3rd, and 5th characters; the expected 
# reply would be: 317.
# 
# The text file, keylog.txt, contains fifty successful login attempts.
# 
# Given that the three characters are always asked for in order, analyse the 
# file so as to determine the shortest possible secret passcode of unknown 
# length.

def break_code(entries):
    class Code_Digit(object):
        def __init__(self, value):
            self.value = value
            self.lt = set()
            self.gt = set()

        def __lt__(self, other):
            if self.value in other.lt or other.value in self.gt:
                return True
            return False

        def __gt__(self, other):
            if self.value in other.gt or other.value in self.lt:
                return True
            return False

        def __eq__(self, other):
            if self.value == other.value:
                return True
            return False

        def __cmp__(self, other):
            if self > other:
                return 1
            elif self < other:
                return -1
            else:
                return 0

    digits = dict()
    for entry in entries:
        for i in range(len(entry)):
            digit = digits.setdefault(entry[i], Code_Digit(entry[i]))
            digit.lt |= set(entry[:i])
            digit.gt |= set(entry[i+1:])

    return ''.join([ digit.value for digit in sorted(digits.values()) ])

if __name__ == "__main__":
    f = open('keylog.txt')
    entries = [ entry.strip() for entry in f.readlines() ]
    f.close()

    print break_code(entries)
