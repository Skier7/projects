name=input("enter your name")
while name == ""or name ==" ":
    print("pleas enter a name to continue")
    name=input("enter your name")    
print(f"hello {name}")
while True:
    color=input("what color is best? green, red, orenge, pink or gray, q to quit")
    if color == "q":
        print("peace")
        quit()  
    elif color == "green":
        print("you made the right choice")
    elif color == "red":
        print("this is also a good choice")
    elif color == "orenge":
        print("this is the best!")
    elif color == "pink":
        reason=input("why do you like pink so much?")
        while reason == "because i do"or reason == "it's the best":
            print("wrong answer!")
            print("you are rong and that's ok, one day you will see the error of your ways")
            break
    elif color == "gray":
        print("you are boring!")
    else:
        print("not a valid option, try again")