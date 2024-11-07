use core::fmt;
use std::fmt as other_fmt;

struct BoxedStack{
    data:Box<Vec<i32>>
}

// function
impl BoxedStack {
    fn new() -> Self{
        BoxedStack {
            data:Box::new(Vec::new()),
        }
    }

    fn push(&mut self, value: i32){
        self.data.push(value)
    }

    fn pop(&mut self) -> Option<i32>{
        self.data.pop()
    }

    fn peek(&self) -> Option<&i32> {
       self.data.last() 
    }

    fn is_empty(&self) -> bool {
        self.data.is_empty()
    }

    fn print_stack(&self) {
        for element in self.data.iter().rev(){
            println!("{}", element)
        }
    }
}

impl std::fmt::Debug for BoxedStack {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>,) -> fmt::Result {
        write!{f,"BoxedStack {{ data {:?} }}", self.data}
    }
}

fn main() {

    let mut st = BoxedStack::new();

    st.push(10);
    st.push(20);
    st.push(30);
    st.print_stack();
    st.peek();
    st.pop();
    st.print_stack();
    st.pop();
    st.print_stack();
    st.pop();
    st.print_stack();
    st.is_empty();

}