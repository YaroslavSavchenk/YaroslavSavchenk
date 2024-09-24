totaal = 0
constante = 5.5
for i in range(1,4):
    cijfer = float(input(f"Wat is uw examen voor examen {i} \n"))
    totaal += cijfer
    gem = totaal / 3
    if constante > cijfer:
        print("Let op je hebt een onvoldonde")
    if i == 3:
        if gem > constante:
            print("U bent geslaagd en uw gemmidelde cijfer is:", gem)
        else:
            print("U bent niet geslaagd en uw gemmidelde cijfer is:", gem)
