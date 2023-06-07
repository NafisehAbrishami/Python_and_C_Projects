import csv
from statistics import mean

def calculate_averages():
    f1 = open('E:\moadel.csv')
    reader = csv.reader(f1)
    for row in reader:
        name = row[0]
        grd = list()
        for grade in row[1:]:
            grd.append(float(grade))
        f2 = open('E:\moadella.csv','a',newline='')
        writer = csv.writer(f2)
        tuple1 =  (name,mean(grd))
        writer.writerow(tuple1) 
    f1.close()
    f2.close()
    
calculate_averages()

        