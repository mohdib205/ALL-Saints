a="The concept of fitness encompasses both physical and mental health. Achieving fitness is essential for leading a fulfilling life. Key principles of maintaining fitness include regular exercise a balanced diet proper hydration and sufficient sleep."

##while True:
##    num1=int(input("enter a number1 "))
##    num2=int(input("enter a number2 "))
##    operator= input(" enter +,-,* or // ")
##
##    if operator=="+":
##        print(num1+num2)
##    elif operator=="-":
##        print(num1-num2)
##    elif operator=="*":
##        print(num1*num2)
##    elif operator=="//":
##        if num2==0:
##            print("can't divide by zero")
##        else:
##            print(num1//num2)
##    else:
##        print("enter valid operator")


'''
Create a list of 50 random numbers between
1 and 200. Ask a user to input any number
and store it. then print a list of
all those numbers from random list that are
divisible by a user inputted number.

WAP to print the index of even numbers in
new list from list1.[11 , 12 ,88 , 77 , 6 ,9]

Given  dict {"num1":12 , "num2":22 , "num3":454}
find the key whole value is largest.


'''
   
'''
Create a list of 50 random numbers between
1 and 200. Ask a user to input any number
and store it. then print a list of
all those numbers from random list that are
divisible by a user inputted number.
'''
##import random
##random_list=[]
##user= int(input("enter a num " ))
##
##for i in range(50): 
##    random_list.append(random.randrange(1, 200))
##print(random_list)
##
##new_list=[]
##for num in random_list:
##    if num%user==0:
##        new_list.append(num)
##print(new_list)

    










'''
list1=[11 , 12 ,88 , 77 , 6 ,9]
list2=[]
for i,e in enumerate(list1):
    if e %2 ==0:
        list2.append(i)
print(list2)


##
##list1.index(88)
list2=[]

for i in list1:
    if i%2==0:
        list2.append(list1.index(i))

print(list2)
'''






        


        

##d={"num1":12 , "num2":22 , "num3":454 ,"num4":4}
##max_value=0
##max_key=''
##
##for k,v in d.items():
##    if v>max_value:
##        max_value=v
##        max_key=k  
##print(max_key)
'''
* * * * *             (* )*5
 * * * *       " "*1+ (* )*4         
  * * *        " "*2+ (* )*3
   * *         " "*3+ (* )*2
    *          " "*4+ (* )*1
'''
##i=5 j=1
##[(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]
##for i,j in zip(range(7,0,-1) , range(1,8)):
##    print("* "*i, end="\n"+" "*j)








num=458
'''
##num%10 = 8
##num // 10 = 45
##
##num%10 = 5
##num // 10 = 4
##
##num%10 = 4
##num // 10 = 0
'''

##8
##8+5 = 13
##8+5+4=17
num=458
s=num
Sum=0
for i in range(len(str(num))):
    rem=num%10
    Sum+=rem
    num= num//10   
print(Sum)
print(num ,s)

l1=[13,45,66,654,141, 7878]
n=[]
for i in l1:
    rev=0
    ...
    if i==rev:
        n.append(i)
n1=121
rev=121

if n1==rev:
    print("it is palindrom")

    
    


##3. Write a function that takes two integers
##as parameters and returns the count of prime
##numbers between them.  
##    For example,
##    let's say the function name is
##    count_primes, then count_primes(10, 30)
##    should return the count of
##    all prime numbers between 10 and 30.

'''
'''

def count_primes(x,y):mnn
    count=0
    for i in range(x,y):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1
    return count
print(count_primes(20,100))


        
    
    




    

    


