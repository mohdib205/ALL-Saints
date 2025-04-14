##1.Lambda 
##2.Map  
##3.Filter 
##4.Reduce


#Lambda

##lambda argument:Expresion if condtion else 

##x=lambda a,b:a+b
##print(x(1,2))

##even=lambda a:"Even"if a%2==0 else "odd"
##print(even(3))




##def check(a,b):
##    print(a+b)
##check(1,2)
##


#Map


##x=map(function,iterable)

    
##x=[1,2,3,4,5,6]
##y=map(lambda a:"Even" if a%2==0 else "odd",x)
##print(list(y))

##x=["noor","shahid","ragib"]
##y=map(lambda a:a.upper(),x)
##print(list(y))


##Use map to calculate the length of each word in the list ['apple', 'banana', 'cherry'].

##list1=['apple', 'banana', 'cherry']
##x=map(lambda a:len(a)>5,list1)
##print(list(x))
##
##
##x=[2,3,4,5]
##y=map(lambda a:a+10,x)
##
##print(sum(list(y)))

##list1=[{"name":"Noor","age":50},{"name":"ragib","age":22}]
##
##x=map(lambda a:a["name"],list1)
##print(list(x))


#Filter
##filter(fuction,iterable)
def even(a):
    if a%2==0:
        return True

##x=[1,2,3,4,5,6,7,8]
##y=filter(even,x)
##print(list(y))


##list1=["Apple","Ball","elephent"]
##x=filter(lambda a:len(a)%2==0,list1)
##print(list(x))


#Reduce
##reduce(fuction,iterable)


from functools import reduce
##
##x=[2,3,4,5,6]
##y=reduce(lambda a,b:a+b,x)
##print(y)

li=[23,56,21,12]
x=reduce(lambda a,b:max(a,b),li)
print(x)





