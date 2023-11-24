lepesek = 0
hatarertek = int(input("Kérem a határértéket: "))
leghosszabbSzekvencia = -1
leghosszabbSzekvSzam = -1
vizsgaltSzam = 0
legmagasabbSzam = 0
maximumVizsgaltSzam = 0
szam = 0

for szamlalo in range (2, hatarertek):
    szam = szamlalo
    vizsgaltSzam = szam
    while szam > 1:
        if szam % 2 == 0:
            szam = int(szam / 2)
            lepesek = lepesek + 1
        else:
            szam = int((3 * szam) + 1)
            lepesek = lepesek + 1
            
        if lepesek > leghosszabbSzekvencia:
            leghosszabbSzekvencia = lepesek
            leghosszabbSzekvSzam = vizsgaltSzam
            print("Új leghosszab szekvenciát találtam:", leghosszabbSzekvencia, "a vizsgált szám:", leghosszabbSzekvSzam)
            
        if szam > legmagasabbSzam:
            legmagasabbSzam = szam
            maximumVizsgaltSzam = vizsgaltSzam
            print("Új legmagasabb számot találtam:", legmagasabbSzam, "a vizsgált szám:", maximumVizsgaltSzam)
            
    lepesek = 0
    
print("A leghosszabb sorozat:", leghosszabbSzekvencia, "a hozzá tartozó szám:", leghosszabbSzekvSzam)
print("A legmagasabb szám:", legmagasabbSzam, "a hozzá tartozó kiinduló érték:", maximumVizsgaltSzam)