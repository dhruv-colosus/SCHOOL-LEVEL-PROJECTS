a=int(input())
if a<=10 and a>=1:
    b=input()
    list1=b.split(' ')
    print(list1)
    for d in range(len(list1)):
        number=int(list1[d])
        for b in range(1,number+1):
            if b%15==0:
                print("FizzBuzz")
            elif b%5==0:
                print("Buzz")
            elif b%3==0:
                print("Fizz")    
            else:
                print(b)    
else:
    pass                