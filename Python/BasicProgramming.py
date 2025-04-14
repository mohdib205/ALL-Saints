##print("Hello World")  #My program




#comments

#Python interpretor  ignores comments during execution
##Comments make code more readable
#Single line comments are Identified by '#' symbol

#Multi line comments
'''
This is example of
multi line
comments
'''

#indentation
#escape characters
'''
Escape characters allow insertion of
special characters in strings
\n, \t, \', \\
'''
# \n newline character

##print("Hello\nWorld")
   
### \t tab
##print("Hello\tWorld")

##print("Hello\"World")

##print("Hello\\nWorld")





#raw string
##Raw strings treat backslashes as literal characters
##print(r'C:\Users\dell\Documents\\New folder')


#WAP to print    " 'He"l\"'lo

##print('" \'He"l\\"\'lo')
##print("\" 'He\"l\\\"'lo")







##end
##The 'end' parameter specifies
##what to print at the end of the statement
print("Hello" , end=" " )
print("World")

print("print1" , end=" Print1 has executed " )
print("print2")



#Variables
'''
Variables are like containers that stores data
Variable in programming is  a reserved memory
location that is used to store data.
'''

##Variable names in Python have certain rules
##and conventions:
##    
##Must start with a letter or underscore (eg,
##name, _count)

##Can contain letters, digits, and underscores
##after the first character (eg, age,
##totalAmount)

## Python is case-sensitive, so 'name' and
##'Name' are different


## Reserved keywords like 'if', 'for', 'def' cannot
##be used as variable names

a1=1
b="Thursday"
abc=23
A=2
NaMe="Ibrahim"
my_name="ibrahim"
_age=7
print(a1)
print(_age)
print(my_name)
print(abc)

'''

Dynamic Typing in Python

Python is a dynamically-typed language:
we do not need to define  datatype when
we are declaring variables.
The data type is assigned based on the value
at runtime

'''
