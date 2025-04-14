//innerHTML
// innerText
// //TextContent
console.log(document.getElementsByTagName('div')[0].innerHTML)

console.log(document.getElementsByTagName('div')[0].innerText)

console.log(document.getElementsByTagName('div')[0].textContent)

document.getElementsByTagName('div')[1].innerHTML="<h1>thiss iss chilld 1 replaced text</h1>"


document.getElementById('child2').style.display='none'

console.log(document.getElementsByTagName('div')[0].getAttribute('class'))
document.getElementsByTagName('div')[0].setAttribute("id", 'parentId')
//events

function button1(){
let text1= document.getElementById('inp1').value
document.getElementsByTagName('div')[1].innerHTML=text1
document.getElementById('inp1').value=''
}

function change_color(color){
    document.getElementById('btn2').style.backgroundColor=color
}

function add(){
    // console.log( typeof(document.getElementById('counter').innerText));
    val=+(document.getElementById('counter').innerText)
    val++
    document.getElementById('counter').innerText= val
    
}

function reduce(){
    
    // console.log( typeof(document.getElementById('counter').innerText));
    val=+(document.getElementById('counter').innerText)
    if (val>0){
    val--
    document.getElementById('counter').innerText= val
    }
    
}




// button1.addEventListener(event , function)

// b1= document.querySelector('button')
// console.log(b1);
// b1.addEventListener('click' , console.log("buttonnn "))
// b1.