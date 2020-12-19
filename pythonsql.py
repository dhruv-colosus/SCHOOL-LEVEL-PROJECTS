import mysql.connector as con

db=con.connect(
    host="localhost",
    user="root",
    passwd="password"
)

if db.is_connected():
    print("Successful")
else:
    print("nice yr")    