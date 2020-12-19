import mysql.connector

connection=mysql.connector.connect(host="localhost", database='use_student',user="root",password="password")

cursor=connection.cursor()

cursor.execute("select * from cakefactory")

records=cursor.fetchall()
print("+------+--------------------+-----------------+---------------------+-------------------------+--------------------+")
print("| ID   | Cakes              | 500gm Eggless   | 1000g Eggless       | 500gm WithEgg           | 1000gm Withoutegg  |  ")
print("+------+--------------------+-----------------+---------------------+-------------------------+--------------------+")
for row in records:
    print("|",row[0],end="    ")
    print("|",row[1],end="       ")
    print("|",row[2],end="             ")
    print("|",row[3],end="                 ")
    print("|",row[4],end="                     ")
    print("|",row[5],"               |")
    print("+------+--------------------+-----------------+---------------------+-------------------------+--------------------+")

