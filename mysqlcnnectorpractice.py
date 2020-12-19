import mysql.connector as mycon

newcon=mycon.connect(host="localhost",username="root",database="use_student",password="password")

cur=newcon.cursor()

command="SELECT * FROM login_data"

cur.execute(command)

username=input("Enter your name : ")

password=input("Enter your password : ")

results=cur.fetchall()
i=0
for a in results:
    if username==(list(a))[1] and password==(list(a))[2]:
        print("Access Provided")
        i=1
        break
    else:
        continue
        
if i==0:
    print("Access Denied")
else:
    pass  
