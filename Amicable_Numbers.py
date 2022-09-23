n = int(input())
m = int(input())
ns = 0
ms = 0
for l in range(1,n):
    if n%l == 0:
        ns += l
for k in range(1,m):
    if m%k == 0:
        ms += k
if n==ms and m==ns:
    print('Amicable')
else:
    print('Not Amicable')