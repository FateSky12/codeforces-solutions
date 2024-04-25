package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    // 打开文件
    file, err := os.Open("test_input.txt")
    if err != nil {
        panic(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)

    // 读取整数
    scanner.Scan()
    integer, _ := strconv.Atoi(scanner.Text())

    // 读取浮点数
    scanner.Scan()
    floatNumber, _ := strconv.ParseFloat(scanner.Text(), 64)

    // 读取字符串
    scanner.Scan()
    str := scanner.Text()

    // 读取空格分隔的整数数组
    scanner.Scan()
    spaceSeparated := strings.Fields(scanner.Text())
    intSlice := make([]int, 0)
    for _, val := range spaceSeparated {
        intVal, _ := strconv.Atoi(val)
        intSlice = append(intSlice, intVal)
    }

    // 读取逗号分隔的整数数组
    scanner.Scan()
    commaSeparated := strings.Split(scanner.Text(), ",")
    intSliceComma := make([]int, 0)
    for _, val := range commaSeparated {
        intVal, _ := strconv.Atoi(strings.TrimSpace(val))
        intSliceComma = append(intSliceComma, intVal)
    }

    // 打印结果以验证
    fmt.Printf("读取的整数: %d\n", integer)
    fmt.Printf("读取的浮点数: %f\n", floatNumber)
    fmt.Printf("读取的字符串: '%s'\n", str)
    fmt.Printf("读取的空格分隔整数数组: %v\n", intSlice)
    fmt.Printf("读取的逗号分隔整数数组: %v\n", intSliceComma)
}
