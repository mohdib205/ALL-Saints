#Dictionary


name=["Apple" , "Banana" , "Mango"]
price=[100,40,80]
prd1={"name":"apple" , "price":100 , "stock":20,"name":"appl2"}

prd2={"name":"banana" , "price":40 , "stock":100}
prd3={"name":"mango" , "price":80 , "stock":50}

prd1["price"]


frt_index=name.index("Mango")
price[frt_index]



'''
Dictionaries are used to store data values in
key,value pairs.
A dictionary is a collection which is ordered,
changeable and do not allow duplicates.
'''
##student1={"name":"Ibrahim" , "semester":3}
##print(student1)
##student2={"name":"Saklen" , "semester":3}
##print(student2 , type(student2))


#to check if any key exists in dict

##print("Age"   in student1)
##
##print("semester" not in student1)


#changing the value of an existing key

##student3={"name":"Shahbaz" , "semester":2}
##
##print(student3["semester"])
##
##student3["semester"]=3
##print(student3)


#to add new key value pair in a dictionary

##student3["branch"]="CS"
##
##student3["College"]="ASCT"
##print(student3)


# remove the element with specified key

#pop
##col=student3.pop("College")
##print(col)
##print(student3)
##
##student1={"name":"Ibrahim" , "semester":3 , "branch":"CS"}
##name=student1.pop("name")
##print(name)
##print(student1)
##
##branch=student1.pop("branch")
##print(branch)
##print(student1)

##Get the list of keys


##student4={"name":"ibrahim" , "sem":3 , "branch":"CS"}
##print(student4.keys())
##
#### Get the list of values
##print(student4.values())



# items() returns a list of tuples where each tuple
# is a tuple of key-value pair

##dict1={"num1":12 , "str1":"Python","bool1":True ,"float1":4.7}
##
##print(dict1)
##
##a=list(dict1.items())
##print(a)
##print(a[0])
##
##
##
###enumerate function
'''
##The enumerate() function takes a
collection (e.g. list or tuple)
##and returns it as an enumerate object.
##we can convert this object into a list
of tuples where each   tuple
contains index and element of lists.
#(index, value)
'''
##list1=[100,200,300,400 , 500]
##print(list1)
##pairs=list(enumerate(list1))
##print(pairs)
##
##tuple1=("a" , "b" ,"c")
##pairs2=list(enumerate(tuple1))
##print(pairs2)



l1=[12,54,98,90 ,100 ,200]

l2=["Hello" , "Good" , "Bad" ,"python"]
l3=[True , False , True , False]
print("list1 " , l1)
print("list2 ", l2)
##print("list3 ", l3)
zip_list=dict(zip(l1,l2,l3))
print("after zip " , zip_list)




###zip method
'''
##The zip() function in Python combines
two or more collections
##(like lists, tuples, etc.) element-wise into pairs
##in the form of tuples.
##It returns a zip object, which contains tuples, where
##each tuple contains one element
from each of the iterables.
'''
