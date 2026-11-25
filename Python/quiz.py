play=input("hello and wellcome to my quiz, do you want to play? y")
if play != "y":
    print("sad to see you go, hope you try again")
    quit()
else:
    print("sweet, let's go!")
scor=0
answer=input("what is Joshua's favorit kind of music?")
if answer == "heavy mettel":
    print("correct, good job")
    scor+=1
else:
    print("wrong answer")
answer=input("what is Joshua's favorit sport?")
if answer == "skiing":
    print("correct, good job")
    scor+=1
else:
    print("wrong answer")
answer=input("what musical instrement does Joshua play?")
if answer == "drums":
    print("correct, good job")
    scor+=1
else:
    print("wrong answer")
answer=input("what instrement did joshua play before he played the drums?")
if answer == "trombone":
    print("correct, good job")
    scor+=1
else:
    print("wrong answer")
answer=input("what heavy mettel consert did Joshua go to in november of 2022?")
if answer == "slipknot":
    print("correct")
    scor+=1
else:
    print("wrong answer")
print(f"you got {scor} questions correct, good job")