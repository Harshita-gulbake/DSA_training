k=int(input())
n=int(input())
w=int(input())
c=0
p=0
for i in range(1,w+1):
    p+=i*k
if p>n:
    print(p-n)
else:
    print(0)