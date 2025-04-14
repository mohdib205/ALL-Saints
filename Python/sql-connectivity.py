import pymysql

connection=pymysql.connect(host='localhost', 
        user='root',  
        password = "mysql", 
        db='demo')

cur_obj =connection.cursor()
cur_obj.execute("select * from Customer")
##print(cur_obj.fetchall())
cur_obj.close()

##cur_obj =connection.cursor()
##cur_obj.execute("Insert into Customer (id , Name , Age, Location, Gender)values(22, 'new' , 23 , 'Bhopal' , 'Male')")
##connection.commit()
##cur_obj.close()

cur_obj =connection.cursor()
cur_obj.execute("Update  Customer set Name='old' where id = 22")
connection.commit()
cur_obj.close()

cur_obj =connection.cursor()
cur_obj.execute("delete from Customer where id=22")
connection.commit()
cur_obj.close()

cur_obj =connection.cursor()
cur_obj.execute("select * from Customer")
print(cur_obj.fetchall())
cur_obj.close()


