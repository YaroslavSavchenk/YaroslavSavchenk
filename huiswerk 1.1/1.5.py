huidige = int(input("Wat is uw huidige verdipping:\n"))
gewenste = int(input("Wat is uw gewenste verdipping:\n "))

if huidige > gewenste:
    print("U gaat naar beneden")
elif huidige < gewenste:
    print("U gaat naar boven")
else:
    print("U hoeft nergens heen")
    