// console.log('hello')

// --------------------------------------------------------

// map function - Map function is applied on a given array by passing 
//                each of its elements into a callback function used
//                and returns a new array 

let NumArr = [1,2,3,4,5,6,7,8,9,10]

// NORMAL FUNCTION
// function cube(n){
//     return n*n*n
// }

// cubeArr = NumArr.map(cube)
// console.log(cubeArr)

// Arrow function example
// console.log(NumArr.map((n)=>n**2))

// adding all the elements of NumArr with 10
// console.log(NumArr.map((n)=>n+10))

// to print the table of user inputted number using map
// let num = parseInt(prompt())
// console.log(NumArr.map((n)=>n*num))

// to convert a number array into a string array
// console.log(NumArr.map((n)=>String(n)))

// let strNum = ['10','20','30','40','50']
// console.log(strNum.map((n)=>parseInt(n)))

// to calculate the length of elements of a string array 
// let stringArray = ['car', 'pencil', 'bottle', 'bag']
// console.log(stringArray.map((n)=>n.length))

// --------------------------------------------------------
// forEach() - It does not returns a new array but applies a given 
//             function to each element within an array

// let a = [1,2,3,4,5]
// console.log(a.map((n)=>n*10))

// a.forEach((n)=>console.log(n*10))

// As forEach does not returns the result in the form of an array,
// therefore we will insert the elements into a new array using .push()

// newArr = []
// a.forEach((n)=>{
//     console.log(n*4)
//     a.push(n*4)
// })
// console.log(newArr)

// difference between map and forEach 
// map returns a new array while forEach does not returns a new array

// --------------------------------------------------------
// filter function - It used to return a new array of filtered elements
// by applyimg each element of a given array to a callback function.

// filtering even numbers
// console.log(NumArr.filter((n)=>n%2==0))

// filtering odd numbers
// console.log(NumArr.filter((n)=>n%2!=0))

// MarksArr = [76, 62, 31, 45, 85, 36, 90, 74]
// console.log(MarksArr.filter((n)=>n>33))

// -----------------------------------------------

// find method - find method returns the value of first element in 
// an array which satisfies a condition

let year = [2002, 2012, 1998, 1990, 2003, 1989, 1992, 1982, 2005]
console.log(year)

// console.log("Result of find:",year.find((n)=>n<2000))
// console.log("Result of filter:",year.filter((n)=>n<2000))

// find index - returns the index of the first element in an array that 
//              satisfies a provided condition.

// console.log("Result of findIndex:",year.findIndex((n)=>n==1992))

// -----------------------------------------------
// let Array1 = [9000, 2000, 3500, 6000, 2500, 7000, 6800, 8300]

// console.log(Array1.filter((n)=>n<5000))
// console.log(Array1.find((n)=>n<5000))
// console.log(Array1.findIndex((n)=>n<5000))

// ------------------------------------------------------
// reduce method - it reduces all the elements of a given array and
//                  returns a single value

// let Array2 = [1,2,3,4,5]

// console.log(Array2.reduce((a,b)=>a*b))
// console.log(Array2.reduce((a,b)=>a+b))

// --------------------------------------------------
// replace method - string method to repalce the first occurence
// let aString = 'Hello World, this World'
// console.log(aString.replace('World', 'Everyone'))

// let week = "Monday, Tuesday, Monday, Sunday"
// console.log(week.replace('Monday', 'Wednesday'))

