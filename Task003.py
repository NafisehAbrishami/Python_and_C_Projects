import csv
from collections import OrderedDict
from statistics import mean
def calculate_three_best():
    f5 = open ('E:\moadel.csv')
    reader = csv.reader(f5)
    Lname = ''
    Lmean = ''
    for row in reader:
        name = row[0]
        these_grade= list()
        for grade in row[1:]:
            these_grade.append(float(grade))
        Lname = Lname + name+' '
        Lmean = Lmean + str(mean(these_grade))+' '
    Lnames = Lname.split()
    Lmeans = Lmean.split()
    tup = list(zip(Lnames,Lmeans))
    od1 = OrderedDict(tup)
    sorted_d1 = sorted(od1.items(),key=lambda x: x[1],reverse=True) 
    ex = []
    ex.extend(sorted_d1[0:3])
    d2_ex = OrderedDict(ex)
    sorted_d2_ex = sorted(d2_ex.items(),key=lambda x: x[0])
    d3_ex = OrderedDict(sorted_d2_ex)
    sorted_d3_ex = sorted(d3_ex.items(),key=lambda x: x[1],reverse=True)
       
    f6 = open('E:\moadeel.csv','a',newline='')
    writer = csv.writer(f6)
    for row in sorted_d3_ex :
        writer.writerow(row)
    f5.close()
    f6.close()
calculate_three_best()



    




