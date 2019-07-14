def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def prime(n):
    j=2
    while(n>0):
        c=0
        for i in range(2,j):
            if j%i==0:
                break;
            else:
                c+=1
        if(c==j-2):
            j+=1
            n-=1
        else:
            j+=1
    return j-1
            

n=int(input("Enter no of terms"))
c=1
d=1
str1=""
for i in range(1,n+1):
    if(i%2!=0):
        z=fibo(c)
        str1+=str(z)+" "
        #print(z)
        c+=1
    else:
        x=prime(d)
        str1+=str(x)+" "
        #print(x)
        d+=1
print(str1)
