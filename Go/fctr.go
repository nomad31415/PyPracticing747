package main


import "fmt"




func fac(n int) int {

	s := 1

	for i:= 1;i <= n ; i++ {
	
	s*= i



	}


return s

}




func main() {

var n int


fmt.Scan(&n)


fmt.Println(fac(n))




}




