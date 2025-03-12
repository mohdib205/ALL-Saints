from django.shortcuts import render 
from demoapp.models import Student
# Create your views here.

def func1(request):
    print(" function 1 is executing")
    return render(request , "home.html")

def studentv(request):
    objs=Student.objects.all()
    print(objs)
    for o in objs:
        print(o)
        print(o.name)
        print("age" , o.age)
    
    return render(request , "student.html" , {"a":objs} )    


    
    
