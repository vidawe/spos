np = int(input("Enter no. of processes: "))
s = []

#for i in range(np):
 #   temp = []
    
  #  bt = int(input("Enter BT of P"+str(i)+": "))
   # p = int(input("Enter Priority of P"+str(i)+": "))
    #temp.append(at)
    #temp.append(bt)
    #s.append(temp)
q = 2
bt = [[5], [4], [2], [1]]
temp = []

for i in range(4):
    t = bt[i][0]
    n = t - 2
    temp.append(n)
print(temp)