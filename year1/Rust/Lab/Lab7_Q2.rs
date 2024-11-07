fn fac(n: u32) -> u32 {
    println!("Caculating fac {}", n);
    println!("Value : {}, Mem address: {:p} ",n, &n );
    
    if n == 0{
        return 1;
    };
    return n * fac(n-1);
}

fn main() {
    let result = fac(5);
    print!("Result : {}", result)
}
