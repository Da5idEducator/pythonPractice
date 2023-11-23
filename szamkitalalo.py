import random

tipp = 0
gondoltSzam = random.randint(1, 100)

tipp = int(input("Gondoltam egy számra. Tippeld meg!: "))

while tipp != gondoltSzam:
    if tipp < gondoltSzam:
        print("A gondolt szám NAGYOBB")
        tipp = int(input("Próbáld újra! Tipp:  "))
    elif tipp > gondoltSzam:
        print("A gondolt szám KISEBB!")
        tipp = int(input("Kérem az új tippet: "))

print("Nyertél! Kitaláltad a számot! Kérd a tanárodtól a plusz pontot!")
        