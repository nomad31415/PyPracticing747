package main

import "fmt"




func main() {

arr := []int{1,2,1,3,1,2,2,4,3,5,5}

mp := make(map[int]int)


fmt.Println(arr[3])




for _,i := range arr {
mp[i]++
}



for k,v := range mp {

fmt.Println(k,v)

}



}


