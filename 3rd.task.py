airport_database = {}

while True:
    print("press 1 to add airport details :")
    print("press 2 to see airport details :")
    print("press 3 to exit")

    user_input = input(":")

    if user_input == "1":
        airport_name  = input("enter airport name:")
        ICOA_code = input("enter ICOA code:")
        airport_database[ICOA_code] = airport_name
        print("airport added")
    elif user_input == "2":
        ICOA_code = input("nter ICOA code:")
        print(f"Name of airport is {airport_database[ICOA_code]}")
    elif user_input == "3":
        break
