def gp(a,b):
    return(a**b)
n=int(input("enter no of terms"))
str1=""
c=0
d=0
for i in range(0,n):
    if(i%2==0):
        x=gp(2,c)
        str1+=str(x)+" "
        c+=1
        #print(x)
    else:
        y=gp(3,d)
        str1+=str(y) +" "
        d+=1
        #print(y)

print(str1)
