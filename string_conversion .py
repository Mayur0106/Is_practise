<<<<<<< HEAD
num="JSpm icoEr is the one OF th e&& bigGeST cOLLEge in puNE ! "
#num=input("Enter the ")
=======
num=input("Enter the string : ")
#>>>>>> 9c33794ec8331ca9633e3f102581f0a7a647b6f6
l1=''
for i in range (0,len(num)):
    if(num[i]>='a' and num[i]<='z'):
        l1=l1+num[i].upper()
    elif(num[i]>='A' and num[i]<='Z' ):
        l1=l1+num[i].lower()
    else:
#<<<<<<< HEAD
        l1=l1+'_'
#=======
        l1=l1+'__'
#>>>>>>> 9c33794ec8331ca9633e3f102581f0a7a647b6f6
print(l1)
