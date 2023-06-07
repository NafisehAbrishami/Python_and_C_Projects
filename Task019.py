ap = []
inp1 = int(input())
inp2 = input()
inp2_1 = inp2.split()
inp2_2 = [int(x) for x in inp2_1]
for x in inp2_2:
    if x <= 2:
        ap.append(x) 
        l = len(ap) // 3
print(l)

