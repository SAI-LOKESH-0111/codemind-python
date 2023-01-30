def isprime(l):
    if l==1:
        return False
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return False
    return True
    
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if isprime(i)==1:
        c+=1
print(c)
        