seznam = ["Ahoj", "Hi", "Bonjour"]

# "w" write --> přepíše celý soubor
# "a" append --> dopíše další řádky a ponechá původní
with open("ukazka.txt", "w", encoding="utf-8") as soubor:
    soubor.write("Guten tag!\n")
    soubor.write("Ciao\n")
    # soubor.writelines(seznam)
    for radek in seznam:
        soubor.write(radek + "\n")

# -- with open je zkrácený zápis pro
# soubor = open("ukazka.txt", "w", encoding="utf-8")
# soubor.write("Guten tag!")
# soubor.close()
# --> tento zápis nepoužíváme, používáme with open