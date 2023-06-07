score = 0
bord = 0
count = 0
inp = int(input())
while count < 29 :
    if inp == 3:
        score = score + 3
        bord = bord + 1
    elif inp == 1:
        score = score + 1
        bord = bord + 0
    elif inp == 0 :
        score = score + 0
        bord = bord + 0
    count = count + 1
    inp = int(input())

print (score," ",bord)
print(count)