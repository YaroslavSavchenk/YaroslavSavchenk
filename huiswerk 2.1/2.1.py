aantal = int(input("Voer aantal vogels in:\n"))

if 1 > aantal > 0:
    print(f"ik zie {aantal} vogel")
elif aantal > 1:
    print(f"ik zie {aantal} vogels")
else:
    print("Er zijn geens vogels")