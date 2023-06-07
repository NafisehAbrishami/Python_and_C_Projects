ap =[]
inp1 = int(input())
count = 0
while count < inp1:
    inp2 = float(input()) 
    import math
    jazr = math.sqrt(inp2)
    ap.append('{0:2.15f}' .format(jazr))
    count = count +1 
for num in ap:
    str_jazr = [str(x) for x in ap]
    print(num[:-11])



