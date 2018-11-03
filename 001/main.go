package main

import (
	"fmt"
)

func main() {
	var i int
	var result int
	result = 0
	for i = 0; i < 1000; i++ {
		if multiple(i) {
			result += i
		}
	}
	fmt.Println(result)
}

func multiple(i int) bool {
	if (i%3 == 0) || (i%5 == 0) {
		return true
	}
	return false
}
