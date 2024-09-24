Anna = int(input("Anna hoeveel boterhamen heb jij gegeten?\n"))
Bob = int(input("Bob hoeveel boterhamen heb jij gegeten?\n"))
Mark = int(input("Mark hoeveel boterhamen heb jij gegeten?\n"))

totaal = Anna + Bob + Mark

gem = round(totaal / 3)

if totaal > 0:
    print(f"Er wordt gemiddeld {gem} boterhamen gegeten. In totaal zijn dit {totaal} stuks. Anna heeft {Anna} gehad, Bob {Bob} en Mark {Mark} stuks")
else:
    print("Er worden geen boterhamen gegeten")