import sqlite3


class Lingo:
    # Constructor met de declaratie van het attribuut woord
    def __init__(self):
        self.woord = self.selecteer_woord()

    def validate_input(self, invoer):
        # Conferteer de invoer naar kleine letters
        invoer = str.lower(invoer)

        # Controleer of de invoer string gelijk is aan het te raden woord
        if invoer == self.woord:
            return "Gewonnen"

        if len(invoer) != 5:
            return "Voer een woord van 5 letters in!"

        # Vergelijk elke letter uit de invoer string met het te raden woord
        uitvoer = ""
        for i in range(5):
            if invoer[i] == " " + self.woord[i] + " ":
                uitvoer += str.upper(" **" + invoer[i] + "** ")
            elif invoer[i] in self.woord:
                uitvoer += str.upper(invoer[i])
            else:
                uitvoer += " ~~" + invoer[i] + "~~ "
        return uitvoer

    # Selecteer een random woord
    @staticmethod
    def selecteer_woord():

        # Verbinding maken met de database
        connection = sqlite3.connect("lingo.sqlite3")

        # Selecteer een woord uit de database
        cursor = connection.execute("SELECT * FROM vijfletters ORDER BY RANDOM();")
        for row in cursor:
            woord = row[0]
        connection.close()

        # Return het woord
        return woord
