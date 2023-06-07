 
vowels = ('a','i','e','u','o')
old_str = input()
new_str = ''
b = "." 
for letter in old_str.lower():
    if letter not in vowels:
        new_str += letter
print("."+b.join(new_str))
        
        





       