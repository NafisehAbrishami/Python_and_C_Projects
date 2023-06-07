import  csv
from statistics import mean

with open('E:\grade.csv') as f:
    reader = csv.reader(f)
    for i in reader:
        name = i[0]
        ap = []
        for x in i[1:]:
            ap.append(float(x))
        print  ("average nomaate %s barabar ast ba %5.2f " % (name, mean(ap)))    