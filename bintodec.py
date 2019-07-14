def bintodec(num):
    c=0
    r=0
    l=len(str(num))
    while(l>0):
        n=num%10
        r=r+n*(2**c)
        num=num//10
        c+=1
        l-=1
    return r

number=int(input("enter a binary number"))
print(bintodec(number))
