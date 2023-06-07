inp = input()
for x in range(0,len(inp)):
    ah = inp.find("h")
    ae= inp.find("e",ah+1)
    al1 = inp.find("l",ae+1)
    al2 = inp.find("l",al1+1)
    ao = inp.find("o",al2+1)
if ah <  ae <  al1 < al2  < ao :
    print("YES")
else:
    print("NO")



    
