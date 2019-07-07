flag=True
i=2
num=int(input("please input a number"))
while i<=num-1:
    if num%i!=0:
        #print num,"is prime"
        flag=True
    else:
        #print num,"is not prime"
        flag=Flase
    i=i+1
if flag==True:
    print( num,"is  prime")
else:
    print( num,"is not prime")
            
