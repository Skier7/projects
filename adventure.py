name=input("Enter your name")
while name == "":
    print("Sorry but you didn't enter a name, you must enter a name to play")
    name=input("Enter your name")
print(f"Hello {name} and wellcome to this adventure game")
path=input("You are walking along a path, you come to the end, whitch way do you go? left/right")
if path == "left":
    bear=input("You meet a big bear, what would you like to do? fight/go back")
    if bear == "fight":
        print("You fight the bair, you try your best, but the bair wins and you die")
    elif bear == "go back":
        for x in range(5,-1,-1):
            print(x)
        print("You go back and you lose, better luck next time")
elif path == "right":
    house=input("You come to a big house, do you want to go in or stay outside, go in/stay")
    if house == "go in":
        IN=input("You are inside the house, you go down a dark hallway and come to the end, whitch way do you go, left/rightt?")
        if IN == "left":
            print(f"You come face to face with a monster and he eats you and you die, better luck next time {name}")
        if IN == "right":
            print(f"You turn right and meat a friendly dog, his name is Joey, you also find gold and win the game, good job {name}")
    elif house == "stay":
        car=input("You stay outside and look over and see a bright orange car, what do you do? get in/stay")
        if car == "get in":
            drive=input("You get in the car, turn the key and start driving, you come to a intersection, witch way do you go? left/right")
            if drive == "left":
                print("You turn left and crash, your car is on fire and you die")
            if drive == "right":
                print("You turn right and drive super fast into the night")
                popo=input("You continue speeding down the rode, the police see you and start chaceing you, what do you do, stop or keep going? stop/go")
                if popo == "stop":
                    print(f"You stop, the police get you and take you to jail")
                    jail=input("You are taken to jail, you get booked in and are sitting on the floor of a cold jail cell, you start looking around, you find a hole in the wall, you want to try to crall through it but it isn't vary big, what do you do, crall/stay")
                    if jail == "crall":
                        print("You crall into the hole, you go through a long tunnel and escape to freedom")
                    elif jail == "stay":
                        print("You stay and watch all the jail shenanigans")
                        FuckShitUp=input("You see a few guys fighting, going at it real hard, what do you do? join/stay")
                        if FuckShitUp == "join":
                            print(f"You join in, beeting people up, you beet everyone up and you are the only one in the jail, you turn it into a house for you and your frends, good job {name}")
                        elif FuckShitUp == "stay":
                            print("You stay and the dudes beet you up, you die")
                elif popo == "go":
                    run=input("You spead down the rode, you weve in and out of trafic but the police catch up to you, they order you out of the car, what do you do? get out/stay")
                    if run == "get out":
                        print("You get out of the car and walk backward to the police, they put you in handcufs, serch you and put you into there car, taking you to jail")
                    elif run == "stay":
                        print("You step on the gass and escape")
        if car == "stay":
            print("You stay and look at the bright orange car and you lose")