import pymysql
 
# 打开数据库连接
try:
    config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'bill',
    'port': 3306,
    'database': 'testdb',
    'charset': 'utf8'
    }   
    #db = pymysql.connect("localhost","root","bill","mydb" )    
    #db = pymysql.connect(host = "localhost", user = "root", password = "bill", database = "mydb")
    db = pymysql.connect(**config) #**解包字典
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
 
    # 使用 execute()  方法执行 SQL 查询 
    rowcount = cursor.execute("SELECT * from users;")
    print(rowcount)#or cursor.rowcount
    
    for data in cursor:
        print(data)
    results = cursor.fetchall()        #上面已fetch，所以后面的fetchall不生效
    print("--fetchall")
    for data in results:
        print(data)

    
    # 使用 fetchone() 方法获取单条数据.
    #data = cursor.fetchone()
    
    #print ("Database version : %s " % data) 
    # 关闭数据库连接
except pymysql.err.MySQLError as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    db.close()
