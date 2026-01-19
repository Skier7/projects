#this is a dicshinary
prices={"s": 1000, "b": 250, "h": 500, "g": 10, "p": 400}
total=0
while True:
    options=input("wellcome to my ski shop, what do you want? s for a pair of skis, b for a pair of boots, h for helmit, g for gluvs, p for poles and done to finish")
    if options == "done":
        print(f"thankyou for shopping, your total is ${total}")
        quit()
    if options in prices:
        q=int(input("how many would you like?"))
        total+=prices[options]*q
    else:
        print("sorry but we don't have that, try again")