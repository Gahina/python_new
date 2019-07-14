def armstrong(num):
    l=len(str(num))
    temp=num
    r=0
    while(num>0):
        n=num%10
        r=r+(n**l)
        num=num//10
    if(temp==r):
        print("armstrong number")
    else:
        print("not armstrong")


number=int(input("entr a number"))
armstrong(number)
        
