
ap = []
ap1 = []
ma = 0
ma1 = 0
inp = input()
for x in range(10,91):
    ap.append(inp)
    if inp == "-1" :
        break
    ap.append(inp)
    inp = input()
inp1 = [int(x) for x in ap]
inp1.sort()
ma=inp1.pop(-1)
ma1=inp1.pop(-2)
print(ma,"", ma1)
