import csv
from collections import OrderedDict
from statistics import mean

def calculate_three_worst():
    f7=open('E:\moadel.csv')
    reader = csv.reader(f7)
    Lname =''
    Lmean = ''
    for row in reader:
        name = row[0]
        these_grade = list()
        for grade in row[1:]:
            these_grade.append(float(grade))
        Lname = Lname + name + ' '
        Lmean = Lmean + str(mean(these_grade)) + ' '
    Lnames = Lname.split()
    Lmeans = Lmean.split()
    tup = list(zip(Lnames,Lmeans))
    od = OrderedDict(tup)
    sorted_d = sorted(od.items(),key=lambda v: v[1])
    ex = []
    ex.extend(sorted_d[0:3])
    f8 = open('E:\moadellll.csv','a',newline='')
    writer = csv.writer(f8)
    for row in ex :
        writer.writerow(row[1:])
    f7.close()
    f8.close()
calculate_three_worst()