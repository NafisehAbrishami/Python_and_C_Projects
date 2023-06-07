score = 0
bord = 0
adade_aval = 1
adade_dovom = 31
emtiaz = int(input())
for i in range(adade_aval,adade_dovom):
    if emtiaz == 3 :
        score = score + 3
        bord = bord + 1
    elif emtiaz == 1 :
        score = score + 1
        bord = bord + 0
    else:
        score = score + 0
        bord = bord + 0
    if i == 30 :
        break
    emtiaz = int(input())

print(score," ", bord)



