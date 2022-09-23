n = int(input())
s = 1
for i in range(1,n+1):
    if n%i == 0:
        s = s*i
if s==n:
    print('prime')
else:
    print('not a prime')