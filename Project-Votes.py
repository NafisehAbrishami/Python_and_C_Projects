
country = dict()
ex = []
cnum = int(input())
count = 0
while count < cnum :
    namec = input()
    sp = namec.split()
    ex.extend(sp)
    ex.sort()
    count = count + 1
for cv in ex :
    country[cv]=country.get(cv,0) + 1
for cv in list(country.keys()):
    print(cv,"",country[cv])

