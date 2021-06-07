from lingo import Lingo

# Maak een instantie van lingo
mijnLingo = Lingo()

# Contoleer het woord
print(mijnLingo.validate_input(mijnLingo.woord))
print(mijnLingo.woord)
# Test het juiste woord
uitvoer = mijnLingo.validate_input("lingo")
if uitvoer == "Gewonnen":
    print("test OK! - Het juiste woord: " + uitvoer)
else:
    print("test Failed! - Het juiste woord: " + uitvoer)

# Test de juiste lengte
uitvoer = mijnLingo.validate_input("lin")
if uitvoer == "Voer een woord van 5 letters in!":
    print("Test OK! - De juiste lengte: " + uitvoer)
else:
    print("Test FAILED! - De juiste lengte: " + uitvoer)

# Test de juiste uitvoer
invoer = "liaaa"
uitvoer = mijnLingo.validate_input(invoer)
if uitvoer == "LI___":
    print("Test OK! - De juiste letters op de plek: " + invoer + " > " + uitvoer)
else:
    print("Test FAILED! - De juiste letters op de plek: " + invoer + " > " + uitvoer)

# Test de foute letters
invoer = "aaaaa"
uitvoer = mijnLingo.validate_input(invoer)
if uitvoer == "_____":
    print("Test OK! - De juiste letters op de plek: " + invoer + " > " + uitvoer)
else:
    print("Test FAILED! - De juiste letters op de plek: " + invoer + " > " + uitvoer)
