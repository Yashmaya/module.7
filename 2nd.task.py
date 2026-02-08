name = set()
while True:
    user_input = input("please enter your name(press enter to quit):")
    if user_input == "":
        break
    elif user_input in name:
        print("existing name")

    else:
        print("new name")
        name.add(user_input)

print("list of names:")
for name in name:
    print(name)