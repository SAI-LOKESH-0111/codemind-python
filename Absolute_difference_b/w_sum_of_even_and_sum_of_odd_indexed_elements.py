n = int(input())
a = list(map(int,input().split()))
se = 0
so = 0
for i in range(n):
    if i%2 == 0 :
        se += a[i]
    else:
        so += a[i]
print(se-so)