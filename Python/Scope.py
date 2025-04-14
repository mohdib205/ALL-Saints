#Write a lambda function that returns the maximum
####of three numbers
##x=lambda a,b,c:a if a>b and a>c else (b if b>c else c)
##print(x(9,7,30))

##Use a lambda function to check if a string starts
##with the letter 'A'.
##x=lambda a:a.startswith('A')
##print(x("Noor"))
##print(x("Ajam"))
##
##Q.3 Create a lambda function that checks if a number
##is divisible by 5.
##x=lambda a: "devisible by 5" if a%5==0 else "Not divisible by 5"
##print(x(10))
##
##Write a lambda function to check if a string starts
##with a given character.
##x=lambda a,b:a[0]==b
##print(x("Noor",'A'))

##Given a list of words, use lambda and filter() to keep only those
##words that have an odd length.

##x=["Noor","Apple","Sibgat","Sam"]
##y=filter(lambda a:len(a)%2!=0,x)
##print(list(y))
## Use map to convert a list of strings ['1', '2', '3']
## to a list of integers.
##x=['1','2','3']
##y=map(lambda a:int(a),x)
##print(list(y))
##Given a list of words, use map to convert
##each word to uppercase.
##x=["noor","shahid","sam","shad"]
##y=list(map(lambda a:a.upper(),x))
##print(y)

##Q.3 Use map to calculate the length of each word
##in the list ['apple', 'banana', 'cherry']
##Q.4 Write a map function to add 10 to each element of the
##list [5, 10, 15, 20].

##Q.5 Given a list of dictionaries representing people,
##use map() to extract the names of all people.

##people=[{"name":"Noor","age":20},{"name":"Ibrahim","age":20}]
##x=list(map(lambda a:a['name'],people))
##print(x)
##Q.6 Given a list of integers, use map() and a lambda function
##to compute the following expression for each element:
##       result= (x**2+2*x+1)/x+1
##       wherex is each element of the list

##x=[2,3,4,5]
##y=list(map(lambda a:(a**2+2*a+1)/(a+1),x))
##print(y)
##Q.1 Use filter to extract even numbers
##from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
##x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##y=filter(lambda a:a if a%2==0 else None,x)
##print(list(y))

##Use filter to find all the strings in a
##list ['hello', 'world', '', 'Python', '', 'Lambda']
##that are non-empty.

##x= ['hello', 'world', '', 'Python', '', 'Lambda']
##y=filter(lambda a:len(a)>0,x)
##print(list(y))

##Write a filter function to find names starting with the letter 'J' from the list
##['Jack', 'John', 'Alice', 'Jake'].

##x=['Jack', 'John', 'Alice', 'Jake']
##y=filter(lambda a:a[0]=='J',x)
##print(list(y))

##Use filter to find palindrome strings from a
##list ['level', 'world', 'radar', 'python'].
##x=['level', 'world', 'radar', 'python']
##y=filter(lambda a:a==a[::-1],x)
##print(list(y))

##Write a program using filter() to filter prime
##numbers from a list of numbers.
##def prime(a):
##    for i in range(2,a):
##        if a%i==0:
##            break
##    else:
##        return True
##x=[1,2,3,4,5,6,7,8,9]
##y=filter(prime,x)
##print(list(y))
##Given a list of dictionaries representing people, use filter() to find people who are over the age of 25 and live in "New York."
##people = [
##    {"name": "Alice", "age": 28, "city": "New York"},
##    {"name": "Bob", "age": 22, "city": "San Francisco"},
##    {"name": "Charlie", "age": 30, "city": "New York"}
##]
##x=filter(lambda a:a if a['age']>25 and a['city']=='New York' else None,people)
##Use reduce to find the sum of all elements
##in the list [1, 2, 3, 4, 5].
##Write a reduce function to find the largest number
##in the list [10, 45, 23, 76, 34].

##Write a reduce() operation that multiplies all
##the even numbers in a list and returns the product.
##If there are no even numbers, return None.
##from functools import reduce
##x=[1,2,3,4,5,6,7,8,9]
##y=list(filter(lambda a:a%2==0,x))
##z=reduce(lambda a,b:a*b,y)
##print(z)
##Write a program that uses filter() to remove
##duplicate elements from a list and reduce() to find
##the sum of the remaining elements.
from functools import reduce
##x = [1, 2, 3, 2, 4, 5, 6, 4, 5]
##y = []
##
##z=list(filter (lambda a:y.append(a) if a not in y else None,x))
##a=reduce(lambda b,c:b+c,y)
##print(a)

##Q.6 Use reduce() to find the longest string in a
##list of strings.words = ["cat", "dog", "elephant", "banana"]
##words = ["cat", "dog", "elephant", "banana"]
##x=reduce(lambda a,b:a if len(a)>len(b) else b,words)
##print(x)

##Q.1 Use filter() to get the odd numbers from a
##list, then use map() to square
##them, and finally use reduce() to sum the squares.

############---------------XXXXXXXXXXXX-----------###############

#######----------join Method------------#####

##The join() method in Python is a string method used
##to concatenate the elements of an iterable
##(e.g., a list or tuple) into a single string, with
##each element separated by the specified delimiter.

#syntax
##separator.join(iterable)
##
##1.separator: A string that will be inserted between each element of the iterable.
##
##2.iterable: An iterable (like a list, tuple, or set) containing strings.
##
##Note:The join method works only on iterables containing strings. If any
##element is not a string, it will raise a TypeError.

##words=['1','2','3','45']
##x=''.join(words)
##print(type(x))

##list1=["Noor","Alam"]
##x=' '.join(list1)
##print(x)

##############------Scope---------################
##Scope=> Scope refers to the area in a program where a variable can be accessed
##or used.It defines where a variable is visible and where it is not.
##1.local Scope
##2.Global Scope
##3.Global Keyword
##########--------Local Scope-------########
##Variables declared inside a function or block.Accessible only within that
##function or block.

##def funct():
##    x=20
##    print(x)
##funct()
##print(x)

########---------Global Scope----------############
##Variables declared outside of all functions or blocks.Accessible throughout
##the entire program.

x="Ibrahim"
def funct():
    print(x)
    z="Rahim"
funct()
print(z)

name="Noor"
##def details():
##    global name
##    name="Yusuf"
##    
##details()
##print(name)






