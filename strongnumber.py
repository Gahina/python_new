def fact(num):
    res=1
    while(num>1):
        res=res*num
        num=num-1
    return res

def strong(n):
    r=0
    while(n>0):
        n1=n%10
        r=r+fact(n1)
        n=n//10
    return r

number=int(input("enter a number"))
if number==strong(number):
    print("it is a strong number")
else:
    print("not a strong number")
    
