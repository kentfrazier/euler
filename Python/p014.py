# 
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

sequences = {}
sequence_lengths = {}

def get_sequence(number):
    if number == 1: return [ number ]

    global sequences

    return sequences.setdefault(number, [number] + get_sequence(next_number(number)))

def next_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3*number + 1

def longest_sequence(limit):
    seq_lengths = dict([ (n, sequence_length(n)) for n in range(1,limit) ])

    return max(seq_lengths.keys(), key=seq_lengths.get)

def sequence_length(number):
    if number == 1: return 1

    global sequence_lengths

    length = sequence_lengths.get(number)
    if not length:
        length = 1 + sequence_length(next_number(number))
        sequence_lengths[number] = length

    return length

if __name__ == "__main__":
    print longest_sequence(1000000)
