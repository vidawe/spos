print("FCFS")

d = dict()

#num = int(input("Enter number of processes: "))
#for i in range(num):
   # key = "P"+str(i+1)
   # a = int(input("Enter Arrival Time "+str(i+1)+":"))
   # b = int(input("Enter Burst Time "+str(i+1)+":"))
   # x = []
   # x.append(a)
  #  x.append(b)
 #   d[key] = x

#ss = sorted(d.items(), key=lambda item: item[1][0])

# AT BT
ss = [('P1', [0, 4]), ('P2', [1, 3]), ('P3', [2, 1]), ('P4', [3, 2]),  ('P4', [4, 5])]
print(ss)   

c = 0
ct = []
for i in range(5):
    c = c + ss[i][1][1]
    ct.append(c)
   

print(ct)










