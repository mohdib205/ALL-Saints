##for s in "Hello World":
    print(s)

##WAP to take input from user and
#print only the vowels from it

str1=input("Enter any word " )
for char in str1: #a,e ,i,o ,u A I O
    if char in ["a","i","e","o","u" ,"A","I","O","E","U"]:
        print(char)

#WAP to print sum of first 10 natural numbers
##print(1+2+3+4+5+6+7+8+9+10)

Sum=0
for num in range(1,11):
    Sum+=num

print(Sum)
    
#WAP to print factorial of 5
##1*2*3*4*5
fac=1
num=5
for num in range(1,num+1):
    fac*=num

print(fac)
#WAP to print sum of all elements of list
##  [100,300,650,67,34] #don't use sum function

#For else
##The else block in a for loop is executed only
##when the loop finishes all iterations.

for i in range(1,5):
    print(i)
else:
    print("For loop terminated")


##Break terminates the loop when a condition is met.
### break statement is used to terminate  loop
### when some external condition is triggered.

for n in range(50):
    print(n)
    if n==20:
        break
else:
    print("Loop terminated")

##If  break is used to terminate the loop early,
##the else block is skipped.



##Continue skips to the next iteration when a condition
##is met.
    
for i in range(20):
    if i%2==0:
        continue
    print(i)
else:
    print("For else block")


#prime numbers


#WAP to check whether a number is prime or not. 


##WAP to print the multiplication table of a number
##provided by the user.

##WAP that counts how many vowels (a, e, i, o, u)
##are in a given string.

#WAP to find the sum of digits of a given number




