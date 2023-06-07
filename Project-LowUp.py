up = 0
low = 0
inp = input()
for x in inp:
    if x == x.upper():
        up = up + 1
    if x == x.lower():
        low = low + 1
if up > low :
    inp1 = inp.upper()
    print(inp1)
else:
    inp2 = inp.lower()
    print(inp2)