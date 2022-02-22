package main

import (
	"fmt"
	s "strings"
)

var p = fmt.Println

func chk(arr []string, inpS string) bool {

	ret := false
	var k string
 
	for _, par := range arr {

		for i, c := range inpS {
			if c == '#' {
				k  = s.Replace(inpS, string(inpS[i]) ,"",i)
				k = s.Replace(k, string(inpS[i-1]) ,"",i - 1)
			}

		}



		if s.Contains(par, k) {

			ret = true
		}

	}
	return ret
}




func main() {

	arr := []string{"1234", "5678", "8912"}

	str := "12345##"

	p(chk(arr, str))

}
