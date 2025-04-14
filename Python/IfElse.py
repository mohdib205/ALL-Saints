'''
The if statement checks a condition.
If the condition is True,
the code block under it will execute.
'''
a=4
if a==4:
    print(" we are in if block")
##There  should be the  indentation(4 spaces or a tab)
##to define blocks of code.

##All lines of code under if, elif, or else should be indented to indicatethey belong to that block.


    
'''   
The elif  statement allows
us to check multiple conditions.

If the first if condition is False,
then the elif condition will be checked.

we can have multiple elif statements.
'''

if True: #it will run 
    print("if")
elif False:
    print("elif block")

    
if False:  
    print("if")
elif True:  #it will run 
    print("elif block")
   
print("out of conditions")
'''
The code inside an else block will run
if the condition in the corresponding
if or elif statements are False.
'''
if False:  
    print("if block")
elif False:  
    print("elif block")
else:           #it will run 
    print("else block")

#Q1
#WAP to check whether user is eligible to vote or not
 
age= int(input("Enter your age "))
if age<0:
    print("Invalid age")
elif age>18:
    print("eligible to vote")
else:
    print("not eligible")

#Q2
#WAP to print whether a number is
##divisible by 2 or divisible by 3 or divisible by both

num1=int(input(("Enter a number ")))
        
if num1%2==0 and num1%3==0:
    print("divisible by both")
elif num1%3==0:
    print("divisible by 3")
elif num1%2==0:
    print("divisible by 2")
else:
    print("not divisible by 2 or 3")
    
#Q3
##WAP to print "Positive", "Negative", or "Zero" based on a number's value.

#Q4  
##WAP to  print which among the any three given numbers (num1, num2, num3) is the greatest.

#Q5
##WAP to determine if a triangle is equilateral, isosceles, or scalene based on its side lengths.
'''
Scalene Triangle: All three sides are of different lengths.
Isosceles Triangle: Any of Two sides are equal length, and the third side is different.
Equilateral Triangle: All three sides are of equal length. 
'''


    

