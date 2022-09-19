a,b = map(int,input().split())
if a==b-1 or a-1==b:
    print('Yes')
elif a==b+9 or a+9==b:
    print('Yes')
else:
    print('No')