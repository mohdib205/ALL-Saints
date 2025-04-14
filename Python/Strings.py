

#Strings
a="Friday"
b="123"

#length
##The len() function returns the number of elements
##in the String (or list,  tuple etc)

##print(len(a))

'''
Indexing
Indexing refers to accessing
individual elements in a sequence(str , list , tuple)

Indexing starts from 0
'''

##print("0th index " ,a[0])
##print("1st index " , a[1])
##print("2nd index " , a[2])
str1="Tuesday"

#negative indexing :  it starts from -1

print(str1[-1]) #-1 denoted last index
print(str1[-2])
print(str1[-3])


##'''
###Slicing
##Slicing is used to obtain a portion of a sequence
## Syntax: [start_index:end_index]
## end_index is excluded
##'''
##str1="Hello"
##
##
print(str1[:5]) #0 , 1 ,2 ,3,4
print(str1[2:])
##
####[startIndex:endIndex: step_size]
print(str1[0:len(str1):2])

# we can return a range of characters by using the slice syntax
print(str1[0:3]) #we give range in sq. brackets
##      [start index:end index]  #end index is excluded
    
print(str1[:4]) #if start index is not given it will start from 0th index
print(str1[2:]) #if last index is not given it will go upto last character of string

print(str1[0:5:2]) #here third number is step size in range




print(str1[-4:-2]) #print characters from -4 to -1 (i,e from 3 to 5)

# to slice strings in reverse order we give -1 as stepsize

print(str1[-1:-4:-1]) #start from -1 , end index is -4)
print(str1[5:1:-1])   #start from 5 , print in reverse order upto 1st index

##"Tuesday" #yadseuT
print(str1[-1:-8:-1])
print(str1[7::-1])
##print(str1[4:])
##print(str1[-3:])


##print(str1[0:3])
##print(str1[1:4])
##          
#### Common string methods:
#### upper(): Converts string to uppercase
##str1="Hello World"
##print(str1.upper())
##
#### lower(): Converts string to lowercase
##str2="HELLO WorlD"
##print(str2.lower())




