n = int(input())
m = int(input())
for i in range(n,m+1):
    a = i
    b = a
    c = 0
    while a>0:
        r = a%10
        c = (c*10)+r
        a = a//10
    if b==c:
        print(c, end=' ')
    else:
        pass