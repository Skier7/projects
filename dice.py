import random
score=0
print("wellcome to the dice roling game, inorder to win you need to get a 1")
while True:
    dice=(random.randint(1,6))
    print(f"you roled a {dice}")
    score+=1
    if dice == 1:
        print("you win")
    elif dice == 2:
        print("so close, try again")
        score+=1
    again=input("would you like to role again? y/n")
    if again == "y":
        continue
    elif again == "n":
        print(f"thankyou for playing, your score is {score}, good buy")
        quit()
    else:
        print("not a valid option")