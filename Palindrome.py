n=int(input())
a=n
s=0
while a>0:
    b=a%10
    s=s*10+b
    a=a//10
if s==n:
    print('True')
else:
    print('False')