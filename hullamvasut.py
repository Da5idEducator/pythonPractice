hatarertek = int(input("Kérem a határértéket: "))
lepesek = 0
maximumLepes = -1
maximumLepesSzamuSzam = -1
vizsgaltSzam = -1
elertLegmagasabbSzam = -1
elertLegmagasabbSzamhozTartozoVizsgaltSzam = -1

for szamlalo in range (2, hatarertek):
    szam = szamlalo
    vizsgaltSzam = szam
    if vizsgaltSzam % 100000 == 0:
        print("*********************************")
        print("***                           ***")
        print("*** A vizsgált szám: ", szam, " ***")
        print("***                           ***")
        print("*********************************")
        
    while szam > 1:
        if szam % 2 == 0:
            szam = int(szam / 2)
            lepesek = lepesek + 1
            # print(szam)
        else:
            szam = int((szam * 3) + 1)
            lepesek = lepesek + 1
            if szam > elertLegmagasabbSzam:
                elertLegmagasabbSzam = szam
                elertLegmagasabbSzamhozTartozoVizsgaltSzam = vizsgaltSzam
                print("Új legmagasabb elért szám:", elertLegmagasabbSzam, "a vizsgalt szam:", vizsgaltSzam)
            # print(szam)
        
        if lepesek > maximumLepes:
            maximumLepes = lepesek
            maximumLepesSzamuSzam = vizsgaltSzam
            print("Új maximum lépésszám:", maximumLepes, "a vizsgált szám:", vizsgaltSzam)
        
    lepesek = 0
print("A leghosszabb sorozat:", maximumLepes, " lepesbol allt.")
print("Leghosszabb sorozat a:", maximumLepesSzamuSzam, "szamhoz tartozott")
print("Az elért legmagasabb szám:", elertLegmagasabbSzam)
print("Az elért legmagasabb számhoz tartozó kiinduló érték:", elertLegmagasabbSzamhozTartozoVizsgaltSzam)

        