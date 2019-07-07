n,m=map(int,input().split)
if m<=4:
    pay=3*n
else:
    if m<=9:
        pay=4*n
    else:
        pay=5*n
print("应付款:",pay)
 
