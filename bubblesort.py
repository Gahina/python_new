str1=input("enter elements")
list1=str1.split(" ")
l=len(list1)
for i in range(0,l):
    for j in range(0,l-i-1):
        if int(list1[j])>int(list1[j+1]):
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print(list1)
