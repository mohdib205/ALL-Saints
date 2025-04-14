'''
 range() returns a sequence of numbers
 Syntax: range(start, stop, step)
 Default start is 0, step is 1
 Negative step for reverse order
'''
##list , tuple , set ,dict
print(list(range(-100,101)))

print(tuple(range(1,100,5)))

##100 1
##(100,99,98,97,96....1)
print(list(range(100,0,-1)))

#1-50 even numbers with the help of range
#step size 2
print(tuple(range(1,50,2)))

print(list(range(30))) #0 to 30


'''
Iteration is the repeated execution of a process in
loops. Each pass through a loop is called an iteration,
it allows automatic handling of
multiple items without manual repetition.
'''





#Iterables
'''
Iterables in Python are objects that can be
looped over or iterated through. Examples are List
,Tuple, set, range, string etc'''

#For loop
'''
A for loop allows to repeat a block of code
for each item in a collection,
such as a list or string.
'''
##
for i in range(0,10):   
    print("Hello World")
##
for i in range(0,10):   
    print(i)
####1,50 even numbers 
##
for num in range(50):
    if num%2==0:
        print(num)

#50,100 odd numbers


#0, 50
'''Q1
WAP to separate even and odd numbers from 0 to 50
into two lists:even_nums and odd_nums,
and then print both lists.
'''
even_nums=[]
odd_nums=[]

for i in range(51):
    if i%2==0:
        even_nums.append(i)
    else:
        odd_nums.append(i)
print(even_nums)
print(odd_nums)

'''Q3
WAP to separate integers and strings
from a mixed list into two lists:
numbers for integers and strings
for strings, then print both lists.
'''

list1=[100,"a",90 , 23, "12i" , "hello"]
strings=[]
numbers=[]

for i in list1:
    if type(i)==str:
        strings.append(i)
    elif type(i)==int:
        numbers.append(i)

'''Q4
Given a list of numbers,
WAP to separate numbers
that are multiples of 3 into a list multiples_of_3
and the rest into a list non_multiples.
'''

'''Q5
Given a list of strings,
WAP to separate strings based on their lengths:
even_length for strings with even lengths and odd_length for strings with
odd lengths.
'''
        























