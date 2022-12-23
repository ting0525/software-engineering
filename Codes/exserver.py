from flask import Flask, render_template, request, redirect, url_for, session , jsonify
from multiprocessing import connection
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb
import pymysql


#資料庫設定
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



def partial_table(p):
  prefix = set()
  res = [0]
  for i in range(1,len(p)):
    prefix.add(p[:i])
    postfix = {p[j:i + 1] for j in range(1,i + 1)}
    res.append(len((prefix & postfix or {''}).pop()))
  return res

def kmp_match(s,p):
  m = len(s)
  n = len(p)
  cur = 0 # 起始指標cur
  table = partial_table(p)
  while cur <= m - n:   #只去匹配前m-n個
    for i in range(n):
      if s[i + cur] != p[i]:
        cur += max(i - table[i - 1],1) # 有了部分匹配表,我們不只是單純的1位1位往右移,可以一次移動多位
        break
    else:    
      return True # loop從 break 中退出時，else 部分不執行。
  return False





app = Flask(__name__)


@app.route('/rank' ,methods=['GET', 'POST'])
def rank():
    if request.method == "POST":
        idtext = request.values.get('username')
        id = (idtext,)
        print(id)
        cursor = connection.cursor()
        cursor.execute("USE `test`;")
        select_all_id = 'SELECT id FROM `game2`;'
        cursor.execute(select_all_id)
        all_id = cursor.fetchall()
        token = False
        for i in all_id:
            print(idtext)
            print(i[0])
            m = i[0]
            token = kmp_match(m , idtext)
            if token==True:
                break
            
            
        if token == True:
            cursor = connection.cursor()
            cursor.execute("USE `test`;")
            select_id = "SELECT id , score FROM `game2` WHERE `id` LIKE '%%%s%%';" % (idtext)
            id_tuple = (idtext,)
            print(id_tuple)
            cursor.execute(select_id)
            content = cursor.fetchall()
            print(content)
            length=len(content)
            return render_template('select.html' , content=content , len=length)
        elif token == False:
            return render_template('Not find.html')
    else:
        cursor = connection.cursor()
        cursor.execute("USE `test`;")
        sql = "SELECT * FROM `game2` ORDER BY `score` DESC LIMIT 15;"
        cursor.execute(sql)
        content = cursor.fetchall()
        number = (1,2,3,4,5)
        return render_template('index.html' , content=content , len=len(number))


@app.route('/api/add_message/<dic>', methods=['GET'])
def add_message(dic):
    if request.method == 'GET': 
        id = request.json['id']
        score = request.json['score']
        my_token = request.json['my_token']  
        print(id)
        print(score)
        print(type(id))
        print(type(score))
        if my_token == 123456:
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
    






if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True , port=80)
    
    
    
