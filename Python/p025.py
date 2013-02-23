# What is the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci(limit=float('Inf')):
    yield 1
    yield 1

    one_back = two_back = 1

    fib = 0
    while fib < limit:
        fib = one_back + two_back
        yield fib

        two_back = one_back
        one_back = fib

def count_digits(n):
    return len(str(n))

def first_fib_to_n_digits(n):
    fibs = fibonacci()

    count = 0
    while True:
        count += 1
        fib = fibs.next()
        if count_digits(fib) >= n:
            break

    return count

if __name__ == "__main__":
    print first_fib_to_n_digits(12)
    print first_fib_to_n_digits(1000)
