n = int(input())
a = n
while 1:
    is_prime = True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            is_prime = False
            break
    if is_prime == True:
        break
    else:
        a += 1
b = n
while 1:
    is_prime = True
    for i in range(2,int(b**0.5)+1):
        if b%i == 0:
            is_prime = False
            break
    if is_prime == True:
        break
    else:
        b -= 1
x = a-n
y = n-b
if x<y:
    print(x)
else:
    print(y)