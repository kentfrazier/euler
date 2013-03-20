package main

import "fmt"

func fibonacci(c chan int) {
	current := 0
	next := 1
	for {
		c <- current
		current, next = next, current+next
	}
}

func evenFibSum(limit int) int {
	c := make(chan int)
	sum := 0

	go fibonacci(c)
	for n := range c {
		if n > limit {
			break
		}
		if n%2 == 0 {
			sum += n
		}
	}
	return sum
}

func main() {
	fmt.Println(evenFibSum(4000000))
}
