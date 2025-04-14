// Functions in JS
// Reusable block of code that can be executed whenever it is called
// It returns a value

// creating our own functions-

// function greet(){
//     console.log('hello')
// }

// greet()

// function returns a value
// function greet2(){
//     return 'hello world'
// }

// let a = greet2()
// console.log(a)

// console.log(greet2())

// -------------------------------------
// Sum Function-
// function Sum(a,b){
//     return (a+b)
// }
// console.log(Sum(4,5))
// let n = Sum(7,8)
// console.log(n)

// Product Function-
// function product(a,b){
//     return a*b
// }
// product(7,10)      //will not print the output 
// console.log(product(7,10))         //will prints the output


// -----------------------------

// Even Function-
// function even(n){
//     if(n%2==0){
//         return 'Even'
//     }
//     else{
//         return 'Not Even'
//     }
// }

// console.log(even(10))
// console.log(even(11))

// user input
// let num = parseInt(prompt("Enter a number:"))
// console.log(even(num))

// odd function-

// function Odd(n){
//     if(n%2 != 0){
//         return 'Odd'
//     }
//     else{
//         return 'Even'
//     }
// }

// let num = parseInt(prompt())
// console.log(Odd(num))


// to calculate the sum of n natural numbers

// function SumOfN(m,n){
//     let sum = 0
//     for (i=m; i<=n; i++){
//         sum = sum+i
//     }
//     return sum
// }

// console.log(SumOfN(1,50))
// console.log(SumOfN(100,150))


// --------------------------------------------

// arrow functions - Arrow functions provide a concise syntax for 
//                 writing functions in JavaScript. The function 
//                 implicitly returns the expression following the 
//                 arrow symbol. It is written like this - ()=>{}

// let greet = ()=> 'Hello World'
// console.log(greet())

// let wish = (val) => 'hello ' + val
// console.log(wish('everyone'))

// let add = (a,b)=> a+b
// console.log(add(3,7))

// let prod = (x,y)=> {return x*y}
// console.log(prod(6,7))

// let square = (n) => {console.log(n*n)}
// square(7)
// square(3)

// let Square = (n)=> n*n
// console.log(Square(5))

// -----------------------------------------
// Multiple lines of code using arrow function
// let Even_odd = (n) => {
//     if (n%2==0){
//         return 'even'
//     }
//     else{
//         return 'odd'
//     }
// }
// console.log(Even_odd(20))

// check for even using arrow function in one line

// let even = (n) => n%2==0
// console.log(even(20))

// let odd = (n) => n%2!=0
// console.log(odd(11))

// Sort Function using string array
// months = ['January', 'April', 'December', 'Zoo', 'May', 'March']
// console.log("Sorted Array:",months.sort())
// console.log("Reversed Array:",months.reverse())

// Sort Function using number array
// ascending order
// function Comparison(a,b){
//     return a-b
// }

// NumArray = [23, 45, 1000, 632, 89, 9, 50]
// console.log(NumArray.sort(Comparison))

// descding order
// NumArray = [23, 45, 1000, 632, 89, 9, 50]
// console.log(NumArray.sort((a,b)=>b-a))

// array of mixed values
// myArray = ['s', 'a', 'd',true, 'Z', 'J', 76, 'm']
// console.log("Original Array:", myArray)
// console.log("Sorted Array:",myArray.sort())



