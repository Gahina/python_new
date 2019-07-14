str1=input("enter 1st string")
str2=input("enter 2nd string")
str3=input("enter 3rd string")
newstr1=""
newstr2=""
newstr3=""
for i in str1:
    if i in ['A','E','I','O','U','a','e','i','o','u']:
        newstr1+='"'
    else:
        newstr1+=i

for i in str2:
    if i not in ['A','E','I','O','U','a','e','i','o','u']:
        newstr2+='*'
    else:
        newstr2+=i

for i in str3:
    if i.islower()==True:
        newstr3+=i.upper()
    else:
        newstr3+=i

print(newstr1)
print(newstr2)
print(newstr3)
