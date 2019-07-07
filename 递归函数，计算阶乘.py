def fac(n):
    if n==0:
        f=1
    else:
        f=fac(n-1)*n;
    return f

n=int(input("please input n: "))
f=fac(n)
print("%d!=%d"%(n,f))
