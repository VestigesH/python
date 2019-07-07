def getMax(a,b,c):
    if a>b:
        max=a
    else:
        max=b
    if c>max:
        c=max
    return max
a,b,c=eval(input("input a,b,c:"))
n=getMax(a,b,c)
print("max=",n)
            
