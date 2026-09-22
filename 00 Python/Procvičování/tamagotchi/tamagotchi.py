surikata = {
    "jméno": "Evžen",
    "čistota": 20,
    "hlad": 0,
    "žízeň": 10,
    "životy": 100,
    "energie": 100,
    "žije": True,
    "nemoc": False,
    "Radost": True,
}


def krmeni():
    surikata["hlad"] -= 20
    print(f"Surikata se napapala")
    print(f"Hlad je {surikata["hlad"]}")


def main():
    print("Vítej!")
    print(f"Zdraví tě {surikata['jméno']}")
    print("""

        /-;
        } (
         \/
        ) / 
     __/ [[
    
    """)


    while True:
        print(f"Pro krmení stiskni k, pro ukončení napiš konec")    

        uziv_inp = input()

        if uziv_inp.lower() == "konec":
            print("Ukončení hry... bye!")
            break
        elif uziv_inp.lower() == "k":
            krmeni()





main()