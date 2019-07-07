x=int(input("请输入一个三位整数:"))
a=x//100
b=(x-a*100)//10
c=x-100*a-10*b
if a**3+b**3+c**3==x:
    print(x,"是水仙花数")
else:
    print(x,"不是水仙花数")
