count=0
n=int()
x=int()
y=int()
z=int()
def hanoi(n,x,y,z):
    global count
if n==1:
    count+=1
    move(count,x,z)
else:
    hanoi(n-1,x,z,y)
    count+=1
    move(count,x,z)
    hanoi(n-1,y,x,z)

def move(n,x,y):
    print("step %d:Move disk from %c to %c"%(count,x,y))
    m=int(input("input the number of disks:"))
    print("The steps to moving %d disks:"%m)
    hanoi(m,"A","B","C")
