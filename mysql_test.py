import mysql.connector                 

# mysql1.py
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'bill',
    'port': 3306,
    'database': 'mydb',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
    exit()
cursor = cnn.cursor()
try:
    res = cursor.execute("select id from user where name='Bony';")
    print(res)
    result = cursor.fetchall()
    if len(result) == 0:
        sql_insert = 'insert into user(name, sex, age, mobil) \
            values("Tony", 1, 12, "3234345545")'
        cursor.execute(sql_insert)
        cnn.commit()
    sql_query = 'select name,age from user ;'
    cursor.execute(sql_query)
    result = cursor.fetchall()
    print(len(result))
    for name, age in result:
        print (name, age)

except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()
