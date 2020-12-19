import mysql.connector


connector=mysql.connector.connect(host="localhost" ,user="root",passwd="password", database="use_student" )

mycursor=connector.cursor()

# mycursor.execute("Show Databases")

# for i in mycursor:
#     print(i)

mycursor.execute("select * from students")

result=mycursor.fetchone()

for i in result:
    print(i)

