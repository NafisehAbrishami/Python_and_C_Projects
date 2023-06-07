import csv
from statistics import mean

def calculate_average_of_averages():
    f9 = open('E:\moadel.csv')
    reader = csv.reader(f9)
    Lname = ''
    Lmean = ''
    for row in reader:
        name = row[0]
        these_grade = list()
        for grade in row[1:]:
            these_grade.append(float(grade))
        Lname = Lname + name +' '
        Lmean = Lmean + str(mean(these_grade))+' '
    Lnames = Lname.split()
    Lmeans = Lmean.split()
    d = dict(zip(Lnames,Lmeans))
    d_val = d.values()
    float_d_val = [float(x)for x in d_val]
    dval_mean = str(mean(float_d_val))
    f10 = open('E:\moadeell.csv','a',newline='')
    writer = csv.writer(f10)
    writer.writerow([dval_mean])
    

    
    f9.close()
    f10.close()
calculate_average_of_averages()