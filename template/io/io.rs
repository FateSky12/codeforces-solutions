use std::io;

// 运行程序：
// rustc io.rs && ./io < test_input.txt && rm io

fn main() {
    // 读入一个整数
    let mut input = String::new();
    println!("请输入一个整数：");
    io::stdin().read_line(&mut input).expect("读取失败");
    let number: i32 = input.trim().parse().expect("输入不是一个有效的整数");
    println!("你输入的整数是：{}", number);

    // 读入一个浮点数
    input.clear();
    println!("请输入一个浮点数：");
    io::stdin().read_line(&mut input).expect("读取失败");
    let float: f64 = input.trim().parse().expect("输入不是一个有效的浮点数");
    println!("你输入的浮点数是：{}", float);

    // 读入一个字符串
    input.clear();
    println!("请输入一个字符串：");
    io::stdin().read_line(&mut input).expect("读取失败");
    let input_str = input.trim(); // 移除可能的换行符
    println!("你输入的字符串是：{}", input_str);

    // 读入空格分隔的数组
    input.clear();
    println!("请输入一个由空格分隔的整数数组：");
    io::stdin().read_line(&mut input).expect("读取失败");
    let numbers: Vec<i32> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    println!("你输入的数组是：{:?}", numbers);

    // 读入逗号分隔的数组
    input.clear();
    println!("请输入一个由逗号分隔的整数数组：");
    io::stdin().read_line(&mut input).expect("读取失败");
    let numbers_comma: Vec<i32> = input
        .trim()
        .split(',')
        .map(|s| s.trim().parse().expect("输入项不是有效的整数"))
        .collect();
    println!("你输入的数组是：{:?}", numbers_comma);
}
