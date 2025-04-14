#inheritance

# When we are creating a class we can inherit
##all of the fields and methods
# from another class.
#This is called inheritance.
 
# The class that inherits is called the subclass
##child and the class we
# inherit from is the super/parent class

##1. Single Inheritance


class A:
    a="Hello"

    def __init__(self , num1, num2):
        self.num1=num1
        self.num2=num2

    def details(self):
        print(self.num1 , self.num2 )

class B(A):
    pass

obj_a=A(12,22)
obj_a.details()


print(B.a)
obj_b=B(25,50)
obj_b.details()




    

##2. Multiple Inheritance

class parent1:
    name="parent1"
    num=50

    def method1(self):
        print("this is method 1 of parent 1")

    def method2(self):
        print("this is method 2")

class parent2:
    num=25

    def method1(self):
        print("this is method 1 of parent2")
        

class child(parent1,parent2):
    pass
class child2(parent2,parent1):
    pass

c1=child()
c2=child2()
c1.method2()

c1.method1()
print(c1.num)
print()
c2.method1()
print(c2.num)



##3. Multilevel Inheritance




