##Python Module is a file that contains
##built-in functions, classes,its and variables



##It is a built-in python module used to perform
##random actions.

##This module can be used to perform
##random actions such as generating random numbers,
##printing random a value for a list or string, etc

#first we have to import the module
import random

## random.randrange() returns a random number
##within a given range

ran_num=random.randrange(1,10)
print(ran_num)
list1=[]
for i in range(20):
    list1.append(random.randint(1,50))
print(list1)

#randrange 

#randint

#choice() Returns a random element from the given sequence
#choices() 	Returns a list with a random selection from the given sequence

str1="abcdefgh"
print(random.choice(str1))

list1=[100,300,400,True,3.8]
print(random.choice(list1))

str1="abcdefgh"
print(random.choices(str1 ,k=3))
print(random.choices(list1, k=2))











