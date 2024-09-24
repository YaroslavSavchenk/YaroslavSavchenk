#1.7
lijst = []

for i in range(3):
    getaal = int(input("Wat is uw getaal:\n"))
    lijst.append(getaal)

print(f"Het grootste getaal is {max(lijst)}")
#1.7b
if  lijst[0] == lijst[1] == lijst[2]:
    print("Alle getallen zijn hetzelfde")
else:
    print("Er zijn geen trippele getallen")
#1.7c
if len(lijst) != len(set(lijst)):
    print("Er zijn twee hetzelfde getallen")
else:
    print("Er zijn geen dubbele getallen")
#1.7d
if lijst == sorted(lijst):
    print("De getallen zijn oplopend")
else:
    print("De getalen zijn niet oplopend")


