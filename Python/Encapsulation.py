#Encapsulation
'''
Encapsulation in Python means keeping
data (variables) and methods (functions)
inside a class and controlling how they can
be accessed or changed.
It helps protect the data and ensures
it is used properly.
'''


#Access Modifiers: they control the access of variables and methods

'''
Public: Accessible from anywhere in the program.
Protected: Accessible within the class and its child classes.
Private: Accessible only within the class itself.
'''
'''
Getter Setter
Getter: method to access the value of a private variable.
Setter: method to modify the value of a private variable in a controlled way.
'''





class Employee: 
    def __init__(self , name,salary , job_title):
        self.name= name
        self._jobtitle=job_title #protected attribute
        self.__salary= salary #private

    def get_salary(self): #getter
        return self.__salary
    def change_salary(self, new_salary):  #setter
        self.__salary= new_salary      
emp1= Employee("Vivek" , 8000 , "Manager")
print(emp1.name)
print(emp1._jobtitle)
emp1._jobtitle="Developer"
print(emp1._jobtitle)

emp1.change_salary(12000)
print(emp1.get_salary())






    
