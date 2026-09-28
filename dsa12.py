n=int(input())
temp=n
place=1
while(temp>0):
    a=temp%10
    if a!=0:
       print(a*place)
    temp=temp//10
    place*=10