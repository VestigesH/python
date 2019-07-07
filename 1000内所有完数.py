m=1000
for a in range (1,m+1):
    s=0
    list=[]
    for i in range (1,a):
        if a%i ==0:
            s+=i
            list.append(i)
            if s==a:
                print("%d it's factors are: "%a,list)
                
