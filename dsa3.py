n=int(input("Enter the number:"))
i=n-1
while(i>1):
    if n%i==0:
        print("It is not prime")
        break
    i-=1
else:
    print("It is prime")
    