huidig_jaar = 2024
huidig_maand = 9  # Stel de huidige maand in
huidig_dag = 24   # Stel de huidige dag in

jaar = int(input("Wat is uw geboortejaar:\n"))
maand = int(input("In welke maand bent u geboren:\n"))
dag = int(input("Welke dag bent u geboren:\n"))

leeftijd = huidig_jaar - jaar

if huidig_maand < maand or (huidig_maand == maand and huidig_dag < dag):
    leeftijd -= 1

if 18 < leeftijd:
    print("U bent 18, u mag stemmen")
else:
    print("U bent geen 18, u mag niet stemmen")