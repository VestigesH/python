#判断某年是否为闰年
def leapYear(y):
    if y<1:
        y=1
    if y%400==0 or y%4==0 and y%100!=0:
        lp=1
    else:
        lp=0
    return lp


#计算y年m月的天数
def getLastDay(y,m):
    if y<1:
        y=1
    if m<1:
        m=1
    if m>12:
        m=12
    #每个月的正常天数
    #月份      1  2  3  4  5  6  7  8  9  10  11  12
    monthday=[31,28,31,30,31,30,31,31,30,31,30,31]
    r=monthday[m-1]
    if m==2:
        r=r+leapYear(y)#处理闰年的2月天数
    return r

#计算从公元1年1月1日到y年m月d日的天数(含两端的天数)
def calcDays(y,m,d):
    if y<1:
        y=1
    if m<1:
        m=1
    if m>12:
        m=12
    if d<1:
        d=1
    if d > getLastDay(y,m):
        d = getLastDay(y,m)
    T=0
    for i in range(1,y):
        T=T+365+leapYear(i)
    for i in range(1,m):
        T=T+getLastYear(y,i)
    T=T+d
    return T
y,m,d=eval(input("please input year,month,day:"))
days=calcDays(y,m,d)
print("从1年1月1日到",y,"年",m,"月",d,"日 共",days,"天")
            
