n=int(input())
l=list(map(int,input().split()))
k=n//2
a=0
b=0
for i in range(n//2):
    a=a+l[i]
for j in range(k,n):
    b=b+l[j]
print(a)
print(b)