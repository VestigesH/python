n=eval(input("请输入位数: "))

for i in range(pow(10,n-1),pow(10,n)): 

    

    for j in str(i): 

         num += int(pow(int(j), n)) 

    if i == num: 

        print(i)
