package main


import (


"fmt"
)




func main() {

a := make(chan int)


go func() { a <-  5  }() 


messg :=     <- a



fmt.Println(messg)




}
