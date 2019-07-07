counter=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=k and j!=k and i!=j:
                counter=counter+1
                print(i,j,k)
print(counter) 
