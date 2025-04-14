'''
The *args parameters allows a function to accept
any number of positional arguments.

Inside the function, args is treated as a
tuple of the passed arguments.
'''
def function(*args):
    return args

print(function(1,2,7,67,980))

def Sum(*num):
    s=0
    for n in num:
        s+=n
    return s
print(Sum(1))
print(Sum(100,34,4,50,23 ,24,25))


    


'''
**kwargs allows for any number of keyword arguments
as a dictionary.

Inside the function, kwargs is treated
as a dictionary where the keys are the argument names
and the values are the argument values.
'''
def function2(**kwargs):
    return kwargs
print(function2(name1="Isuf" , name2="Saklen") )

def Students(**info):
    for k,v in info.items():
        print( f"{k} is {v}")
    return info
print(Students(name="Isuf" , semester=3) )




#One line  Function

##A lambda function is a small anonymous function
##A lambda function can take any number of arguments,
##but can only have one expression.


square=lambda a:a**2
print(square(4))

even=lambda num: num%2==0
print(even(12))
capital=lambda s: s.upper()
print(capital("python"))

Sums=lambda x,y,z:x+y+z
print(Sums(10,20,30))




