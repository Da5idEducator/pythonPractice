alsoHatar = 0
felsoHatar = 0
osszeg = 0

alsoHatar = int(input("Kérem a sorozat alsó határát: "))
felsoHatar = int(input("Kérem a sorozat felső határát: "))

szamossag = felsoHatar - alsoHatar + 1

osszeg = int(((alsoHatar + felsoHatar) * szamossag) / 2)

print("A sorozat elemeinek összege: ", osszeg)