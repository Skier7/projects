print("Hello, the commands are rules to live by")
Legion=["1. asume nothing", "2. how you do anything is how you do everything", "3. master your surroundings", "4. never make it persinal", "5. if you don't know what to do, do nothing", "6. question orders", "7. one mission at a time", "8. never kill a kid", "9. always play offence", "10. never let an innocent die"]
while True:
    cmd=input("choose a number between 1 and 10, all to list all commands or q to quit")
    if cmd == "1":
        print(Legion[0])
    elif cmd == "2":
        print(Legion[1])
    elif cmd == "3":
        print(Legion[2])
    elif cmd == "4":
        print(Legion[3])
    elif cmd == "5":
        print(Legion[4])
    elif cmd == "6":
        print(Legion[5])
    elif cmd == "7":
        print(Legion[6])
    elif cmd == "8":
        print(Legion[7])
    elif cmd == "9":
        print(Legion[8])
    elif cmd == "10":
        print(Legion[9])
    elif cmd == "all":
        print("all legion commands are," ,Legion)
    elif cmd == "Q" or cmd =="q":
        end=input("you are about to quit, are you sure? y/n")
        if end == "y":
            for x in range(5,0,-1):
                print(x)
            print("buy")
            quit()
        elif end == "no":
            print()
    else:
        print("not a valid option, pleas try again")