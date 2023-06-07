string = "salam. Jadi is here and testing python for fun"

counter = dict()
for letter in string:
#if letter in counter:
    counter[letter] = counter.get(letter,0)+ 1
# counter[letter] += 1
# #else:
#counter[letter]= 1

for x in list(counter.keys()):
    print("%s appeared %s times" % (x,counter[x]))
   