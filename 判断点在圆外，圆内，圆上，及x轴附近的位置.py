x,y=eval(input("请输入x和y:"))
if  x**2+y**2<=1:
    if x**2+y**2==1:
         print("点(%f,%f)在圆上"%(x,y))
    else:
         print("点(%f,%f)在圆内"%(x,y))
else:
    if y>=0:
        if y==0:
           print("点(%f,%f)在圆外，在x轴上"%(x,y))
        else:
            print("点(%f,%f)在圆外，在x轴上方"%(x,y))
    else:
         print("点(%f,%f)在圆外，在x轴下方"%(x,y))
         
