# Lottó számok listájának a létrehozása
import random

lottoGomb = []
kihuzottSzamok = []
tipp = []
fonyeremeny = 3100000000
lottoszelvenyAra = 400
counter = 0

for i in range(0, 5):
    szam = int(input("Kérek egy 1 és 90 közé eső számot: "))
    tipp.append(szam)
    
tipp.sort()

for i in range (1, 91):
    lottoGomb.append(i)

while True:
    counter = counter + 1
    kihuzottSzamok.clear()
    random.shuffle(lottoGomb)

    for i in range(0, 5):
        kihuzottSzamok.append(lottoGomb[i])
        
    # kihuzottSzamok.clear()
    # kihuzottSzamok = [4, 3, 5, 2, 1]

    kihuzottSzamok.sort()
    #print(kihuzottSzamok)
    if counter % 500000 == 0:
        print("Szamlalo:", counter, "tipp:", tipp, "kihuzott:", kihuzottSzamok)
    
    if kihuzottSzamok == tipp:
        break

elkoltottPenz = lottoszelvenyAra * counter
nyereseg = fonyeremeny - elkoltottPenz

print("Az ön tippje: ", tipp)
print("A kihúzott számok:", kihuzottSzamok)
print("A megvásárolt lottószelvények száma: ", counter)
print("A szelvényekre költött összeg:", elkoltottPenz)
print("A lottó főnyereménye:", fonyeremeny)
print("Az on nyeresége:", nyereseg)
