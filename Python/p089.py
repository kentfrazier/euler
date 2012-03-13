"""
The rules for writing Roman numerals allow for many ways of writing each number
(see About Roman Numerals...). However, there is always a "best" way of writing
a particular number.

For example, the following represent all of the legitimate ways of writing the
number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least
number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
contains one thousand numbers written in valid, but not necessarily minimal,
Roman numerals; that is, they are arranged in descending units and obey the
subtractive pair rule (see About Roman Numerals... for the definitive rules for
this problem).

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.
"""

VALUES = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
)
VALUE_MAP = dict(VALUES)

def parse_roman_numeral(numeral):
    numeral = numeral.upper()
    total = 0
    previous = 0
    for char in numeral:
        current = VALUE_MAP[char]
        total += current
        if current > previous:
            total -= 2 * previous
        previous = current
    return total

def generate_roman_numeral(number):
    chunks = []
    for numeral, value in VALUES:
        count, number = divmod(number, value)
        chunks.append(numeral * count)
    return ''.join(chunks)

def main():
    saved = 0
    with open('roman.txt', 'r') as f:
        for line in f:
            numeral = line.strip()
            value = parse_roman_numeral(numeral)
            canonical = generate_roman_numeral(value)
            saved += len(numeral) - len(canonical)
    print saved

if __name__ == '__main__':
    main()
