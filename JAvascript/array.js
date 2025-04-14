// console.log('hello')
// Array in Javascript - used to store collection of elements

// let myArr = [20,30,40,50,60,70]
// console.log("Array:",myArr)

// Index - Accessing elements by their position
// console.log("First Element:",myArr[0])
// console.log(myArr[4])
// console.log(myArr[1])

// console.log("Length of an Array:",myArr.length)

// string array
// let stringArray = ['dog', 'lion', 'horse', 'camel', 'bear']
// console.log(stringArray)

// array with multiple data types
// multArray = ['a',"a",'B',34, 35.7, true]
// console.log(multArray)

// --------------------------------------------------------------------------
// ARRAY METHODS-
// let array1 = ['rose', 'lotus', 'marigold', 'lily', 'sunflower']
// console.log(array1)


// slice - It is used to extract a portion of an array into a new array. 
//         It does not modify the original array, it returns a new array.
// console.log(array1.slice(1,3))
// console.log(array1.slice(0,4))


// indexOf - It helps to find the index of the first occurrence of a specified 
//           element within an array.
// console.log(array1[3])
// console.log(array1.indexOf('lily'))


// push - Adds element to the end of an array
// array1.push('tulip')
// console.log(array1)
// adding multiple elements 
// array1.push('jasmine','hibiscus')
// console.log(array1)


// pop - Remove elements from an array
// array1.pop()
// console.log(array1)


// Shift - removes first element from an array
// array1.shift()
// console.log(array1)


// unshift - adds element at the start of an array
// array1.unshift('lavender')
// console.log(array1)


// includes - checks whether an element is present or not
// console.log(array1.includes('lotus'))
// console.log(array1.includes('daisy'))


// join - joins elements of an array into a string using a delimiter (a separator)
// let sentence = ['Hello', 'Everyone', 'Good', 'Morning']
// console.log(sentence)
// console.log(sentence.join(' '))


// split - splits a string into an array of elements at a specified separator
// let a = 'Good Evening Good Morning Everyone'
// console.log(a)
// console.log(a.split(' '))


// concat - It is used to combine arrays
// let wild_animal = ['lion', 'tiger', 'zebra']
// let pet_animal = ['horse', 'camel', 'cow']
// let birds = ['sparrow', 'crow', 'peacock']
// console.log(wild_animal.concat(pet_animal,birds))
//
// z = wild_animal.concat(pet_animal)
// console.log(z)


// splice - It changes the contents of an array by removing, 
//          replacing, or adding elements at a specific index.

let colors = ["red", "green", "blue", "yellow", "brown", "black"]
console.log(colors)

// removes two elements starting from index 1.
// colors.splice(1, 2)
// console.log(colors)

// inserts "pink" at index 2, without removing any elements.
// colors.splice(2, 0, "pink")
// console.log(colors)

// // inserts "orange" and "purple" at index 1, replacing two elements.
// colors.splice(1, 2, "orange", "purple")
// console.log(colors)


// sort - sorts array
// let strArray = ['b','z','i','a','m','s','y']
// console.log(strArray.sort())

// let numArray = [2, 5, 30, 1, 6, 8, 9, 4, 7, 10, 100000000]
// console.log(numArray.sort())

// reverse - reverses an array
// console.log(strArray.reverse())
// console.log(numArray.reverse())




