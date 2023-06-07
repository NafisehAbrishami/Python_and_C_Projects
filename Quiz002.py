import random
answer = random.randint(1,50)
name = str(input("what is your name?"))
print("this is a game !", name , "Are you ready? ") 
guess = int(input("what is your guess? "))

while guess != answer:
    if guess > answer:
        print("mine is smaller!")
    else:
         print("mine is greater!")
    guess = int(input("what is your guess? "))



print(name,"you did it!wooow")

   
