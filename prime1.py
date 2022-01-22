n = 22
i = 2
count = 0
while (i<=n-1):
    if (n%i==0):
        count=count+1
        print("not prime")
        break
    i+=1
if (count==0):
    print("prime")