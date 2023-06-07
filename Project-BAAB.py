
a = 0
b = 0
aa = 0
bb = 0
inp = input()
for x in range(0,len(inp)):
    a = inp.find("A")   
    b = inp.find("B",a+1)
    aa = inp.find("B",a+3)
    bb = inp.find("A",a+4)
    c = inp.find("B")
    d = inp.find("A",c+1)
    cc = inp.find("A",+3)
    dd = inp.find("B",c+4)
if a < bb > b < aa :
    print("YES")
elif x == (c , d , cc , dd)  :
    print("YES")
else:
    print("NO")

    #print("YES")


    #print("YES")
#else:
    
    #3rint("NO")


        
        
