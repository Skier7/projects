menu={"black": 10, "donut": 2, "ice cream": 1, "hot chocolate": 1}
total=0
name=input("What is your name?")
if name == "kile" or name == "izzy" or name == "ben":
    good_deeds=int(input("How many good deeds have you done today?"))
    if good_deeds<5:
        print(" You haven't done enough good deeds, get the fuck out!")
        quit()
    else:
        print("You are vary good, come in")
while True:
    order=input("Welcome to my coffee shop, what do you want? We have black, donut, ice cream, and hot chocolate, when you are finnished, type done")
    if order == "done":
        print(f"your order will be ready soon, your total is ${total}")
        quit()
    if order in menu:
        q=int(input("How many would you like?"))
        total+=menu[order]*q
    else:
        print("We don't have that, please try again")