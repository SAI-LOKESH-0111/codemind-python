n = int(input())
a = list(map(int,input().split()))
b = sum(a)
c = b//n
if c in a:
    print('True')
else:
    print('False')