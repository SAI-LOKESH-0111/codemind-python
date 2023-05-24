def fun(a):
    l=' '
    s=''
    for i in range(1,a+1):
        s=(str(i))+l+s
    print(s)
    
a=int(input())
for i in range(a):
    fun(a)