def sum_of_squares(limit):
	return sum([n**2 for n in range(1,limit+1)])

def square_of_sum(limit):
	return sum(range(1,limit+1))**2

def diff_sum_of_squares_and_square_of_sum(limit):
	return abs(sum_of_squares(limit) - square_of_sum(limit))

if __name__ == "__main__":
	print diff_sum_of_squares_and_square_of_sum(100)
