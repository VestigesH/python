s=str(input("please input a string : "))
len=len(s)
counter=0
for i in s.split(" "):
     if i:
         counter+=1
print("The length is:%.f"%len)
print("The counter is:%.f"%counter)
