def dectobin(num):
    r=0
    i=0
    while(num>0):
        n=num%2
        r=r+n*(10**i)
        num=num//2
        i+=1
    return r   
   


number=int(input("enter a number"))
print(dectobin(number))
#l3=l2.reverse()
#print(l2)

    
