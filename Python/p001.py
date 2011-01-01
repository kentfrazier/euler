def find_multiples(limit):
    sum_of_multiples = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            sum_of_multiples += num
    return sum_of_multiples

if __name__ == "__main__":
    print find_multiples(1000)
