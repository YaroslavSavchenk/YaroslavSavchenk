cijfer = float(input("Wat is uw raportcijfer:\n"))

afgeronde = round(cijfer)

if afgeronde > 9:
    print("Uitstekend")
elif afgeronde >= 8:
    print("Goed")
elif afgeronde >= 7:
    print("Ruim voldoende")
elif afgeronde >= 6: 
    print("Voldoende")
elif afgeronde >= 5:
    print("Matig")
else:
    print("Onvoldonde")