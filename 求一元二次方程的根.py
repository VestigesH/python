import math
a,b,c=eval(input("请输入一元二次方程的系数:"))
if a==0:
    print("输入错误")
else:
    delta=b*b-4*a*c
    x=-b/(2*a)
    if delta==0:
        print("方程只有一根，X=%f"%(x))
    elif delta>0:
        x1=x-math.sqrt(dealt)/(2*a)
        x2=x+math.sqrt(dealt)/(2*a)
        print("方程有两个实根;X1=%f,X2=&f"%(x1,x2))
    else:
        x1=(-b+complex(0,1)*math.sqrt(-1)*delta)/(2*a)
        x2=(-b-complex(0,1)*math.sqrt(-1)*delta)/(2*a)
        print("方程有两个虚根，分别是:  ")
        print(x1,x2)
