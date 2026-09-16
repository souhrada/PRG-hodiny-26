jmena = [
    "Anna", "Jan", "Eliška", "Jakub", "Tereza", 
    "Tomáš", "Kryštof", "Adéla", "Lukáš", "Barbora", 
    "Matěj", "Karolína", "Filip", "Natálie", "Vojtěch", 
    "Viktorie", "Ondřej", "Kateřina", "David", "Simona"
]


print(jmena[2])
print(jmena[-1]) # -1 je poslední položka v seznamu
print(jmena[1:4]) # 1 až 4 (ne včetně) položka v seznamu
print(jmena[:11])
print(jmena[15:])

# append přidává položku do seznamu
jmena.append("Mojmír")
print(jmena)

# pro přepisování položky používáme =
jmena[3] = "Svatopluk"

jmena.insert(2, "Květoslava")


# pop odebírá položku na základě indexu a umožní nám ji uložit pod proměnnou
odebrana_hodnota = jmena.pop(5)

print(f"Ze seznamu jsem odebral {odebrana_hodnota}")


# remove odebírá na základě hodnoty
jmena.remove("Filip")


for i, jmeno in enumerate(jmena):
    print(f"{i+1}. {jmeno}")