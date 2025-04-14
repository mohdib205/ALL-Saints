console.log("Hello World ") 
console.log(12345666) 

console.log(typeof('12.9'))
// this is a comment 

/* this
is multi 
line 
comment
*/

// let, var and const


d=1000
console.log(d)

d=8
console.log(d)


var a=3
console.log(a)

var a=3
console.log(a)

let b=5
console.log(b)

//let b=2 //it will raise error
//console.log(b)

b=58
console.log(b)


const c='hello'
console.log(c)

//c='a'  //it will raise an error
//console.log(c)


// conditional operatpors

let num1=100
let num2=20

console.log(num1>num2)


// Difference between == and ===

num1=100
num2=90
num3= '100'

console.log(num1==num2)
console.log(num1==num3)

console.log(num1===num3)



// + , - , % , ** 

// || && 


// if else 

//if   else if   else 

if (a>6){
 console.log("a is greater than 6")
}
else {
console.log("a is not greater than 6")
}

num1=10

if (num1 % 2==0 && num1 % 3==0){

console.log("divisible by both") }

else if (num1%2==0){
console.log("divisible by 2")
}

else{
console.log("divisible by 3")
}



//alert("Check your internet")

a= +(prompt("enter your name"))
//	a= parseInt(prompt("enter your name"))


console.log(a , typeof(a))
