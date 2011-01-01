def fibonacci_list(limit):
    fib_list = []
    i = 0
    while True:

        if i < 2:
            fib = i
        else:
            fib = fib_list[i-1] + fib_list[i-2]

        if fib > limit: break

        fib_list.append(fib)
        
        i += 1

    return fib_list

def sum_even(seq):
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False

    return sum(filter(is_even,seq))

def even_fib_sum(limit):
    return sum_even(fibonacci_list(limit))

if __name__ == "__main__":
    print even_fib_sum(4000000)
