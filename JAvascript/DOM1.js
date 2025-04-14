
console.log(document)
// get element throgh Tagname

console.log(document.getElementsByTagName('p')[0])
console.log(document.getElementsByTagName('p')[1])


console.log(document.getElementsByTagName('h1'));

console.log(document.getElementById('par1'))

console.log(document.getElementsByClassName('heading'))

document.getElementsByTagName('h1')[0].style.color='red'

document.getElementsByClassName('heading')[1].style.border='solid black 1px'

document.getElementById('par2').style.backgroundColor='red'


//queryselector
//queryselectorAll

document.querySelector('h1').style.color='red'

document.querySelectorAll('h1')[1].style.backgroundColor='green'

document.querySelectorAll('p')[0].style.display='inline'
document.querySelectorAll('p')[1].style.display='inline'
