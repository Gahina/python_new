def fibo(n):
    x=0
    y=1
    z=0
    print(x)
    print(y)
    while(n>0):
        z=x+y
        x=y
        y=z
        print(z)
        n-=1
        
r=int(input("enter the range"))
fibo(r-2)
