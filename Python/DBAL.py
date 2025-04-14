#CRUD
##Create , Insert  , Post
##
##Read , Get , Fetch , Retreive
##
##Update  , put
##
##Delete

import pymysql
def Connection():
    conn= pymysql.connect(host='localhost' , user='root' ,
                db= 'EMS' , password='mysql' )
    return conn

def getData():
    con=Connection()
    cursor= con.cursor()
    cursor.execute("select * from Employee")
    data=cursor.fetchall()
    return data


def insertData(obj):
    con=Connection()
    cursor= con.cursor()
    cursor.execute(f"INSERT INTO Employee (EmpID, EmpName, DOJ, Salary, DepartmentID, Age, Country, Contact) values ({obj.empId} , '{obj.empName}' , '{obj.DOJ}' , {obj.salary} , {obj.depId} , {obj.age} ,'{obj.country}' , {obj.contact} )")
    con.commit()
    con.close()

    

    






    
    





    
    
    






































