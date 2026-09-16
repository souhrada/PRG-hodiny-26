def counter(n):
    for x in range(1, n+1):
        if x == 13:
            continue
        print(x)

# alternativně

def counterv2(n):
    for x in range(1, n+1):
        if x != 13:
            print(x)

counterv2(15)


def zigzag(n):
    for x in range(1, n+1):
        if x%2 == 0: # x%2 má zbytek 0, tzn. je sudé číslo
            print(f"    {x}")
        else:
            print(x)

zigzag(10)