'''
List comprehensions in Python are a concise way
to create lists by applying an expression
to each item in an iterable, all in a single line.
They’re often more readable and
efficient than using for loops to build lists.

[expression for item in iterable]
'''
##"PYTHON"
##["P","Y","T","H","O","N"]

List1=[]
for i in "PYTHON":
    List1.append(i)
print(List1)
    
print([i for i in "PYTHON"])
print([n for n in range(1,11)])


##Comprehension can be used in Transformation

list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_list=[n**2 for n in list1]
print(sq_list)

list2=["abc"  , "python" ,"hello"]

print([s.upper() for s in list2])

##Comprehension can be used in Filtering also
##[expression for item in list if condition].

list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##odd_list=[i for i in list1 if i%2!=0]
##print(odd_list)
##

'''
Dictionary comprehensions in Python are a
concise way to create dictionaries by specifying
both keys and values in a single line.
They allow us to build dictionaries
from an iterable, using the syntax
{key: value for item in iterable if condition}

,
where each key-value pair is derived from an
expression.
'''
list2=["abc"  , "python" ,"hello"]

print({i:len(i) for i in list2})

d1={"num1":10 ,"num2":12,"num3":15}

d2={}
for k,v in d1.items():
    d2[k]=v**2
print(d2)   

print({k:v for k,v in d1.items() })
d1={"num1":10 ,"num2":12,"num3":15,"num4":20}


print({k:v**2 for k,v in d1.items() if v**2>200})











