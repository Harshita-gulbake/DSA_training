n=int(input())
step=0
while(n>0):
    if n>5:
        n=n-5
        step+=1
    else:
        step+=1
        break
print(step)