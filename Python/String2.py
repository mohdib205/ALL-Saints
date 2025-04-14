#replace() this method is used to replace characters from a string
#replace(currentCharacters, newCharacters)

str1="Cat"

str2=str1.replace("C","B")
print(str1.replace("C","B"))

print(str1) #replace does not change the original variable
print(str2)
##
str1="PythonProgramming"
str2=str1.replace("Python", "Javascript")
print(str2)
str2=str1.replace("P", "K") #it will replace all occurances of "P"
print(str2)
####split
####split() method splits a string into a list.
####split(seperator)

str1="Hello World Good Afternoon"
print(str1)
sep1=str1.split(" ")
print(sep1)
sep2=str1.split("o")
print(sep2)

sep3=str1.split() #by default seperator is space(" ")
print(sep3)

####maxsplit
####to limit the number of splits that
####can be performed on a string ,
####maxsplit parameter is used


str1="Hello World Good Afternoon Everyone"
sep4=str1.split( maxsplit=2)#this will split only 2 times

print(sep4)

####casting
####Changing datatypes of variables
####int , float , str 
f1=3.5
int1= int(f1) #convertig float into integer
print(int1 , type(int1))

int2=50
f2= float(int2) #convertig integer into float
print(f2, type(f2))

str1="12"
int3=int(str1) #converting string into integer (only if string contains integers)
print(int3, type(int3))

int4=1234
str2= str(int4) #integer into string
print(str2, type(str2))





#input()
## it is used to take input from user
##by default input function
##stores values in  str datatype

name=input("Enter your name ")
print(name)
print(type(name))

num1= int(input("enter a number ")) #we have to convert it into integer
print(num1 , type(num1))


'''
#String Format
##The format() method formats
the specified value(s) and
insert them inside the string's placeholder.

# The format() method returns
the formatted string.


#we can also use f string for formatted strings
'''

##a=10
##print("value of a is {}".format(a))
##b=4
##c=3
##print("a is {},b is {},c is {}".format(a,b,c))
num1=15

print(f"num1 is {num1}")
num1 =10
num2=8

print("sum of {} and {} is {}".format(num1,num2,num1+num2))

print(f"sum of {num1} and {num2} is {num1+num2}")




