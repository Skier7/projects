name = input("enter your name: ").strip()
while not name:
    print("You didn't enter a name; please enter a name to continue.")
    name = input("enter your name: ")
print(f"hello {name}!")
age=int(input("enter your age"))
print(f"your age is {age}")
color = "green"
print(f"your favorite color is {color}")
sport = "skiing"
drink = "hot chocolate"
print(f"I love {sport} and I like to have {drink} when I come in for a warmup")