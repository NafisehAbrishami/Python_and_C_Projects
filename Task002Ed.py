import csv
from collections import OrderedDict
from statistics import mean
def calculate_sorted_averages():
    f1 = open('E:\moadel.csv')
    reader = csv.reader(f1)
    Lname = ''
    Lmean =''
    for row in reader:
        name = row[0]
        these_grade = list()
        for grade in row[1:]:
            these_grade.append(float(grade))
        Lname = Lname+name+' '
        Lmean = Lmean + str(mean(these_grade))+' '
    Lnames = Lname.split()
    Lmeans = Lmean.split()
    tup = list(zip(Lnames,Lmeans))
    od = OrderedDict(tup)
    sorted_d = sorted(od.items(),key=lambda x: x[1])
    f2 = open('E:\moadell.csv','a',newline='')
    writer = csv.writer(f2)
    for i in sorted_d:
        writer.writerow(i)
    f1.close()
    f2.close()
calculate_sorted_averages()

    
