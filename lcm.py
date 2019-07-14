def lcm(a,b):
    if(a==b):
        return a
    elif(a==0 or b==0):
        return 0
    else:
        if(a>b):
            large=a
        else:
            large=b
        while(1):
            if(large%a==0 and large%b==0):
                return large
            else:
                large+=1

a=int(input("enter a number"))
b=int(input("enter a number"))
x=lcm(a,b)
print(x)
