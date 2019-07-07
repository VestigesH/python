year,month,day=eval(input("please input year,month,day:"))
days=0
if ((year%4==0 and year%100!=0) or (year%400==0)):#判断是否为闰年
    LY_dict={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    for m in range(1,month):
        days=days+int(day)+int(LY_dict[m-1])
        m=m-1
else:#平年
    P_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    for m in range(1,month):
        days=days+int(day)+int(P_dict[m-1])
        m=m-1
print("是第%d天"%days)
