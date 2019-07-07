num=int(input("请输入一个三位整数: "))
a=num//100
b=(num-a*100)//10
c=num-a*100-b*10
if num==a**3+b**3+c**3:
    print("%d是水仙花数",num)
else:
    print("%d不是水仙花数",num)
