def convert():
    num=int(input("Enter the number : "))
    l=len(bin(num))
    print("Bin".center(l),"    ","oct".center(l)," ","dec".center(l),"   ","Hex".center(l))
    for i in range(num):
        m=bin(i).replace("0b",' ')
        n=oct(i).replace("0o"," ")
        o=hex(i).replace("0x",' ')
        ii=str(i)
        print(m.rjust(l),"",n.rjust(len(bin(num))),"     ",ii.rjust(l),"  ",o.rjust(l))
        
while(True):
    print(" You can continue the program(Yes/No) \n\t1.Yes \n\t2.NO")
    ch=input("Enter the your chise : ")
    if(ch==1 or 'Yes' or'yes'):
        print("add")
        convert()
