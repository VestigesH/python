def getMaxMin(x):
    max=x[0]
    min=x[0]
    for i in range(0,len(x)):
        if max<x[i]:
            max=x[i]
        if min>x[i]:
            min=x[i]
    return (max,min)

a_list=[-1,28,-15,5,10]
x,y=getMaxMin(a_list)
print("a_list=",a_list)
print("最大元素=",x,"最小元素=",y)

string="Hello"
x,y=getMaxMin(string)
print("string=",string)
print("最大元素=",x,"最小元素=",y)
