import DBAL

class Employee:

    def __init__(self , empid=1, empname="name" ,  doj="2024-01-01" , salary=1000 ,depid=1 ,age=3 , country="india" , contact=10):
        self.empId= empid
        self.empName= empname
        self.DOJ= doj
        self.salary=salary
        self.depId= depid
        self.age=age
        self.country=country
        self.contact= contact

    def get(self):
        d=DBAL.getData()
        return d

    def post(self):
        DBAL.insertData(self)
        

    






        




    
