n=int(input())
z=n
s=0
while z>0:
    a=z%10
    s=s*10+a
    z=z//10
if s==n:
    print('True')
else:
    print('False')