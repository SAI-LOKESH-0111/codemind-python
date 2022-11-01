n = int(input())
s = 0
for i in range(1,n+1):
    if n==i*(i+1):
        s = 1
if s==1:
    print('YES')
else:
    print('NO')