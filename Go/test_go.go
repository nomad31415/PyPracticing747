package main

import "fmt"

func gorutinIt(s []int, c chan int) {

	sum := 0

	for _, v := range s {
		sum += v
	}

	c <- sum
}

func main() {

	arr := []int{1, 2, 3, 4, 5, 6, 7}

	c := make(chan int)

	go gorutinIt(arr[:len(arr)/2], c)
	go gorutinIt(arr[len(arr)/2:], c)

	x, y := <-c, <-c

	fmt.Println(x + y)

	fmt.Println("test")

}
