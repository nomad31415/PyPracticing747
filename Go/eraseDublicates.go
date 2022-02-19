package main

import (
	"fmt"
)

func Dublicates(a, b []string) []string {

	var ret []string

	mp := map[string]int{}

	a = append(a, b...)

	for _, in := range a {

		mp[in]++

	}

	for k, v := range mp {

		if v == 1 {
			ret = append(ret, k)

		}

	}

	return ret
}

func main() {

	a := []string{"abc", "dcd", "747"}

	b := []string{"abc", "747"}

	out := Dublicates(a, b)

	fmt.Println(out)

}
