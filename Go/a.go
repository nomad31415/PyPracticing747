package main


import "fmt"



func main() {

const (

a = iota
b
c

)

fmt.Println("c=",c)

fmt.Println(a)




var a1 [3]int // [0,0,0]
fmt.Println("a1 short", a1)
fmt.Printf("a1 short %v\n", a1)
fmt.Printf("a1 full %#v\n", a1)



}


