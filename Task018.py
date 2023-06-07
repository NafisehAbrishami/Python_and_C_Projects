
inp = input()
inp2 = ''
inp3 = []

for x in inp:
    if x in "+":
       inp2 = inp.split(x)
    inp2 = list(inp2)
    inp2.sort()
    inp3= [str(x) for x in inp2]
    result= '+'.join(inp3)
print(result)


    
        
    
        

    

        
        

        
