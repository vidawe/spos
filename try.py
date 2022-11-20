file = open("st.txt", "r")
#print (file.read())
with open('st.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
li = [x.strip() for x in content]
print(li)


sym = []
for string in li:
    if string[0] != "-":
        a = string[0]+string[1]
        sym.append(a)
        #print(arr)
    else:
        print()
print(sym)

for string in li:
    for i in range(len(string)):
        if string[i] == "=":

            print(string[i]+string[i+1]+string[i+2]+string[i+3])

asmdir = {"START":"01","END":"02","ORIGIN":"03","EQU":"04","LTORG":"05","TRANSL":"07"}
dclst = {"DC":"01","DS":"02"}
impst = {"STOP":"01","ADD":"02","SUB":"03","MULT":"04","MOVER":"05","MOVEM":"06","COMP":"07","BC":"08","DIV":"09","READ":"10","PRINT":"11"}

#for string in li:
#    for i in range(2,7):
 #       print(string[i],end=" ")

arr = []
a = li[0]
arr = a.split()
print(arr[1])
#f = arr[1]

if arr[1] in asmdir :
    print("(AD,"+asmdir[arr[1]]+")")
elif arr[1] in dclst:
    print("(DL,"+dclst[arr[1]]+")")
elif arr[1] in impst:
    print("(IS,"+impst[arr[1]]+")")
    
file.close()
