def square(n):
    y=2
    if n==1:
        return 1
    else:
        print(n*square(n,y-1))


n=5
print(square(n))            