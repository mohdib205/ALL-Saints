##Python Operators
####Operators are used to perform operations on variables and values.
##
####Python Arithmetic Operators
####Arithmetic operators are used with numeric values
####to perform common mathematical operations
##
###addition
####+
##print(12+4)
##print("Today is " + "Tuesday")
##num1=23
##num2=7
##total_num= num1+ num2
##print(total_num)
##
###Subtraction
####-
####print(num1-num2)
##
###Multiplication
##print(20*5)
##print("Good Afternoon "*10)
##
#### / (Division): Returns the exact quotient
####(eg, 5 / 2 = 2.5)
##num_1=10
##print(num_1 / 4)
##
####
###### % (Modulus): Returns the remainder
####(eg, 5 % 2 = 1)
##print(num_1 % 4)
##print(num_1 % 2)
####
######// (Floor Division): Returns the quotient
######rounded down (eg, 5 // 2 = 2)
####
##print(10//3)
##print(10/3)
##print(10 % 3)
##
###**
##print(2**2  , 2**3)
##print(5**5)
##
##

'''
Comparison Operators

Used to compare values:
 > Greater than
 < Less than
 == Equal to
 >= Greater than or equal to
 <= Less than or equal to
 != Not equal to
'''
num1=12
##print(num1 >10)
##print(num1 < 5)
##print(num1==12)
##num2=10
##result=  num2!=num1
##print(result)
##print(num1>=12)
##print(num2<=8)

'''
#ASSIGNMENT OPERATORS : Used to assign values to variables:
 =  `   Assigns the value
 +=     x += 3 (Equivalent to x = x + 3)
 -=     x -= 3 (Equivalent to x = x - 3)
 *=     x *= 3 (Equivalent to x = x * 3)
 /=     x /= 3 (Equivalent to x = x / 3)
'''

##+=
num1=5
num1= num1 + 2
print(num1)

num1+=2
print(num1)

##-=
num1-=5
print(num1)

#*=
num=2
num*=10
print(num)

num%=6  #num= num%6
print(num)
'''
#logical operators
Logical operators are used to combine conditional statements:
and: Returns True if both statements are true

or: Returns True if at least one statement is true

not: Reverses the result
     (True becomes False, and vice versa)
'''
num=4
#divisible by 2
div_by2=  num%2 == 0 # it will store True or False
print(div_by2)

div_by3 = num%3 == 0
print(div_by3)

print("and " ,  div_by2 and div_by3) 
print( "or " , div_by2 or div_by3)
print("not" ,  not(div_by2))































