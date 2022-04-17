import mysql.connector                 

# mysql1.py
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'bill',
    'port': 3306,
    'database': 'testdb',
    'charset': 'utf8',
    'auth_plugin': "mysql_native_password"
}
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
    exit()
cursor = cnn.cursor()
try:
    res = cursor.execute("select userid from users where username='Tony';")
    print(res)
    result = cursor.fetchall()
    if len(result) == 0:
        try:
            sql_insert = 'insert into users(userid, username, sex, age, birthday, Tel, mobil) \
                values(1003, "Tony", 1, 12, "2007-1-2", "54391151", "3234345545")'
            cursor.execute(sql_insert)
            cnn.commit()
        except mysql.connector.Error as e:
            print(e)       
        
    sql_query = 'select username, age from users ;'
    cursor.execute(sql_query)
    result = cursor.fetchall()
    print(len(result))
    for username, age in result:
        print (username, age)

except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()
