import sys
import mysql.connector
import pymysql

"""mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "bill", 
    database ="testdb", 
    auth_plugin = "mysql_native_password")
"""
mydb = pymysql.connect(
    host = "localhost", 
    user = "root", 
    password = "bill", 
    database ="testdb")
#print(mydb)

mycursor = mydb.cursor()
"""
[[mycursor.execute("show tables")
for x in mycursor:
    print(x)
    """
mycursor.execute("CREATE TABLE if not exists sites (name VARCHAR(20), url VARCHAR(255), UNIQUE INDEX name_UNIQUE (name ASC) VISIBLE);")
mycursor.execute('show fields from sites like "id";')
mycursor.fetchone()
if mycursor.rowcount <= 0:
        mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
try:
    mycursor.execute(sql, val)
    mydb.commit()    # 数据表内容有更新，必须使用到该语句
    print(mycursor.rowcount, "记录插入成功。")
except:
    mydb.rollback()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
 
try: 
    mycursor.executemany(sql, val)
    mydb.commit()    # 数据表内容有更新，必须使用到该语句
    print(mycursor.rowcount, "记录插入成功。", "lastid:", mycursor.lastrowid)
except:
    mydb.rollback()


mycursor.execute("SELECT name, url FROM sites LIMIT 3 OFFSET 1;") 
myresult = mycursor.fetchall()
 
for x in myresult:
  print(x)

mycursor.close()