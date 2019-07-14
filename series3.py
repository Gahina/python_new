n=int(input("enter no of terms"))
c=-2
str1=""
for i in range(1,n+1):
    if i%2!=0:
        c+=2
        str1+=str(c)+" "
    else:
        d=c//2
        str1+=str(d)+" "

print(str1)
