   
f=open("F:\school level python\my.txt","r") 
string1=f.read()
print(string1)
print(f.closed)
print(f.mode)
print(f.newlines)
   
f.close()
