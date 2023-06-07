a_list = [1,2,3]
b_list = [2,1,4]
count = 0
count1 = 0
for a , b in zip(a_list,b_list):
    if a < b :
        count += 1
    if b < a :
        count1 += 1


print(count,count1)
