n = int(input())
s = 0
for i in range(1,n+1):
    if i*i == n:
        s = 1
if s==1:
    print('True')
else:
    print('False')