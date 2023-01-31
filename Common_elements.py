a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=[]
for i in l:
    if i in k and i not in c:
        c.append(i)
print(*c)
