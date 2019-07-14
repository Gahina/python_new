def dectooct(num):
    r=0
    i=0
    while(num>0):
        n=num%8
        r=r+n*(10**i)
        i+=1
        num=num//8
    return r

number=int(input("enter a number"))
print(dectooct(number))
                 
