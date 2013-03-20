package main

import "fmt"

// fibonacci returns a function that can be called to return the next number
// in the fibonacci sequence
func fibonacci() func() int {
	current := 0
	next := 1
	return func() int {
		result := current
		current, next = next, current+next
		return result
	}
}

func evenFibSum(limit int) int {
	fib := fibonacci()
	sum := 0
	for n := fib(); n <= limit; n = fib() {
		if n%2 == 0 {
			sum += n
		}
	}
	return sum
}

func main() {
	fmt.Println(evenFibSum(4000000))
}
