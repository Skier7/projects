import random
print("you will be guessing a number in the next step. choose the number range you want")
lowest_num=int(input("enter the 1st number"))
highest_num=int(input("enter the 2nd number"))
answer=random.randint(lowest_num, highest_num)
guesses = 0
is_running = True
print(f"wellcome to the python umber guessing game\n please select a number between {lowest_num} and {highest_num}")
while is_running:
    guess = input("Enter your guess")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("out of range, please select a number within range, try again")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Good job, you got it in {guesses} guesses")
            is_running = False
    else:
        print("Invalid guess")