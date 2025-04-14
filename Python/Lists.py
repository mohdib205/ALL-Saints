###list is a collection of items

l1=["Python" , 12, 100 , 3, True , 3.6 ]

print(len(l1))
l2= list((1,2,3,4,5))
print(l1)
print(l2)
#length (to get length of list)
l1=["Python" , 12, 100 , 3, True , 3.6 ]
print(len(l1))

#indexing
print(l1[-1])
print(l1[4])
#####slicing
print(l1[0:3])
print(l1[2:])
print(l1[:4])

print(-1::-1])



#index
'''index method is used to
find the index of any item'''
list1=["Python" , 12,13,False , 12]
print(list1)

list1[2]="Hello"
print(list1)

##append
'''append method (to add an element in a list)
append add element at the last index of list'''
list1.append(100)
print(list1)

###insert
'''insert is also used to add element but in this
we can specify at which index element would be added'''
list1.insert(1, 5.8)
list1.insert(3 , "New element")
print(list1)


#####changing item value
list1[2]="a" #it will change element of 2nd index
print(list1)

##remove
#remove method removes given elememt from list
#syntax: remove(element)
##
list2=["a" , "b" , "c" , 1,2 , "b"]
print(list2)
list2.remove("b")
print(list2)


####pop
'''
pop deletes element according to the given index
Syntax: pop(index)
 pop also return the deleted element
if no index is given then
it would delete last element of list

'''
list3=["a","b","P", 600,700]
print(list3)
print(list3.pop(2)) #it will return the deleted element
print(list3.pop())   ###it would delete last element of list
print(list3)




####clear
'''it removes all the elements from a list
clear makes the list empty but
didnot delete the list'''

list3=["a","b","P", 600,700]
list3.clear()
print(list3)


#del deletes the variables  from the memory
del list3[1] #it will delete the element of 3ed index
print(list3)
del list3   #it will delete the list
# print(list3)    #it would raise error as list2 has deleted



####adding two lists
l1=["a" , "b" , "c"]
l2=[1,2,3,4]
print(l1 + l2)


list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list1+list2)

###extend (to add multiple elements in a list)
'''
The extend method adds the specified list elements
(or tuple)to the end of the current list.
'''

list1=[1,2,3,4,5]
print(list1)
list1.extend((10,20,"a"))
print(list1)

print(list2)
list2.extend(["a","b","c"])
print(list2)
list1.extend(list2)
print(list1)

#sort
##The sort() method used to sort the list
list1=["v" , "y" , "z","abc" , "abd"]
print("before sorting" , list1)
list1.sort()
print("after sorting" , list1)

list1=[23,21,4,54,100,45,3]
print(list1)
list1.sort()
print("sorted list" , list1)
list1.sort(reverse=True)
print(list1)


###reverse  #it is used to reverse order of elements
list1=[23,21,4,54,100,45,3]
##print(list1,list1[-1::-1])

list1.reverse()
print(list1)


list1=[23,5,78,98,100,3]
list1.sort() #it sorts in ascending order by default
print(list1)

list1.sort(reverse=True) #to sort in descending order 
print(list1)


#sorted is also used to sort the items

my_list=[23,44,5,3,22,78,0,1]
sorted_list=sorted(my_list)

print("original list" , my_list)
print("sorted_list asc" ,sorted_list)
print("sorted_list desc" ,sorted(my_list , reverse=True))


#difference between sort and sorted
'''
sort is a list method it only works
on lists while sorted 
sorted() method can sorts list ,
tuples , sets , dictionary

sort method sorts the original list while sorted()
does not change  the original list but
creates a new sorted list.
'''

#reversed #it reversed the order of items in a list

my_list=[23,44,5,3,22,78,0,1]
#reversed
rev_list=reversed(my_list)
print(list(rev_list))

rev_list=list(reversed(my_list))
print("original" , my_list)
print("rev", rev_list)


#Difference between reverse and reversed is
##same as between sort and sorted
'''
reverse is a list method it only works
on lists while   reversed() method can reverses list ,
tuples , sets , dictionary

reverse method reverses the original list while reversed()
does not change  the original list but
creates a new reversed list.
'''






















