####Write a program that takes a string and returns a new
####string with the vowels removed
##str1="Abcdefijklmnopqrstuvwxyz"
##new_s=""
####s=="a" or s=="e" or s=="i" or s=="A" or s=="E"
##for s in str1:
##    if s not in ["a","e","i" ,"o" , "u" , "A" , "E" , "I" , "O" ,"U"]: 
##        new_s+=s
##print(new_s) 
##        
##
##
####Write a Python program to find the most frequent
####word in a string.
##st1="aaabbggttiiaadeeddggff"
##d1={}
##
##for s in st1:
##    if s not in d1:
##        d1[s]=1
##    else:
##        d1[s]+=1
##print(d1)
##m=0
##max_key=""
##for i in d1:
##    if d1[i]>m:
##        m=d1[i]
##        max_key=i
##        
##print(max_key)
##
##
##
####Write a program  to remove duplicates from a list.
##l1=[1,2,3,4,1,5,6,2,3,2,4,3,2,4,5,9,10,11]
##l2=[]
##for i in l1:
##    if i not in l2:
##        l2.append(i)
##print(l2)       
##    
##
##          
##            
##            
##
####WAP to check if two sets have any elements in common
##s1={1,2,3,4,5}
##s2={3,5,7,8,9}
##s3=set()
##for num1 in s1:
##    for num2 in s2:
##        if num1==num2:
##            s3.add(num1)
##print(s3)  
####How do you access a value associated with a specific key
####in a dictionary?
##
##d1={"A":1 , "B":2}
##      
##print(d1["B"])
##d1["B"]=7
##
####Write a program to check if a key exists in a dictionary.
##print("A" in d1)
##
##
####How would you remove a key-value pair from a dictionary?
##
##d1.pop("A")
##
##
####WAP to print the factorial of a number using a while loop
##
##
##
####WAP to generate a multiplication table using a while loop
##a=5
##i=1
##while i<11:
##    print(a*i)
##    i+=1
##
##
####WAP to  find the  key that has the maximum value in a dictionary
##d={'a': 5, 'b': 2, 'g': 4, 't': 2, 'i': 8, 'd': 3, 'e': 2, 'f': 2}
##
##m=0
##max_key=""
##for i in d:
##    if d[i]>m:
##        m=d[i]
##        max_key=i
##      
##print(max_key)
##
##        
####functions (positional argumnets , keyword arguments
####default argument, args, kwargs)
####lambda map filter reduce
####list comprehension , dictionary comprehension
####key sorting
##
####
##
##
import random as rn

randomList=[]
score=0
correct={}
incorrect={}
for num in range(50):
    randomList.append(rn.randrange(1,50))


##for i in range(1,11):
##    num=int(input("Guess a number "))
##    if num in randomList:
##        score+=2
##        correct[f"Guess{i}"]= num
##
##    else:
##        score-=1
##        incorrect[f"Guess{i}"]= num
##        
##print(score)
##print(randomList)
##print(correct)
##print(incorrect)





list1=[1,2,3,4,5,6,7,8 , 9]
list2=["Gyan" , "Saklen" , "Shahbaz" , "Shaik" , "Vivek" ,"Shahid" , "Afreen" , "Faiz" , "Shadman"]

##Extract names from list2 that start with the letter 'S'

print(list(filter(lambda x:x[0]=="S" , list2)))
print([ i for i in list2 if i[0]=="S"])

print([round(i**(1/2) , 2) for i in list1])
       
    
##Create a dictionary with name as key and index of name as value from list2

print({x:len(y) for x,y in enumerate(list2)  if y[0]=="S"  })


##create a dictionary where values are first
##CHaracvter of each element of list2 and
##keys are squares of each element of list1
##output ={1:"G",4:"S" , 9:"S" ,16:"S" …...}


##print({a**2:b[0] for a,b  in zip(list1,list2)})

d1={1: 6, 2: 7, 3: 5, 5: 6, 8: 7}

print({v:k for  k,v  in d1.items()})

## regex , file handling , os module , recursion ,
## OOP , exception handling
