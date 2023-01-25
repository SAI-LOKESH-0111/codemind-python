n=int(input())
l=list(map(int,input().split()))
k=set(l)
j=list(k)
s=0
for i in range(len(j)):
    if j[i]%2 == 1:
        s += j[i]
print(s)