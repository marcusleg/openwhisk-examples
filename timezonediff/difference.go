package main

import "encoding/json"
import "fmt"
import "math"
import "os"

func main() {
	if len(os.Args) < 2 {
		os.Exit(1)
	}
	arg := os.Args[1]

	var obj map[string]interface{}
	err := json.Unmarshal([]byte(arg), &obj)

	a, ok1 := obj["a"].(float64)
	b, ok2 := obj["b"].(float64)

	var msg map[string]float64
	if err != nil || !ok1 || !ok2 {
		msg = map[string]float64{"error": -1}
	} else {
		msg = map[string]float64{"difference": math.Abs(a - b)}
	}

	res, _ := json.Marshal(msg)
	fmt.Println(string(res))
}
