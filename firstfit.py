print("First Fit")

numm = int(input("Enter no of mem blocks available:"))

m = []
for x in range(numm):
    a = int(input("Enter the memory segment"+str(x)+":"))
    m.append(a)

p = []
nump = int(input("Enter number of processes:"))
for i in range(nump):
    b = int(input("Enter the process size P:"+str(i)+":"))
    p.append(b)

alloc = [-1] * nump
occupied = [False] * numm

for z in range(0,nump):
    for y in range(0,numm):
        if not occupied[y] and p[z] <= m[y]:
                alloc[z] = y
                occupied[y]=True
                break

print("Process No:     Size of block:    Allocated Segment:")
for i in range(nump):
    print(str(i+1)+"\t\t"+str(p[i])+"\t\t", end=" ")

    if alloc[i] != -1:
        print(alloc[i]+1)
    else:
        print("Not allocated")
                

