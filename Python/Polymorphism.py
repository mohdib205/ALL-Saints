'''
Polymorphism means using the same method name
for different objects, but each object
can have its own implementation of that method.
'''




#Different Forms of Polymorphism
'''
1.Method Overriding

Method overriding refers to
defining a method in a subclass with the
same name as a method in its superclass.
The method that gets called depends on the
type of the object at runtime.
'''
class Member:
     def __init__(self, Name, Contact):
         self.name=Name
         self.contact=Contact
     def info(self):
         print(f"{self.name} is instance of Member")
         
class Student(Member):
    
    def info(self):
        print(f"{self.name} is instance of Student class")

member1=Member("Saklen" , 12345)
student1=Student("Gyan" , 787878)
member1.info()
student1.info()


    



'''
2.Operator overloading
Operator overloading is used to modify
the behavior of an existing operator
by redefining a special method, often called
a magic method, in a class.
These special methods are automatically called
when their associated operator is used with
objects of the class.
This allows you to customize how operators
like +, -, or * work for your class objects,
making the operations more   meaningful.
'''

class Product:
    def __init__(self, name , price , stock):
        self.name=name
        self.price=price
        self.stock=stock
    def __add__(obj1, obj2):
        return obj1.name + obj2.name
    def __sub__(obj1,obj2):
        return obj1.stock- obj2.stock
p1=Product("pen" , 10 , 100)    
p2=Product(" pencil" , 5 , 40)    
print(p1+p2)
print(p1-p2)




#3. Method Overloading


