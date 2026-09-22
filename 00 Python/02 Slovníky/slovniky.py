# dictionary (slovník) je soubor zprárovaných klíčů a hodnot (key - value)
# levá strana = key, pravá strana = value

telefonni_seznam = {
    "Kvído": "777 666 555",
    "Anděla": "723 123 456",
    "Emil": "735 321 123"
}

print(telefonni_seznam["Anděla"])

cat = {
    "name": "Beruška",
    "age": 20,
    "color": "orange",
    "alive": True,
    "favorite_food": ["fish", "lasagne", "meat"]
}


print(cat)
print(cat["color"])
print(cat["favorite_food"][1])

# vypsat všechny keys
for klic in cat:
    print(klic)


# alternativní způsob jak vypsat keys
for klic in cat.keys():
    print(klic) 

# vypsat všechny values
for klic in cat:
    print(cat[klic])

# alternativní způsob, jak vypsat values
for hodnota in cat.values():
    print(hodnota)


# výběr jak keys, tak values
for klic, hodnota in cat.items():
    print(f"Key {klic}, value {hodnota}")


for food in cat["favorite_food"]:
    print(food)

# přidání nového páru key-value do dictionary
cat["eye_color"] = "green"

print(cat)

# přepsání value v dictionary
cat["age"] = 21