# Lottó számok listájának a létrehozása
import random

lottoGomb = []
kihuzottSzamok = []
tipp = []
szam = 0

for i in range(0, 5):
    szam = int(input("Kérek egy 1 és 90 közé eső számot: "))
    tipp.append(szam)
    
for i in range (1, 91):
    lottoGomb.append(i)

random.shuffle(lottoGomb)

for i in range(0, 5):
    kihuzottSzamok.append(lottoGomb[i])

kihuzottSzamok.sort()
tipp.sort()

print("Az ön tippje: ", tipp)
print("A kihúzott számok:", kihuzottSzamok)
