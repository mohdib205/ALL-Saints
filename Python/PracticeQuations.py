
num=35

for i in range(2,num):
    if num%i==0:
        print("it is not a prime number")
        break
else:
    print("it is a prime number")
    






##given a list of strings
##["abc"  , "hello","friday" ,"name"]
##make a dictionary with keys as elements of list
##and values are their lengths.
##output: {"abc":3 , "hello":5 ,"friday":6 ,"name":4 }

'''
Given a list of numbers [5, 12, 8, 3],
create a new list where each number is multiplied by 2.
Output: [10, 24, 16, 6]
'''
list1=[5, 12, 8, 3]
list2=[]
for i in list1:
    list2.append(i*2)
print(list2)

'''
Q1
Given a list of numbers [2, 4, 6, 8, 10],
create a dictionary where the keys are the numbers
and the values are their squares.
Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

'''
list1=[2, 4, 6, 8, 10]
dict1={}

for e in list1:
    dict1[e]=e**2
print(dict1)
    
    




'''
Q2
Given a list of names ["Smith", "Kane", "Joe", "Khan"],
create a list of the first letters of each name.
Output: ['S', 'K', 'J', 'K']
'''
list1=["Smith", "Kane", "Joe", "Khan"]
l2=[]
for s in list1:
    l2.append(s[0])

'''
Q3
Given a dictionary
{"apple": 3, "banana": 2, "cherry": 5},
create a new dictionary with the keys and values
swapped.
Output: {3: "apple", 2: "banana", 5: "cherry"}
'''
d1={"apple": 3, "banana": 2, "cherry": 5}
d2={}
##print(d1.items())

for a,b in d1.items():
    d2[b]=a
print(d1)
print(d2)








'''
Q4
Question: Given a dictionary {"a": 1, "b": 2, "c": 3},
print the sum of all the values.
Output: 6
'''
s=0
d1={"a": 1, "b": 2, "c": 3}
##print(d1.values())
for i in d1.values():
    s+=i
print(s)  



'''
Q5
You have a list ["apple", "banana", "cherry", "date"].
WAP to print the index and element for
every element where the index is even.
'''
l1=["apple", "banana", "cherry", "date"]
for i,e in enumerate(l1):
    if i%2==0:
        print(f"index is  {i} and element is {e}")
'''
Q6
Given two lists: ["name", "age", "city"] and
["Sam", 25, "Delhi"]
make a dictionary where keys are the elements of
first list and values are elements of second list.
Output:{"name":"Sam" , "age":25 ,"city":"Delhi"}
'''


'''
Q7
WAP to reverse order of digits of a number.
(without converting into a string)
'''

num=143
rev_num=0
for i in range(len(str(num))):
    mod=num%10
    rev_num= rev_num*10 + mod #rev_num=34
    num=num//10
print(rev_num)




##Today's Questions

#WAP to print the prime numbers from the given list
list1=[12,34,5,91,7,80,49]

'''
Q1
#WAP to print the prime numbers from the given list
list1=[12,34,5,91,7,80,49]

Q2
WAP to create a new list of even numbers from
a given list using for loop. 

Q3
WAP to print a dictionary to filter out all key-value 4
pairs of any given dict  
where the value is less than 10 
for eg:
input : {"a":123,"b":7 ,"c":25 ,"d":5 ,"e":44}
output:  {"a":123, "c":25 ,"e":44}

Q4
Given two lists: ["name", "age", "city"] and
["Sam", 25, "Delhi"]
make a dictionary where keys are the elements of
first list and values are elements of second list.
Output:{"name":"Sam" , "age":25 ,"city":"Delhi"}

Q5 Given a dictionary {"apple": 10, "banana": 15, "kiwi": 5, "cherry": 20}.
Write a Python program to print only the key-value pairs
where the value is greater than 10.

Q6
Given a list ["cat", "dog", "fish", "bird"],
WAP to print the index and element for every element
where the element length is greater than 3.

Q7
WAP to check whether a number is prime or not using
while loop
'''










