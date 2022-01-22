n=1
while(n<=100):
    count=0
    i=1
    while(i<=n):
        if (n%i==0):
            count=count+1
        i=i+1
    if(count==2):
        print(n)
    n=n+1

n=23
i=2
while(i<=n-1):
    if (n%i==0):
        count=count+1
        print("not prime")
        break
    i=i+1
if (count==0):
    print("prime")


#one two 100 prime number