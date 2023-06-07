import random
adade_aval = 1
adade_dovom = 99
guess = random.randint(adade_aval,adade_dovom)
print(guess)
my_answer = input()
while my_answer != "d" :
    if my_answer == "k":
        adade_dovom = (guess - 1)
    elif my_answer == "b":
        adade_aval = (guess + 1)
    else :
        break
    guess = random.randint(adade_aval,adade_dovom)
    print(guess)
    my_answer = input()

print("you win!!!!")



    
    
    







    
    

     




   

