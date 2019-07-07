L=[1,1]
while len(L)<10:
    L.append(L[-1]+L[-2])
print(L)
