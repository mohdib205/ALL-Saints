#NESTED LIST

##A nested list  is simply a list that
##contains other lists as its elements.
##It’s like having a list inside another list.


list1=[[1,2,3] , [4,5,[10,16]] , [7,8,9]]

print(list1[0][0])
print(list1[1][2][0])


##A nested dictionary  is a dictionary that
##contains other dictionaries as values


dict1={"product1":{"name":"abc","price":100 ,
                   "colors":["red","blue"]} ,
 "product2":{"name":"xyz","price":300} }

print(dict1["product1"]["colors"][0])

'''
 
#Given a dict
fruits = {
    "Apple": {"quantity": 20, "price": 2},
    "Banana": {"quantity": 50, "price": 1}
}
WAP to print price of Apple.
WAP to print quantity of Banana
WAP to change the price of Banana to 100.

Add a new fruit 'Mango' with its quantity as 25
and price as 120.


Given a dict:
employees = {
    "Emp1": {"age": 30, "skills": ["Python", "C++"]},
    "Emp2": {"age": 25, "skills": ["JavaScript", "HTML"]}
}
WAP to Add a new skill "Java" to Emp1’s list of skills.

