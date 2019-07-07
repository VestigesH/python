
a,b,c=eval(input("a,b,c=   "))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print ("area=",s)
else:
    print("这三条边不能构成三角形")
