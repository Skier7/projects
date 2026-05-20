menu={"black": 10, "donut": 2, "icecreem": 1, "hot chocklit": 1}
total=0
name=input("what is your name?")
if name == "kile" or name == "izzy":
    print("you are not wellcome hear, get out!!!!!!!!!!!!!!!!!!!!")
    quit()
while True:
    order=input("welcom to my coffee shop, what do you want? we have black, donut, icecreem, and hot chocklit, when you are finnished, type done")
    if order == "done":
        print(f"your order will be ready soon, your total is ${total}")
        quit()
    if order in menu:
        quantity=int(input("how many would you like?"))
        total+=menu[order]*quantity
    else:
        print("we don't have that, try again")