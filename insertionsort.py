str1=input("enter array elements")
l1=str1.split(" ")
for i in range(1,len(l1)):
    j=i-1
    temp=int(l1[i])
    while(j>=0 and temp<int(l1[j])):
        l1[j+1]=l1[j]
        j-=1
    l1[j+1]=temp

print(l1)
