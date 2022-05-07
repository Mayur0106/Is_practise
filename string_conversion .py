num="JSpm icoEr is the one OF th e&& bigGeST cOLLEge in puNE ! "
#num=input("Enter the ")
l1=''
for i in range (0,len(num)):
    if(num[i]>='a' and num[i]<='z'):
        l1=l1+num[i].upper()
    elif(num[i]>='A' and num[i]<='Z'):
        l1=l1+num[i].lower()
    else:
        l1=l1+'_'
print(l1)
