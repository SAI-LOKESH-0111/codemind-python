def add(num):
    a = num
    s = 0
    while a>0:    
        r = a%10
        s += r
        a = a//10
    a=s
    
    if s>=9:
        return add(s)
    else:
        return s

num = int(input())
print(add(num))