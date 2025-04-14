// prime number
num1=21

a=true


for (i=2; i<num1; i++){
if (num1%i==0){
console.log("not a prime number")
a= false
break
}
}
console.log(i)

if (i== num1 ){
console.log("it is a prime number")

}


if (a){
console.log("it is a  prime number")
}
else{
console.log("it is not a prime number")
}


//  splice(index , remove , insertElement)

//array1=[100,200,300,400 , 500, 600 , 700]
// remove 
//console.log(array1.splice(1,1, 1000 ,20000,999,8000))
//console.log(array1)

//console.log(array1.splice(1,2))
//console.log(array1)


//remove elements from an array which are divisible by 3,5 both...

//print the table of 6 in an array form

//template literals backticks 
a=0
console.log("value of a is " + a)

console.log(`value of a is ${a}`)

var num1=10
let num2=15

console.log(`sum of ${num1} and ${num2} is ${num1+num2}`)



// object

obj1={ 'name':'ibrahim' , 'sem':3 , 'year':2}
console.log(obj1)

console.log(obj1['name'])

obj1['name']='saklen'
console.log(obj1)

obj1['branch']='CSE'

console.log(obj1)

console.log(Object.keys(obj1))
console.log(Object.values(obj1))

console.log(Object.entries(obj1))


for (i=0; i<Object.entries(obj1).length ; i++){
console.log(Object.entries(obj1)[i])
}





































