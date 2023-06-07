import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    f1 = open(input_file_name)
    reader = csv.reader(f1)
    lname = ''
    lhash = ''
    for row in reader:
        name = row[0]       
        lname = lname + name + ' '
        lhash = lhash + str(row[1]) +' '
    lnames = lname.split()
    lhashs = lhash.split()
    d1 = list(zip(lnames,lhashs))
    od1 = OrderedDict(d1)
    p = ''
    h = ''
    for password in range(0,10000):
        p_str = str(password)
        hash_obj = hashlib.sha256(p_str.encode('utf-8')).hexdigest()  
        p = p + p_str + ' '
        h = h +str(hash_obj) + ' '
    psp = p.split()
    hsp = h.split()
    d2 = list(zip(psp,hsp))
    od2 = OrderedDict(d2)
    f2 = open(output_file_name,'a',newline='')
    writer = csv.writer(f2)
    for key1,val1 in zip(od1.keys(),od1.values()):
        for key2,val2 in zip(od2.keys(),od2.values()):
            if val1 == val2:
                writer.writerow([key1,key2])
    f1.close()
    f2.close()



















    #f2 = open('E:\word.csv','a',newline='')
