value=int(input())
i=1
#logic
while(i<=value):
    count5=0
    count1=0
    count2=0
    n5=i//5
    n=i%5
    n2=n//2
    n1=n%2
    count5+=n5
    count2+=n2
    count1+=n1
    print("amount is",i)
    #print("no of 5re coin",count5)
    #print("no of 2re coin",count2)
    #print("no of 1re coin",count1)
    print("min no of coins required",count5+count2+count1)
    i+=1
