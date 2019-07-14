str1=input("enter array elements")
l1=str1.split(" ")
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if int(l1[i])>int(l1[j]):
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp

for i in l1:
    print(int(i))
