import csv
from statistics import mean

def calculate_three_best():
  
    with open('E:\moadel.csv') as f2:
        reader = csv.reader(f2)
        Lname=''
        Lmean=''
        c=0
        for row in reader:
            c=c+1        
            name=row[0]
            these_grades=list()
            for grade in row[1:]:
                these_grades.append(float(grade)) 
            Lname=Lname+name+' '
            Lmean=Lmean+str(mean(these_grades))+' '
    
        Lname=Lname.split()
        Lmean=Lmean.split()

        for i in range(0,c-1):
            for j in range(i+1,c):
                if float(Lmean[i])<float(Lmean[j]):
                    temp1=Lmean[i]
                    Lmean[i]=Lmean[j]
                    Lmean[j]=temp1
                    temp2=Lname[i]
                    Lname[i]=Lname[j]
                    Lname[j]=temp2

        for i in range(0,2):
            if float(Lmean[i])==float(Lmean[i+1]) and (Lname[i])>(Lname[i+1]):
                temp2=Lname[i]
                Lname[i]=Lname[i+1]
                Lname[i+1]=temp2         

        L_results=''
        for i in range(0,3):
            L_results=L_results+str(Lname[i])+','+str(Lmean[i])+'\n'
        L_results=L_results.split() 
     

    with open('E:\moadell.csv', 'a',newline='') as f3:
        writer = csv.writer(f3)    
        for row in L_results: 
            columns = [c.strip() for c in row.strip(', ').split(',')]
            writer.writerow(columns) 
  
    f2.close() 
    f3.close()   

calculate_three_best() 
