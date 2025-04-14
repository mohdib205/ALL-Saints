#Tuples 

'''

Tuples are used to store multiple items
in a single variable.
Tuple is one of 4 built-in data types in Python
used to store collections of data.
Lists are mutable but tuples are immutable
Tuple is ordered and unchangeable.

'''

##t1=(12,23,"hello" , True , "python", 23)
#index (to get index of any element)
print(t1.index(23))

print(t1[3])

#count method is used to count
##number of times given element is present in a list/tuple

print(t1.count(23))

#adding two tuples
tuple1=(23,32,"a", 100)
tuple1=(78,"Python",False, 50)

tuple3=tuple1+tuple2
print(tuple3)


##SETS
#sets is also used to multiple items in
##a single variable
#sets are unordered and unindexed
#sets are unchangable
#sets contains unique values

set1={12,56,88,90}
print(set1)
print(type(set1))

#set  constructor
set2= set((1,2,3,4.5))
print(set2)

#to add an element
set2.add(3)
print(set2)

set3={1,3,5,6,5,6,6,8}
print(set3)
 

#union
#union contains all elements of  all sets
set1={10,20,30,40,50}
set2={20,25,30,35,40,45}
print("set1", set1)
print("set2", set2)
union_set=set1.union(set2) #it have all elements of both sets
print("union" , union_set)
union_set=set1 | set2
print("union" , union_set)


#intersection
##intersection contains common elements of sets
intersection_set=set1.intersection(set2)
print("intersection" , intersection_set)
intersection_set=set1 & set2
print("intersection" , intersection_set)
