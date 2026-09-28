n=int(input())
d=0
a,b,c=0,0,0
for i in range(n):
    a,b,c=map(int,input().split())
    a+=a
    b+=b
    c+=c
if a==0 and b==0 and c==0:
    print("YES")
else:
    print("NO")