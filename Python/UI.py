import BLL

user_input=input("Enter G to get data , I to insert data , U to update data and D to delete data")

if user_input=="G":
    obj=BLL.Employee()
    data=obj.get()
    for d in data:
        print(data)

elif user_input=="I":
    id= int(input("Enter Id "))
    name=input("Enter name ")
    doj=input("Enter date of joining " )
    salary=float(input("Enter Salary " ))
    depId=int(input("Enter Department Id " ))
    age=int(input("Enter Age " ))
    country=input("Enter Country " )
    contact= int(input("Enter contact " ))
    obj1=BLL.Employee(id,name ,doj,salary , depId,age, country,contact)
    obj1.post()
    print("data submitted successfully")
    


    
