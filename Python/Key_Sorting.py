'''
Key sorting in Python refers to the process
of sorting elements in a collection based
on a specific value or attribute of each element,
rather than sorting based on the elements themselves.
This is done by providing a function to the
key argument in sorting functions like sorted()
or list.sort(), where the function returns
the value to be used as the basis for sorting.
'''

list1=[-1,-8,5,-2,3,0,-6,2]

print(list1)
list1.sort(key= lambda x:x**2)
print(list1)

list2=sorted(list1 , key=abs)
print(list2)


# -- DICTIONARY SORTING ----
dict1={"b":20,"a":5,"c":100,"d":8}

print(dict1)
sorted_dict=dict(sorted(dict1.items()))
print(sorted_dict)


#sorting on the basis of values of dictionarym
dict1={"b":20,"a":5,"c":100,"d":8}

print(dict1)
sorted_dict=dict(sorted(dict1.items() ,key=lambda x:x[1]))
print(sorted_dict)















