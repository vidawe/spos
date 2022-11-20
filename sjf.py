np = int(input("Enter no. of processes: "))
s = []

#for i in range(np):
 #   temp = []
    
  #  at = int(input("Enter AT of P"+str(i)+": "))
   # bt = int(input("Enter BT of P"+str(i)+": "))
    #temp.append(at)
    #temp.append(bt)
    #s.append(temp)


s = [[0, 3, 4], [1, 8, 3], [2, 6, 1], [4, 4, 5], [5, 2, 2]]

s.sort()

b = []
for x in range(len(s)):
    t = s[x][1]
    b.append(t)
print(b)
a = []
for x in range(len(s)):
    t = s[x][0]
    a.append(t)
print(a)
#AT   BT  ID
#[0, 1, 2, 4, 5]
#[3, 8, 6, 4, 2]
#[4, 3, 1, 5, 2]

k = []
for i in range(len(s)):
    k.append(i+1)
print(k)
    
tot = sum(b)
print(tot)
c = 0

f = []
for i in range(0,23):
    if c == b[i]:
        f.append(b[i])
        b[i] = b[i] - 1
        f.append(b[i])
        c += 1
    

    










