lengte = float(input("Wat is uw lengte in cm:\n"))
gewicht = float(input("Wat is uw gewicht in kg:\n"))
lengte_m = lengte / 100
BMI = gewicht / (lengte_m ** 2)

if 0 < BMI < 18:
    print("Ondergewicht")
elif BMI < 24:
    print("Normaal geiwcht")
elif BMI < 29:
    print("Bovengewicht")
else:
    print("Extreem bovengewicht")