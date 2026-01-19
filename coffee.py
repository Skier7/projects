menu={"black": 10, "donut": 2, "icecream": 1, "hot chocolate": 1}
total=0
name=input("what is your name?")
if name == "kile" or name == "izzy" or name == "ben":
    good_deeds=int(input("how many good deeds have you done today?"))
    if good_deeds<5:
        print(" you haven't done enough good deeds, get the fuck out of here right fucking now!")
        quit()
    else:
        print("you are vary good, come in")
while True:
    order=input("welcome to my coffee shop, what do you want? we have black, donut, icecreem, and hot chocolate, when you are finnished, type done")
    if order == "done":
        print(f"your order will be ready soon, your total is ${total}")
        quit()
    if order in menu:
        quantity=int(input("how many would you like?"))
        total+=menu[order]*quantity
    else:
        print("we don't have that, please try again")