def fun(a):
    s=''
    for i in range(1,a+1):
        s=s+(str(i))
    print(s)
    
a=int(input())
while a>0:
    fun(a)
    a=a-1