number = int(input())
count = 0
for i in range(1,number):
    if (number % i == 0):
        count+= 1
if (count == 1):
    print("prime")
else:
    print("not prime")
    


    



    




