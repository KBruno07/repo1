import pymysql
mydb = pymysql.connect(
    host="192.168.0.124",
    user="Kiberbiztos",
    password="Kiberbiztos007!",
    database="finance_tracker"
)
print(mydb)