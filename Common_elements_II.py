a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=[]
for i in l:
    if i not in k and i not in c:
        c.append(i)
for i in k:
    if i not in l and i not in c:
        c.append(i)
print(*c)
