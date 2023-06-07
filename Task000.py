import csv
import operator
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
    d = dict(zip(Lnames,Lmeans))
    sorted_d = sorted(d.items(),key=lambda x: x[1])
    f2 = open('E:\moadell.csv','a',newline='')
    writer = csv.writer(f2)
    for row in sorted_d:
        writer.writerow(row)
    f1.close()
    f2.close()
calculate_sorted_averages()

    
