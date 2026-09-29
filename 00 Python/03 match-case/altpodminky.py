uziv_input = input("Stiskni nějakou klávesu")


if uziv_input.lower() == "a":
    print("Uživatel napsal a")
elif uziv_input.lower() == "b":
    print("Uživatel napsal b")
elif uziv_input.lower() == "c":
    print("Uživatel napsal c")
elif uziv_input.lower() == "d":
    print("Uživatel napsal d")
elif uziv_input.lower() == "e":
    print("Uživatel napsal e")
else:
    print("Žádná z možností")


match uziv_input.lower():
    case "a":
        print("Uživatel napsal a")
    case "b":
        print("Uživatel napsal b")
    case "c":
        print("Uživatel napsal c")
    case "d":
        print("Uživatel napsal d")
    case _: # tohle je else
        print("Žádná z možností")