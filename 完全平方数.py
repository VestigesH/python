

for i in range(1,1001):
    a=int((100+i)**0.5)
    b=int((168+i)**0.5)
    if a*a==100+i and b*b==168+i:
        print(i)
