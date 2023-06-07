inp = input()
for x in inp:
    a = inp.find("A")
    b = inp.find("B",a+1)
    c = inp.find("B",a+2)
    d = inp.find("A",a+3)
    e = inp.find('B')
    f = inp.find('A',e+1)
    g = inp.find('A',e+2)
    h = inp.find('B',e+3)

if b == c and a < b and c > d:
    print('YES')
    
elif b != c and a < b and c < d:
    print('YES')
    
elif f == g and e < f and g > h:
    print('YES')
elif f != g and e < f and g < h:
    print('YES')
else:
    print("NO")
    
    



      