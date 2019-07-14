str1=input()
if str1[0]=='-':
    newstr="-"
else:
    newstr=""

l1=['0','1','2','3','4','5','6','7','8','9']
for i in str1:
    if i in l1:
        newstr+=i

print(newstr)
    
