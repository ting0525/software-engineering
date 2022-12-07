from flask import Flask, render_template, request, redirect, url_for, session , jsonify
from multiprocessing import connection
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb
import pymysql

'''
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'          # 登入ip
app.config['MYSQL_USER'] = 'root'               # 登入帳號
app.config['MYSQL_PASSWORD'] = '123456'           # 登入密碼
app.config['MYSQL_DB'] = 'test2'                  # 登入資料庫名稱
app.config['MYSQL_PORT'] = '3306'             # Port號（預設就是3306)
mysql = MySQL(app)
'''

connection = mysql.connector.connect(  
    host = '127.0.0.1' ,
    port = '3306' , 
    user = 'root', 
    password = '123456'
)

cursor = connection.cursor()



app = Flask(__name__)


@app.route('/rank' ,methods=['GET', 'POST'])
def rank():
    if request.method == "POST":
        id = request.values.get('username')
        print(id)
        cursor = connection.cursor()
        cursor.execute("USE `test`;")
        select_id = 'SELECT id , score FROM `game2` where id=%s;'
        id_tuple = (id,)
        cursor.execute(select_id, id_tuple)
        content = cursor.fetchall()
        print(content)
        #return redirect(url_for("content",content=content))
        return render_template('select.html' , content=content)
    else:
        cursor = connection.cursor()
        cursor.execute("USE `test`;")
        sql = "SELECT * FROM `game2` ORDER BY `score` DESC LIMIT 15;"
        cursor.execute(sql)
        content = cursor.fetchall()
        number = (1,2,3,4,5)
        return render_template('index.html' , content=content , len=len(number))
'''
@app.route("/<content>")
def user(content):
    return render_template("select.html",content=content)
'''

@app.route('/api/add_message/<dic>', methods=['GET'])
def add_message(dic):
    if request.method == 'GET': 
        id = request.json['id']
        score = request.json['score']   
        print(id)
        print(score)
        print(type(id))
        print(type(score))

        #print(type(data))
        cursor = connection.cursor()
        cursor.execute("USE `test`;")
        #cursor.execute('CREATE TABLE `asd`(mystr varchar(20));')
        #id = "handwrite"
        #score = 87
        
        insert_id = "INSERT INTO `game2` (id , score) VALUES(%s,%s);" 
        score_tuple = (id,score)
        
        cursor.execute(insert_id, score_tuple)
        connection.commit()
        cursor.execute("SELECT * FROM `game2` ORDER BY  `score` DESC LIMIT 3;")
        records = cursor.fetchall()
        for r in records:
            print(r)
        return jsonify({"dic":dic})
    
'''
@app.route('/rank/select/' , methods=['GET' , 'POST'])
def select():
    if request.method == "POST":
        id = request.form['id']
        id = 'testlast'
        cursor = connection.cursor()
        cursor.execute("USE `test`;")
        select_id = 'SELECT id , score FROM `game2` where id=%s;'
        id_tuple = (id,)
        cursor.execute(select_id, id_tuple)
        content = cursor.fetchall()
        return render_template('select.html' , content=content)
    else:
        return render_template('index.html' , content=content)
'''





if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True , port=80)
    
'''
def add_message(dic):
    content = request.json
    print(content)
    print(type(content))
    print(content['id'])
    return jsonify({"dic":dic})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
    
'''


'''
connection = mysql.connector.connect(  
    host = '127.0.0.1' ,
    port = '3306' , 
    user = 'root', 
    password = '123456'
    )
def record(content):
    cursor = connection.cursor()
    cursor.execute("USE `test`;")
    id = content['id']
    score = content['score']
    print(id)
    print(score)
    insert_stmt = "INSERT INTO `game` VALUES(%s,%d);"
    cursor.execute(insert_stmt, id , score)
    connection.commit()
'''

#cur = mysql.connection.cursor()
    #cur.execute("INSERT INTO `game` (id , score) VALUES (%s,%d)" , (id , score))
    #mysql.connection.commit()
    
    
    #cur = mysql.connection.cursor()
        #sql = "INSERT INTO `game` (id , score) VALUES ('{id}' , '{score}');"
        #cur.execute(sql, id , score)
        #print(sql)