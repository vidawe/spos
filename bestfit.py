print("Best Fit")

nm = int(input("Enter no of mem blocks available:"))

list_1 = []
for x in range(nm):
    a = int(input("Enter the memory segment"+str(x)+":"))
    list_1.append(a)

list_2 = []
np = int(input("Enter number of processes:"))
for i in range(np):
    b = int(input("Enter the process size P"+str(i)+":"))
    list_2.append(b)


alloc = []
for x in range(len(list_2)):
    y = list_2[x]
    a = []
    for z in range(len(list_1)):
        if y < list_1[z]:
            #print("small")
            a.append(list_1[z])
        else:
            print(" ")
    
    
    a.sort()
    #print(a)
    if a[0] not in alloc:
        alloc.append(a[0])

print("Process Size:    Alloted Memory Size:")