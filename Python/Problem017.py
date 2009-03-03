# If the numbers 1 to 5 are written out in words: one, two, three, four, 
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written 
# out in words, how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred 
# and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. The use of "and" when writing out numbers is in 
# compliance with British usage.

class Numbers(object):
    def __init__(self):
        self.ones = {
            '0': '',
            '00': '',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '10': 'ten',
            '11': 'eleven',
            '12': 'twelve',
            '13': 'thirteen',
            '14': 'fourteen',
            '15': 'fifteen',
            '16': 'sixteen',
            '17': 'seventeen',
            '18': 'eighteen',
            '19': 'nineteen',
        }
        self.tens = {
            '2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety',
        }
        self.places = {
            2: 'hundred',
            3: 'thousand',
        }
numbers = Numbers()

def spell_out(number, place=0):
    digits = list(str(number))
    num_list = []

    if place != 0:
        num_list.append(numbers.places[place])

    tail = digits[-2:]
    if tail[0] == '0': tail = tail[1]
    if int(''.join(tail)) < 20:
        num_list.append(numbers.ones[''.join(tail)])
    else:
        num_list.extend([numbers.ones[tail[1]],numbers.tens[tail[0]]])

    if len(digits) > 2 and digits[-3] != '0':
        if int(''.join(tail)) != 0:
            num_list.append('and')
        num_list.append(spell_out(digits[-3],2))

    if len(digits) > 3:
        num_list.append(spell_out(''.join(digits[0:-3]),place + 3))

    return ''.join(reversed(num_list))

if __name__ == "__main__":
    total_length = 0
    for number in range(1,1001):
        total_length += len(spell_out(number))

    print total_length
