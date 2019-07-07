n = int(input("输入一个正整数"))
t = n
i=2
while n != 1:
    if n%i==0:
        n = n/i
        print("%d*" % i,end="")
        i=2
    i+=1


print("\b=%d" % t)
