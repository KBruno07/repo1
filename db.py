import pymysql
mydb = pymysql.connect(
    host="192.168.0.124",
    user="newuser",
    password="stop1",
    database="finance_tracker"
)

cursor = mydb.cursor()
cursor.execute("CREATE TABLE users(user_id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255))")
