np = int(input("Enter no. of processes: "))
s = []

#for i in range(np):
 #   temp = []
    
  #  bt = int(input("Enter BT of P"+str(i)+": "))
   # p = int(input("Enter Priority of P"+str(i)+": "))
    #temp.append(at)
    #temp.append(bt)
    #s.append(temp)
s = [[1, 3], [2, 8], [3, 6], [4, 4], [5, 2]]

b = []
for x in range(np):
    t = s[x][1]
    b.append(t)
print(b)

c = []
s = 0

for i in range(np):

    s = s + b[i]
    c.append(s)
print(c)

wt = []
w = 0

for i in range(np):
    w = c[i] - b[i]
    wt.append(w)
print(wt)



