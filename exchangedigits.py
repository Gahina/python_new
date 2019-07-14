str1=input()
l1=str1.split()
a=l1[0]
b=l1[1]
l2=[]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        str2=a[i]+a[j]
        print(str2)
        if(len(str2)==len(b)):
            l2.append(str2)
    str2=""
l1.reverse()
for i in range(0,len(a)):
    for j in range(i,len(a)):
        str2=a[i]+a[j]
        if(len(str2)==len(b)):
            l2.append(str2)
    str2=""

print(l2)

