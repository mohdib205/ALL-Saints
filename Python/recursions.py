##RECURSION

##5!= 5 * 4* 3* 2*1
##  = 5* 4!
##
##4!= 4* 3! = 4*3*2!
##
##n!= n* (n-1)!



    
'''
Any function that calls itself in its body
repeatedly until a particular condition
becomes false and the target task is done is
called a "Recursive function" and
this procedure is called "Recursion"
'''

def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)

##fact(5)= 5 * fact(4)
def Sum(x):
    if x==0:
        return 0
    else:
        return x+ Sum(x-1)


    

##print(Sum(20))
##
####5*4*3*2*1=120
##print(fact(5))

##5* fact(4)
##
##4* fact(3)
##.... 2* fact(1)

##10th= 9th+ 8th
##1st =1
##0th=0
##
##0 1 1 2 3 5 8 13 21 34  
##0=0
##1=1
##2=
##f(n) = f(n-1) + f(n-2)

def febo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return febo(n-1) +febo(n-2)

##print(febo(15))

user= int(input("enter a number: "))
for i in range(1, user+1):
    print(febo(i) , end=' ')
    



        
    
    












'1 1 2 3 5 8 13 21 34 ...'

##sum(n-1) + sum(n-2)

##def febo(n):
##    if n==1:
##        return 0
##    elif n==2:
##        return 1
##    return febo(n-1) + febo(n-2)
##
####print(febo(10))
##a=10
##for i in range(1,a+1):
##    print(febo(i))









