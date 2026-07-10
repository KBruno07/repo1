import pymysql
mydb = pymysql.connect(
    host="192.168.0.124",
    user="newuser",
    password="stop1",
    database="finance_tracker"
)
print(mydb)

cursor = mydb.cursor()

