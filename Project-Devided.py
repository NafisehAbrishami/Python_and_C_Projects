l1 = []
l2 = []
l3 = []
list_inp = []
c1 = 0
for i in range(1,21):
    inp = int(input())
    list_inp.append(inp)
    list_inp.sort()
    list_inp2 = list_inp
    c1 += 1
c2= 0
for i in list_inp:
    c2 = 0
    for j in range(1,i+1):
        if i % j == 0:
            c2 += 1
    l1.append(c2)
    l1.sort()
for i in l1:
    if l1[-1] == l1[-2]:
        a = l1.pop(-1)
        b = l1.pop(-1)
        l2.extend([a,b])
        if l1[-1] == a:
            e = l1.pop(-1)
            l2.append(e)
    else :  
        aa = l1[-1]
        l2.append(aa)      
c4 = 0
for i in list_inp2:
    c4 = 0
    for j in range(1,i+1):
        if i % j == 0:
            c4 += 1
    if c4 == l2[0] :
        l3.append(j) 
print(max(l3),max(l2))


    


   








