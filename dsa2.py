n=int(input())
a=[]
sum=0
for i in range(n):
    c=int(input())
    a.append(c)
for i in range(len(a)):
    if a[i]>=10 and a[i]%2==0:
        sum+=1
print(sum)