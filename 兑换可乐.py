n=int(input("请输入最初的可乐数量:" ))
k=int(input("请输入兑换一瓶可乐所需的瓶盖数" ))
cap=0
drink=0
while n>0:
    drink+=1
    cap+=1
    n-=1
    if cap == k:
        n+=1
        cap = 0
if cap+1==k:
    print(drink+1)
else:
    print(drink)
