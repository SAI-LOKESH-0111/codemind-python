n = int(input())
a = n*n
ra = 0
while n>0:
    r = n%10
    ra =(ra*10) + r
    n = n//10
b = ra * ra
rb = 0
while b>0:
    rr = b%10
    rb =(rb*10) + rr
    b = b//10
if rb==a:
    print('True')
else:
    print('False')