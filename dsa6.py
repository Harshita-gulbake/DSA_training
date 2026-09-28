n=int(input("Enter the number:"))
p_sum,c_sum=0,0
while n>0:
    a=n%10
    while (a>0):
        i=a-1
        while (i>1):
            if(a%i==0):
                c_sum+=1
                break
            else:
                p_sum+=1
                break
            i-=1
        a-=1
    n=n//10
print(p_sum)
print(c_sum)
            