def fibs(n):
    if n==1 or n==0:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)
L=[x for x in map(fibs,range(10))]
print(L)
