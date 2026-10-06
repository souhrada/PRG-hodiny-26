with open("ukazka.txt", "r", encoding="utf-8") as soubor:
    # obsah = soubor.read() # přečte celý soubor
    radky = soubor.readlines() # pokud chci pracovat s jednotlivými řádky, použiju readlines()


# print(obsah)
print(radky)
print(radky[2].strip())