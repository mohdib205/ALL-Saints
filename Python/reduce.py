transactions = [
    {"type": "debit", "amount": 1200},
    {"type": "credit", "amount": 5600},
    {"type": "debit", "amount": 4000},
    {"type": "credit", "amount": 23006},

   ]

##WAP to convert amount of Transaction to Dollars

#/ 1 dollar=84 Rs
##1 Rs= 1/84 dollar 

##def dollar(a):
##    a["amount"]=a["amount"]/84
##    return a
##
##print(list(map(dollar, transactions)))



'''
reduce helps reduce a list of values
to a single result. By applying a function
to the iterable’s elements,
reduce() returns a single cumulative value.
This reduce() function is part of
Python’s functools module
'''
'''
Reduce function passes a given sequence to a function
and reduces it to a single value
'''
from functools import reduce

list1=[1,2,3,4,5]
print(reduce( lambda a,b:a*b , list1))

print(reduce( lambda a,b:a+b , range(1,11)))

#WAP to print factorial of 6 using reduce
print(reduce( lambda a,b:a*b , range(1,7)))











