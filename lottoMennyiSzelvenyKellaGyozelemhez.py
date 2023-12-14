# Lottó számok listájának a létrehozása
import random

lottoGomb = []
kihuzottSzamok = []
tipp = []
talalatok = [0, 0, 0, 0]
#fonyeremeny = 3100000000
#lottoszelvenyAra = 400
counter = 0

lottoszelvenyAra = int(input("Mennyibe kerül egy lottószelvény?: "))
fonyeremeny = int(input("Mennyit fizet az öttalálatos szelvény?: "))
negytalalatos = int(input("Mennyit fizet egy négytalálatos szelvény?: "))
haromtalalatos = int(input("Mennyit fizet egy háromtalálatos szelvény?: "))
kettalalatos = int(input("Mennyit fizet egy kéttalálatos szelvény?: "))

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
        eddigiKettalalatosNyereseg = talalatok[1] * kettalalatos
        eddigiHaromtalalatosNyereseg = talalatok[2] * haromtalalatos
        eddigiNegytalalatosNyereseg = talalatok[3] * negytalalatos
        eddigiBevetel = eddigiKettalalatosNyereseg + eddigiHaromtalalatosNyereseg + eddigiNegytalalatosNyereseg
        eddigiKiadas = counter * lottoszelvenyAra
        jelenlegiMerleg = eddigiKettalalatosNyereseg - eddigiKiadas
        
        print("****************************************************")
        print("Sorsolások száma:", counter) 
        print("Megjátszott szelvény (tipp):", tipp)
        print("Utoljára kihúzott szelvény:", kihuzottSzamok)
        print("Eddigi találatok száma [egytalálatos, kéttalálatos ...]:", talalatok)
        print("Eddigi kiadásunk:", eddigiKiadas, "Ft.")
        print("Eddigi bevételünk:", eddigiBevetel, "Ft.")
        print("A jelenlegi mérleg:", jelenlegiMerleg, "Ft.")
        
    kozosElemek = (set(tipp) & set(kihuzottSzamok))
    kozosElemekSzama = len(kozosElemek)
    
    if kozosElemekSzama > 0:
        if kozosElemekSzama == 1:
            talalatok[0] = talalatok[0] + 1
        elif kozosElemekSzama == 2:
            talalatok[1] = talalatok[1] + 1
        elif kozosElemekSzama == 3:
            talalatok[2] = talalatok[2] + 1
        elif kozosElemekSzama == 4:
            talalatok[3] = talalatok[3] + 1
    
    if kihuzottSzamok == tipp:
        break

elkoltottPenz = lottoszelvenyAra * counter
# nyereseg = fonyeremeny - elkoltottPenz

zaroKettesNyeremeny = talalatok[1] * kettalalatos
zaroHarmasNyeremeny = talalatok[2] * haromtalalatos
zaroNegyesNyeremeny = talalatok[3] * negytalalatos
zaroBevetel = fonyeremeny + zaroKettesNyeremeny + zaroHarmasNyeremeny + zaroNegyesNyeremeny
nyereseg = zaroBevetel - elkoltottPenz
print("Az ön tippje: ", tipp)
print("A kihúzott számok:", kihuzottSzamok)
print("Egytalálatos szelvények:", talalatok[0], "db.")
print("Két találatos szelvények:", talalatok[1], "db. Értékük:", zaroKettesNyeremeny, "Ft.")
print("Három találatos szelvények:", talalatok[2], "db. Értékük:", zaroHarmasNyeremeny, "Ft.")
print("Négy találatos szelvények:", talalatok[3], "db. Értékük:", zaroNegyesNyeremeny, "Ft.")
print("A megvásárolt lottószelvények száma: ", counter)
print("A szelvényekre költött összeg:", elkoltottPenz, "Ft.")
print("A lottó főnyereménye:", fonyeremeny, "Ft.")
print("Az összes pénznyeremény:", zaroBevetel)
print("A játék mérlege:", nyereseg, "Ft.")