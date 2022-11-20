list_1 = [100,50,70,120,35]
list_2 = [110,60,80,30]

alloc = []
for x in range(len(list_2)):
    y = list_2[x]
    a = []
    for z in range(len(list_1)):
        if y < list_1[z]:
            a.append(list_1[z])
        else:
            print(" ")
    print("----------")
    
    a.sort()
    print(a)
    if a[0] not in alloc:
        alloc.append(a[0])

print("Process Size:    Alloted Memory Size:")
for s in range(len(list_2)):
    print(list_2[s], end=" ")        