name_list = []
adade_aval = 1
adade_dovom = 11

inp = input()
for y in range (adade_aval,adade_dovom):
    new1 = inp.lower()
    new2 = new1[0].upper() + new1[1:]
    name_list.append(new2)
    if y == 10:
      break
    inp = input()
for x in range (0,len(name_list)):
    print(name_list[x])
    



  
