n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=[]
for i in l:
    if i<=a:
        c.append(i)
print(sum(c))