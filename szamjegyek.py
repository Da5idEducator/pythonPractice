szam = int(input("Kerek egy szamot: "))
szamjegyek = 0

while szam > 0:
    szamJegy = szam % 10
    print("A kovetkezo szamjegy: ", szamJegy)
    szamjegyek = szamjegyek + 1
    szam = szam - szamJegy
    szam = int(szam / 10)

print("A szamjegyek szama: ", szamjegyek)

