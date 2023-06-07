rev = ""

inp = input()
for x in inp:
    inp1 = inp.lower()
    rev = x + rev
    rev1 = rev.lower()
if inp1 == rev1:
    print("palindrome")
else:
    print("not palindrome")
