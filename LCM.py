a,b = map(int,input().split())
i = 1
while True:
    z = a*i
    if z%b == 0:
        print(z)
        break
    i += 1