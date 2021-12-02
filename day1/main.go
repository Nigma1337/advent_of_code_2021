package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

func main(){
	dat, err := readLines("input.txt");
	if err != nil {
        panic(err);
    }
	res := 0;
	current := 0;
	for i := range dat{
		a, err := strconv.Atoi(dat[i]);
		if err != nil {
			panic(err);
		}
		if a > current{
			res++;
		}
		if err != nil {
			panic(err);
		}
		current = a;
	}
	fmt.Println(res);
	res = 0;
	for i := range dat{
		if i+4>len(dat){
			break
		}
		current, err := strconv.Atoi(dat[i]);
		if err != nil {
			panic(err);
		}
		three, err := strconv.Atoi(dat[i+3])
		if err != nil {
			panic(err);
		}
		if current<three{
			res++;
		}
	}
	fmt.Println(res);
}