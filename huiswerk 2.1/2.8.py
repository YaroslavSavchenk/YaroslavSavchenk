# Vragen aan de gebruiker
vraag1 = input("Regent het? (ja/nee)\n")
vraag2 = input("Mag ik met iemand meerijden? (ja/nee)\n")

# Variabelen instellen op basis van de antwoorden
regen = False  # Standaardwaarde
meerijden = False  # Standaardwaarde

if vraag1.lower() == "ja":  # Gebruik lowercase om invoer te standaardiseren
    regen = True
else:
    regen = False

if vraag2.lower() == "ja":
    meerijden = True
else:
    meerijden = False

# Beslissing maken op basis van de variabelen
if regen == False:
    print("Ik ga met de fiets")
elif regen == True:
    if meerijden == True:
        print("Ik mag met iemand meerijden")
    else:
        print("Ik moet met de bus gaan")