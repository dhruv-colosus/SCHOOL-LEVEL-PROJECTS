import mysql.connector as mycon

con=mycon.connect(host="localhost",username="root",passwd="password",database="use_student")

cur=con.cursor()

command="SELECT * FROM Login_Data"

cur.execute(command)

username1="Dhrhuv"

mainlist1=[]

user_list=[]

results=cur.fetchall()

for a in results:
    d=list(a)
    mainlist1.append(a)
for i in mainlist1:
    user=i[0]
    user_list.append(user)    

if username1 in user_list :
    print("YES")

else:
    print("NO")
        
