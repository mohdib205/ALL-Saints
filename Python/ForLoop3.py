####WAP to print the multiplication table of a number
####provided by the user.
##
####WAP that counts how many vowels (a, e, i, o, u)
####are in a given string.



###WAP to find the sum of digits of a given number.

##123%10==3
##s+=3
##
##123//10=12
##
##12%10==2
##
##12//10=1
##
##1%10=1



num=1235  
s=0

for i in range(len(str(num))):
    mod=num%10
    s+=mod
    num=num//10
print(s)







dict1={"num1":12 , "num2":34}
dict1["num3"]=12
##print(dict1["num1"])

for i in dict1:
    print(i , dict1[i])

for key,value in dict1.items():
    print("key is " ,key)
    print("value is ",value)
list1=["Hello" , 12,90,True , "Bhopal",100]

for i in range(0,len(list1)):
    print(i ,list1[i])
    
for i,e in enumerate(list1):
    print(i , e)
##    
list1=["Hello" , 12,90,True , "Bhopal",100]
list2=[23 , 12,90,False , "Friday",60]

for l1,l2 in zip(list1,list2):
    print(l1 , l2)

#Q1
##given a list l1=[250,500,650,700]
##make dictionary with keys as indices of l1 and values
##as elements of l1.
##Output: {0:250,1:500,2:650,3:700}

##dict1[0]=250
##dict1[1]=500
##dict1[2]=650
##dict1[3]=700
l1=[250,500,650,700]
dict1={}
for index,elem in enumerate(l1):
    dict1[index]=elem
    
print(dict1)


##given a list of strings
##["abc"  , "hello","friday" ,"name"]
##make a dictionary with keys as elements of list
##and values are their lengths.
##output: {"abc":3 , "hello":5 ,"friday":6 ,"name":4 }

'''
Given a list of numbers [5, 12, 8, 3],
create a new list where each number is multiplied by 2.
Output: [10, 24, 16, 6]

Q1
Given a list of numbers [2, 4, 6, 8, 10],
create a dictionary where the keys are the numbers
and the values are their squares.
Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

Q2
Given a list of names ["Smith", "Kane", "Joe", "Khan"],
create a list of the first letters of each name.
Output: ['S', 'K', 'J', 'K']

Q3
Given a dictionary
{"apple": 3, "banana": 2, "cherry": 5},
create a new dictionary with the keys and values swapped.
Output: {3: "apple", 2: "banana", 5: "cherry"}

Q4
Question: Given a dictionary {"a": 1, "b": 2, "c": 3},
print the sum of all the values.
Output: 6


Q5
You have a list ["apple", "banana", "cherry", "date"].
WAP to print the index and element for
every element where the index is even.


Q6
Given two lists: ["name", "age", "city"] and ["Sam", 25, "Delhi"]
make a dictionary where keys are the elements of
first list and values are elements of second list.
Output:{"name":"Sam" , "age":12 ,"city":"Delhi"}


Q7
WAP to reverse order of digits of a number.
(without converting into a string)
'''




