sum=0
n=int(input("enter the number:"))
while n>0:
    a=n%10
    sum+=a
    n=n//10    
print(sum)
