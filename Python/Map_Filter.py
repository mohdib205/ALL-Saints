##
##
add=lambda a,b:a+b


print(add(5,6))

##lambda s: s[-1::-1]

even=lambda x: x%2==0

print(even(5))

check=lambda x: "even" if x%2==0 else "odd"

print(check(9))

##lambda num: num%5==0

[12,67,99,100,5]  #Transformation

#map


'''
Python’s map() is a built-in function that allows
you to process and transform all the items in
an iterable without using an explicit for loop,
a technique commonly known as mapping.
map() is useful when you need to apply
a transformation function to each item
in an iterable and transform them into a new iterable.
'''
'''
Map function returns a map object.
It takes two arguments, a function and an iterable.
It appplies a given function to each item of that given
iterable.'''

def square(n):
    return n**2

list1=[90,1,3,5,7,14]
Sq_list=list(map(square , list1))

print(list1)
print(Sq_list)


list1=["abc" ,"er","qwer","hello"]

print(list(map(len,list1)))



list1=[90,1,3,5,7,14]

print(list(map(lambda x:x**2 , list1)))

price=[120,340,5000,280,5900,10000]
#10 percent discount

print(price)
disc_price=list(map(lambda p: p- p* 10/100 , price))
print(disc_price)

list1=[90,1,3,5,7,14]
list2=[100,200,3,4,5,7]

def add(a,b):
    return a+b
print(list(map(add , list1,list2)))
print(list(map(lambda a,b:a+b , list1,list2)))


##first_names=["Md","Mr","Sir" ,"Mrs"]
##last_names=["Kane","Sam","Peter","Sonia"]
##
##output:["Md Kane" , "Mr Sam" , "Sir Peter", "Mrs Sonia"]






##def x(a):
##    return a**2
##
##list1=[12,11,10,9,8,7,6,5]
##list2=[121,110,100,91,81,70,60,51]
##print(list(map(x,list1)))
##
##def summ(a,b):
##    return a+b
##print(list(map(summ,list1,list2)))






'''
Python’s filter() is a built-in function that
allows you to process an iterable and extract
those items that satisfy a given condition.
This process is commonly known as
a filtering operation.
'''

'''Filter function filters out a given
sequence by passing it
into a function returning true values
'''



def check(x):
    if x%2==0:
        return False
    else:
        return True
list1=[1,2,34,5,6,7,99,100]

##even_list=list(filter(check,list1))
even_list=list(filter(lambda a:a%2!=0,list1))

print(list1)
print(even_list)




