n,m=map(int,input().split())
while n != 0 and m != 0:
    if n>m:
        n %= m
    else:
        m %= n
if m==0:
    print(n)
else:
    print(m)