num=eval(input('请输入一个数字'))
if num==1:
          print('这不是一个素数')
elif num==2:
          print('这是一个素数')
else:
     i=2
   while i<=num:
    if num %i==0:
          print('这不是一个素数')
          break
          i=3
    else:
          print('这是一个素数')
          break
