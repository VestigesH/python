for n in range(3,8):
    for i in range(int(pow(10,n-1)),int(pow(10,n))): 

        num = 0 

        for j in str(i): 

            num += int(pow(int(j), n)) 

        if i == num: 

           1 print(i)
