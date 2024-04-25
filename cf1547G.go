package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func cf1547g(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()

	var T, n, m int

	for fmt.Fscan(in, &T); T > 0; T-- {
		fmt.Fscan(in, &n, &m)
		g := make([][]int, n)
		for ; m > 0; m-- {
			var v, w int
			fmt.Fscan(in, &v, &w)
			g[v-1] = append(g[v-1], w-1)
		}

		ans := make([]int, n)
		inStack := make([]bool, n)

		var dfs func(int, bool)
		dfs = func(v int, inCycle bool) {
			inStack[v] = true
			if inCycle {
				ans[v] = -1
			} else {
				ans[v]++
			}
			for _, w := range g[v] {
				if ans[w] < 0 {
					continue
				}
				if inCycle || inStack[w] {
					dfs(w, true)
				} else if ans[w] < 2 {
					dfs(w, false)
				}
			}
			inStack[v] = false
		}

		dfs(0, false)
		for _, v := range ans {
			fmt.Fprint(out, v, " ")
		}
		fmt.Fprintln(out)
	}

}

func main() {
	cf1547g(os.Stdin, os.Stdout)
}
