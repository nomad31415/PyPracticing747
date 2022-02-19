package main

import (
	"fmt"
	"strings"
)

func Dublicates(a, b []string) []string {

	var ret []string

	mp := map[string]int{}

	a = append(a, b...)

	ss :=   strings.Join(b, " ")
	fmt.Println(ss)

	for _, in := range a {

		mp[in]++

	}

	for k, v := range mp {

		if v == 1  &&  strings.Index(ss, k) > 0  {
			ret = append(ret, k)

		}

	}

	return ret
}

func main() {

	a := []string{"abc", "dcd", "747"}

	b := []string{"abc", "747","kkk"}

	out := Dublicates(a, b)

	fmt.Println(out)

}
