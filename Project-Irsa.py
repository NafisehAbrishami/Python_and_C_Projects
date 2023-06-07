qeymat = []
keyfiat = []
inp1 = int(input())
count = 0
while count < inp1:
    inp2 = input()
    inp3 = inp2.split()  
    inp4 = [int(x) for x in inp3]
    qeymat.append(inp4[0])
    keyfiat.append(inp4[1])
    count = count + 1
hap = 0
for qey,key in zip(qeymat,keyfiat):
    for qey2,key2 in zip(qeymat,keyfiat):
        if qey > qey2 and key < key2:
            hap = hap + 1
while hap >= 1:
    print('happy irsa')
    break
else:
    print('poor irsa')
    
    
    



            
        
             
            
    


            

    
    






    
   

    


    

    
    

#print(p, count)

