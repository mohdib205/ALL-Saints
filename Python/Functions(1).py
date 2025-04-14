##A function is a block of organized,
##reusable code that performs a specific task.
##Functions make the code easier to understand.


##In python ,we define a function using the
##def keyword followed by the function name,
##parentheses (), and a colon :  .
##The code inside the function is indented,
##just like in any other block in Python.



def gm():
    print("It is inside the function block")

##Function only runs when it is called

gm() #calling the function

##A function can return data as a result


def gm():
    print("It is inside the function")
    return "This is returned by Function"
print(gm())


#l1.append()
'''
We can pass data, known as parameters,
into a function.
'''
def add(a,b): #here a,b are parameters which mean function will take 2 variables as arguments.
    return a+b

##data can be passed into functions as arguments.


S=add(3,5) #3 and 5 are arguments
print(S)
'''
A parameter is the variable listed inside
the parentheses in the function definition.

An argument is the value that is sent to the function
when it is called.
'''








