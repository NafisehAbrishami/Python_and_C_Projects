import csv
from collections import OrderedDict
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    f1 = open(input_file_name)
    reader = csv.reader(f1)
    for row in reader:
        name = row[0]
        grd = list()
        for grade in row[1:]:
            grd.append(float(grade))
        f2 = open(output_file_name,'a',newline='')
        writer = csv.writer(f2)
        tuple1 =  (name,mean(grd))
        writer.writerow(tuple1) 
    f1.close()
    f2.close()

def calculate_sorted_averages(input_file_name, output_file_name):
    f3 = open(input_file_name)
    reader = csv.reader(f3)
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
    f4 = open(output_file_name,'a',newline='')
    writer = csv.writer(f4)
    for i in sorted_d:
        writer.writerow(i)
    f3.close()
    f4.close()

def calculate_three_best(input_file_name, output_file_name):
    f5 = open (input_file_name)
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
    f6 = open(output_file_name,'a',newline='')
    writer = csv.writer(f6)
    for row in sorted_d3_ex :
        writer.writerow(row)
    f5.close()
    f6.close()

def calculate_three_worst(input_file_name, output_file_name):
    f7=open(input_file_name)
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
    f8 = open(output_file_name,'a',newline='')
    writer = csv.writer(f8)
    for row in ex :
        writer.writerow(row[1:])
    f7.close()
    f8.close()

def calculate_average_of_averages(input_file_name, output_file_name):
    f9 = open(input_file_name)
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
    dval_mean =str(mean(float_d_val))
    f10 = open(output_file_name,'a',newline='')
    writer = csv.writer(f10)
    writer.writerow([dval_mean])
    f9.close()
    f10.close()
