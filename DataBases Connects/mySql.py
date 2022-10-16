import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='123456',database="farmers_market",auth_plugin='mysql_native_password')

print(mydb)

cur = mydb.cursor()
cur.execute("SHOW DATABASES")

for x in cur:
    print(x)
    
cur.execute("select * from farmers_market.booth")
res = cur.fetchall()

for x in res:
    print(x)