n = int(input())
m = int(input())
l = 0
k = 0
for i in range(1,n):
    if n%i == 0:
        l += i
for j in range(1,m):
    if m%j == 0:
        k += j
if l==m and k==n:
    print('Amicable')
else:
    print('Not Amicable')