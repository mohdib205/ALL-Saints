'''
OOP (Object-Oriented Programming): A way of organizing programs by
grouping related data and actions into "classes" and "objects."

Class: A blueprint or template that defines
how to create objects.
Object: A specific real world-entity created using a class.

Static Properties: Features of a class that
belong to the class itself, not to individual
objects.

Instance Properties: Features of a class that
are unique to each object.

Constructor: A special method used to set up
an object when it is created.
'''

class Student:
    school_name="LGS"  #static method

    def __init__(self , N, C):
        self.name=N #instance variables
        self.Class=C

    def read(self):
        print( f"{self.name} is reading")

    def __str__(self): #function that is added to a class to control what shows up when we print an object or turn it into a string
    
        return self.name      

##s1=Student("abc" , 10)
##print(s1.name)
##print(s1.Class)
##
##s1.name="Abc"
##
##Faiz=Student("faiz" , 12)
##Shahid=Student("shahid",11)
##
##Faiz.read()
##Shahid.read()
##
##print(s1 , Faiz , Shahid)

##class Fruits , instance variables Color,Taste,
##Size
##
##method eat():

##@staticmethod


class Fruit:
    def __init__(self,name="a", Color="a" , Taste,Size):
        self.name=name
        self.color=Color
        self.taste=Taste
        self.size=Size

    def change_color(self , new):
        self.color=new
        
        
    @staticmethod
    def eat():
        print("Fruit is eaten")

apple=Fruit("Apple","red","sweet",5)

apple.color="Orange"
print(apple.color)


apple.change_color("green")
print(apple.color)





        








    







