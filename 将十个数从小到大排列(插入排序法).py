def insert_sort(array):
    for i in range (1,len(array)):
        if array[i-1]>array[i]:
            temp=array[i]
            index=i
            while index>0 and arrary[index-1]>temp:
                arrary[index]=arrary[index-1]

                index-=1
            arrary[index]=temp

b=str(input("请输入一组数据:"))
arrary=[]
for i in b.split(","):
    arrary.append(int(i))
print("排序前的数据:")
print(arrary)
insert_sort(arrary)
print("排序后的数据:")
print(arrary)
