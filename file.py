def my():
   
    count=0
    lines=0
    vowels=0
    char=0  
    A=0
    title=0
    
    f=open("D:\Coding\my stuff\school level python\my.txt","r") 
    string1=f.read()
    print(string1)

    print(f.newlines)
    #No. of Lines
    list2=string1.split('\n')
    lines=len(list2)

    #Occurences of word

    list1=string1.split(' ')
    m=input("Which word to find : ")
    for a in range(len(list1)):
        if list1[a].lower()==m.lower():
            count+=1
    
    #Occurences of lines with A
    for a in list2:
        if a[0]=="A":
            A+=1
        else:
            continue    
    
    #No. Of words
    words=len(list1)
    f.close()

    #No. of vowels
    for a in range(len(string1)):
        if string1[a] in ['a','e','i','o','u']:
            vowels+=1
    
    #Smaller than 4 Char
    for a in range(len(list1)):
        if len(list1[a])<=4:
            char+=1
    
    #No.of words with Uppercasre CHar
    for a in range(len(list1)):
        if list1[a].istitle():
            title+=1

    print("No. of occurences of word ",m ," are ",count)  
    print("No. of lines are : ",lines) 
    print("No of lines which start with the word A are : ",A)
    print("No of Words in the file are : ",words)
    print("No of Vowels in the file are : ",vowels)
    print("No of Char less than 4 len in the file are : ",char)
    print("Words Starting With UpperCase Character : ",title)


if __name__ == "__main__":
    my()
