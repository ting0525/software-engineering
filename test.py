from multiprocessing import connection
import mysql.connector
import MySQLdb


connection = mysql.connector.connect(  
    host = '127.0.0.1' ,
    port = '3306' , 
    user = 'root', 
    password = '123456'
)
cursor = connection.cursor()

cursor.execute("USE `test`;")
id = "testttt"
id_tuple = (id,)
#cursor.execute('CREATE TABLE `asd`(mystr varchar(20));')
sql = 'SELECT id , score FROM `game2` where id=%s;'
cursor.execute(sql ,id_tuple)
content = cursor.fetchall()
print(content)
number = (1,2,3,4,5)
print(len(number))
#for i in content:
   #print(i)
connection.commit()

#cursor.close()
connection.close()






