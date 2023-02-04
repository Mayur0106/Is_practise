strr=" India is the seventh-largest country by area  and the second-most populous country in the world, situated in Asiab   "
a=strr.split()
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
        temp=i
print(temp)
print(len(temp)) 
