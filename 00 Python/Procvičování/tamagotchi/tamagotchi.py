import sys, json, os
from rich import print


default_surikata = {
    "jméno": "Evžen",
    "čistota": 80,
    "hlad": 50,
    "žízeň": 10,
    "životy": 100,
    "energie": 100,
    "žije": True,
    "nemoc": False,
    "radost": True,
}

def lek():
    if surikata["životy"] >= 100:
        print(f"{surikata["jméno"]} je zdravý a nepotřebuje léky")
    else:
        surikata["životy"] += 25
    surikata["nemoc"] = False

def hra():
    surikata["hlad"] += 15
    surikata["žízeň"] += 15
    surikata["energie"] -= 15
    surikata["radost"] = True
    print(f"{surikata["jméno"]} si hrál a má radost")

def spanek():
    surikata["energie"] = 100
    print(f"Zzz...")

def krmeni():
    surikata["hlad"] -= 20
    print(f"{surikata["jméno"]} se napapal")
    print(f"Hlad je {surikata["hlad"]}")

def zkontroluj_status():
    if surikata["hlad"] > 100 or surikata["hlad"] < 0:
        surikata["životy"] -= 10
    if surikata["žízeň"] > 100 or surikata["žízeň"] < 0: 
        surikata["životy"] -= 10
    if surikata["energie"] < 0:
        print(f"{surikata["jméno"]} chce spát!!!!")
    if surikata["energie"] > 100:
        print(f"{surikata["jméno"]} má ADHD")
    if surikata["radost"] == False:
        print(f"{surikata["jméno"]} je smutná")
        surikata["životy"] -= 5
    if surikata["čistota"] < 25:
        surikata["radost"] = False
        surikata["nemoc"] = True
    if surikata["nemoc"] == True:
        print(f"{surikata["jméno"]} je smutný")
        surikata["životy"] -= 10

    if surikata["životy"] < 0:
        surikata["žije"] = False

    if surikata["žije"] == False:
        print(f"{surikata["jméno"]} umřel... :(")
        sys.exit()

def vypis_status():
    print(f"""{surikata["jméno"]}:
        hlad: {surikata["hlad"]}
        žízeň: {surikata["žízeň"]}
        energie: {surikata["energie"]}
        životy: {surikata["životy"]}
        má radost: {surikata["radost"]}
    """)  


def save_game():
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(surikata, f, ensure_ascii=False, indent=4)


def load_game():
    global surikata

    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            surikata = json.load(f)
    else:
        surikata = default_surikata
        save_game()



def main():
    load_game()

    print("[green bold]Vítej![/green bold]")
    print(f"Zdraví tě {surikata['jméno']}")
    print("""[yellow bold]

        /-;
        } (
         \/
        ) / 
     __/ [[
    
    [/yellow bold]""")


    while True:

        print(f"""Menu:
        k: krmení
        h: hra
        s: spánek
        v: vypiš status
        konec: ukonči hru
        """)    

        uziv_inp = input()

        match uziv_inp.lower():
            case "konec":
                print("Ukončení hry... bye!")
                break
            case "k":
                krmeni()
            case "s":
                spanek()
            case "h":
                hra()
            case "v":
                vypis_status()
            case "save":
                save_game()
            case "l":
                lek()
            case _:
                print("[bold red]Neplatná klávesa[/bold red]")


        
        zkontroluj_status()
        save_game()



main()