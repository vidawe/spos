list_1 = [100,50,70,120,35]
list_2 = [110,60,80,30]

for x in range(len(list_2)):
    y = list_2[x]
    a = []
    for z in range(len(list_1)):
        if y < list_1[z]:
            a.append(list_1[z])
            
