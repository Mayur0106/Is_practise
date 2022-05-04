num=input("Enter the string : ")
l1=''
for i in num:
    if(i>='a' and i<='z'):
        l1=l1+i.upper()
    elif(i>='A' and i<='Z'):
        l1=l1+i
    else:
        l1=l1+'__'
print(l1)
