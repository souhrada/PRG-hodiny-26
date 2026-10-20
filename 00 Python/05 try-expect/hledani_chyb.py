# try:
#     uzivInput = int(input("Zadej číslo: "))
#     if uzivInput > 100:
#         print("Uživatel zadal velké číslo")
# except ValueError:
#     print("Nezadal jsi číslo")



predmety =  ["wet, prg, oss"]

try:
    print(predmety[4])
except IndexError:
    print("Neexistující index!!!")



# Vlastní error

def zkontroluj_vek(vek):
    if vek > 18:
        print("Můžeš zakoupit alkohol ale nedělej to není z toho dobře")
    if vek < 0:
        raise ValueError("Věk nemůže být záporný")

try: 
    zkontroluj_vek(5)
except ValueError:
    print("Zadal jsi neplatný věk")