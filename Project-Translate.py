k = []
v = []
my_dict = dict()
#ap = []
inp =int(input())
count = 0
while count < inp:
    inp2 = input()
    sp1 = inp2.split()
    list_key = sp1[0].split()
    list_value = sp1[1].split()
    k.extend(list_key)
    v.extend(list_value)
    my_dict = dict(zip(k,v))
    count = count + 1
ap =[]
se = input()
se1 = se.split()
for key in se1:
    if key in my_dict:
        ap.append(my_dict[key])
    elif key not in my_dict:
        ap.append(key)              
print(' '.join(ap))
 
