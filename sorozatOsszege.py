alsoHatar = 0
felsoHatar = 0
osszeg = 0

alsoHatar = int(input("Kérem a sorozat alsó határát: "))
felsoHatar = int(input("Kérem a sorozat felső határát: "))

while alsoHatar <= felsoHatar:
    osszeg = osszeg + alsoHatar
    alsoHatar = alsoHatar + 1
    
print("A sorozat tagjainak összege: ", osszeg)
