n=int(input())
l=list(map(int,input().split()))
k=set(l)
j=list(k)
c=0
for i in range(len(k)):
    if j[i]%2 == 0:
        c += 1
print(c)