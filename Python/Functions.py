####A function is a block of organized,
####reusable code that performs a specific task.
####Functions make the code easier to understand.
##
##
####In python ,we define a function using the
####def keyword followed by the function name,
####parentheses (), and a colon :  .
####The code inside the function is indented,
####just like in any other block in Python.
##
##
##
##def gm():
##    print("It is inside the function block")
##
####Function only runs when it is called
##
##gm() #calling the function
##
####A function can return data as a result
##
##
##def gm():
##    print("It is inside the function")
##    return "This is returned by Function"
##print(gm())
##
##
###l1.append()
##'''
##We can pass data, known as parameters,
##into a function.
##'''
##def add(a,b): #here a,b are parameters which mean function will take 2 variables as arguments.
##    return a+b
####data can be passed into functions as arguments.
##print(add("a","i"))
##
##S=add(3,5) #3 and 5 are arguments
##print(S)
'''
A parameter is the variable listed inside
the parentheses in the function definition.

An argument is the value that is sent to the function
when it is called.
'''
def check(num):
    if num%2==0:
        return "Even Number"
    else:
        return "Odd Number"

##print(check(5))
##print(check(8))
##
##for i in range(20):
##    print(i, check(i))

##WAP to write a function which will take an integer
##and return sum of all numbers between 0 and
##given integer.


def Sum(num):
    s=0
    for n in range(1,num+1):
        s+=n
    return f"sum is {s}"
##print(Sum(10))

##cal(65,100, "+")
###+,-,*
##cal(num1,num2,operator)


list1=[2 ,100,50,12,56,900,67]

##m=0
##for num in list1:
##    if m<num:
##        m=num #m=100
##print(m)



#Default Arguments

def Subtract(num1,num2):
    return num1-num2

##print(Subtract(12,6)) #positional arguments

#keyword arguments

Subtract(num1=13 , num2=7) #keyword arguments

def Subtract(num1=100,num2=50): #default argument
    return num1-num2

##print(Subtract())


##WAP to find common elements between two lists.
list1=[12,67,99,100,50]
list2=[13,44,99,50,78]










