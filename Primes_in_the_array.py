def isprime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if isprime(i)==True:
        c+=1
print(c)