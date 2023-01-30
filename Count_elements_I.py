a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=[]
for i in l:
    for j in k:
        if i==j:
            c.append(i)
d=set(c)
print(len(d))
