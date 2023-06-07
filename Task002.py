import csv
import operator
from statistics import mean

#def calculate_sorted_averages():
f3 = open('E:\moadel.csv')
reader = csv.reader(f3)
for row in reader:
    name = row[0]
    grd = []
    ex = []
    for grade in row[1:]:
        grd.extend([name,mean(grade)])
    #ex.extend([name,mean(grd)])
        
    print(grd)
    #for key in ex : 
        #print(ex)
    

        #sort=sorted(d.items(), key =lambda ele: ele[1])
        #print(sort)
    #f3.close()
    #f4.close()

#calculate_sorted_averages()

    


        
        
        
    
    
    
    #print(sorted(MyDict.items(), key=lambda kv:kv[1]))
    
