num=int(input("Enter the number : \n"))
flag= False
for i in range(2,num ):
    if(num%i==0):
        flag=True
if(flag):
    print(f"{num} is a not prime number. ")
else:
    print(f"{num} is a prime number .")
    


