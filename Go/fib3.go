package main



import "fmt"



func  ffb(n int) int {

	x, y := 0,1


	for i:= 0;i < n ; i++ {
		x, y = y , x + y

	}

	return x


}



func  main() {

var n  int 

for {	
fmt.Scan(&n)

if n == 777 {
	break
}


fmt.Println(ffb(n))
}






}
