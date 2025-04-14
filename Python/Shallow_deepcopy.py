'''Shallow Copy makes copies of the nested
objects' reference and doesn't
create a copy of the nested objects.
A deep copy is a process where we create a
new object and add copy elements recursively.
The independent copy is created of original
object and its entire object.
'''

import copy
list1=[1,2,3,[4,5]]
copy_l1= copy.copy(list1)

copy_l1[3][0]=10

print(list1)

deep_l1= copy.deepcopy(list1)
deep_l1[3][1]=100
print("original" , list1)
##print("deep copy " , deep_l1)

dict1={"a":1 , "b":2 ,"c":{"d":3, "e":4}}

shallow= copy.copy(dict1)
deep= copy.deepcopy(dict1)

dict1["c"]["d"]=5
dict1["a"]=10

print("original", dict1)
print("shallow" , shallow)
print("deep" , deep)
