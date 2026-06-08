Legion=["1. Assume nothing", "2. How you do anything is how you do everything", "3. Master your surroundings", "4. Never make it personal", "5. If you don't know what to do, do nothing", "6. Question orders", "7. One mission at a time", "8. Never kill a kid", "9. Always play offense", "10. Never let an innocent die", "11. Only do things with a point", "12. Use your resources"]
print("Hello, the commands are rules to live by")
while True:
    cmd=input("choose a number between 1 and 12, all to list all commands or q to quit")
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
    elif cmd == "11":
        print(Legion[10])
    elif cmd == "12":
        print(Legion[11])
    elif cmd == "all":
        print("all legion commands are," ,Legion)
    elif cmd == "Q" or cmd =="q":
        end=input("you are about to quit, are you sure? y/n")
        if end == "y":
            print("piece")
            quit()
        elif end == "no":
            print()
    else:
        print("not a valid option, pleas try again")