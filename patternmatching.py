test=int(input())
count=1
while(count<=test):
    str1=input()
    c=0
    match=input()
    newstr=""
    len1=len(match)
    for i in range(0,len(str1)):
        if str1[i]==match[0]:
            t=i
            for j in range(0,len1):
                if t<len(str1):
                    #print(str1[t])
                    newstr+=str1[t]
                    t+=1
            print(newstr)
            if newstr==match:
                #print("found")
                c=1
                break
                
            else:
                #print("not found")
                c=0
        newstr=""
                
    if(c!=1):
        print("not found")
    else:
        print("found")
                
    count+=1
