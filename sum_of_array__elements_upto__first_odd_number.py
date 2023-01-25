n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    if l[i]%2==1:
        break
    else:
        c.append(l[i])
print(sum(c))