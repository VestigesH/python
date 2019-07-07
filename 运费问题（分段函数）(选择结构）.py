s=eval(input("请输入路程:"))
if s<250:
    fee=s
if 250<=s<500:
    fee=0.98*s 
if 500<=s<1000:
    fee=0.95*s
if 1000<=s<2000:
    fee=0.92*s
if 2000<=s<3000:
    fee=0.9*s
if s>=3000:
    fee=0.85*s
print("运费是: %.4f"%fee)
