import random

while True:  # tahle smyčka opakuje celou hru
    print("Vítej ve hře: Hádej číslo 1–100! (napiš číslo, nebo q pro konec)")

    tajne = random.randint(1, 100)
    pokusy = 0

    while True:  # tahle smyčka je jedno kolo hádání
        tip_text = input("Tvůj tip: ")

        if tip_text.lower() == "q":
            print("Konec hry. Díky!")
            break

        try:
            tip = int(tip_text)
        except ValueError:
            print("Prosím napiš celé číslo (nebo q pro konec).")
            continue

        if not (1 <= tip <= 100):
            print("Tip musí být mezi 1 a 100.")
            continue

        pokusy += 1

        rozdil = abs(tip - tajne)
        if rozdil <= 5:
            print("Jsi blízko!")

        if tip < tajne:
            print("Moc nízko.")
        elif tip > tajne:
            print("Moc vysoko.")
        else:
            print(f"Trefa! Uhodl/a jsi na {pokusy}. pokus.")
            break  # konec vnitřní smyčky (hráč vyhrál)

    #  po skončení jednoho kola:
    odpoved = input("Chceš hrát znovu? (a/n): ")

    if odpoved.lower() != "a":
        print("Díky za hraní! Měj se!")
        break  # konec celé hry
