def xn(x,n):
    if n==0:
        f=1
    else:
        f=x*xn(x,n-1)
    return f

x,n=eval(input("please input x and n:"))
if n<0:
    n=-n
    y=xn(x,n)
    y=1/y
else:
    y=xn(x,n)
print(y)
        
