magassag = float(input("Írja be a magasságát cm-ben: "))
testsuly = float(input("Írja be a testsúlyát kg-ban: "))

magassagMeterben = magassag / 100

BMI = testsuly / (magassagMeterben * magassagMeterben)

print("Az ön testtömegindexe (BMI): ", BMI)

if BMI < 18.5:
    print("Ön alultáplált.")
    print("  o  ")
    print(" )|( ")
    print("  A  ")
elif BMI >= 18.5 and BMI < 24.9:
    print("Az ön testsúlya ideális.")
    print("  o  ")
    print(" ||| ")
    print("  A  ")
elif BMI >= 24.9 and BMI < 29.9:
    print("Ön túlsúlyos.")
    print("Az ön testsúlya ideális.")
    print("  o  ")
    print(" (|) ")
    print("  A  ")
elif BMI >=29.9 and BMI < 34.9:
    print("Ön elhízott.")
    print("  o  ")
    print("( | ) ")
    print("  A  ")
elif BMI >= 34.9 and BMI < 39.9:
    print("Ön súlyosan elhízott.")
    print("  o  ")
    print("(*|* ) ")
    print("  A  ")
else:
    print("Ön morbidan elhízott.")
    print("   o     ")
    print("( *|*  ) ")
    print("   A     ")
    