package main

import (
	"fmt"
	"time"
	)

	func portal2(channel2 chan string) {
	time.Sleep(5*time.Second)
	channel2 <- "Welcome to channel 2"
	}



	func main() {
	fmt.Println("Hello, playground")
	ch1 := make(chan string)
	go portal2(ch1)

	select {
		case res:=   <- ch1:
		fmt.Println(res)
													}
													}

