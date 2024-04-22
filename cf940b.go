package main

import (
	"fmt"
	"io"
	"os"
)

func cf940b(in io.Reader, out io.Writer) {
	var n, k, a, b, res int
	fmt.Fscan(in, &n, &k, &a, &b)
	for n > 1 {
		res += n % k * a
		n -= n % k
		if (n-n/k)*a < b {
			res += (n - 1) * a
			break
		}
		res += b
		n /= k
	}
	fmt.Fprint(out, res)
}

func main() {
	cf940b(os.Stdin, os.Stdout)
}
