print("Jsem velký programátor")

jmeno = "Jarmil"
cislo = 42
nadseni = True

# print(jmeno)


# def pozdrav(jmeno1, jmeno2):
#     print("Ahoj!", jmeno1)
#     print("Hi!", jmeno2)


# pozdrav("Kvído", "Anděla")
# pozdrav("Emil", "Fridolín")


# uzivateluv_input = input("Sem něco napiš")

# print(uzivateluv_input)


# zadane_km = int(input("Zadej počet km pro převod: "))


def prevod(km):
    mile = km * 0.62
    return mile

# vysledek = prevod(zadane_km)

# print(f"Výsledek převodu je, že {zadane_km} km je {vysledek} mil.")


if cislo == 42:
    print("Číslo je 42")
elif cislo > 42:
    print("Číslo je větší než 42")
else:
    print("Číslo je menší než 42")



seznam_mest = ["Praha", "Brno", "Zdiby", "Ostrava"]

print(seznam_mest[1])

for mesto in seznam_mest:
    print(mesto)


for x in range(1, 11):
    print(x)

for y in range(6):
    print(y)

# range(od kolika, do kolika, po kolika)
for z in range(10, 0, -1):
    print(z)


pocitadlo = 1
while pocitadlo < 4:
    print(pocitadlo)
    pocitadlo += 1 # pocitadlo = pocitadlo + 1; python neumi pocitadlo++
