class Tenis():
    puntajePlayer1 = "0"
    puntajePlayer2 = "0"

    def puntoPlayer1(self):
        if self.puntajePlayer1 == "0":
            self.puntajePlayer1 = "15"
        elif self.puntajePlayer1 == "15":
            self.puntajePlayer1 = "30"
        elif self.puntajePlayer1 == "30":
            self.puntajePlayer1 = "40"
        elif self.puntajePlayer1 == "40" and self.puntajePlayer2 != "40" and self.puntajePlayer2 != "Advantage":
            self.puntajePlayer1 = "Set to Player 1"
        elif self.puntajePlayer1 == "40" and self.puntajePlayer2 == "40" and self.puntajePlayer2 != "Advantage":
            self.puntajePlayer1 = "Advantage"
        elif self.puntajePlayer1 == "40" and self.puntajePlayer2 == "Advantage":
            self.puntajePlayer2 = "40"
        elif self.puntajePlayer1 == "Advantage":
            self.puntajePlayer1 = "Set to Player 1"

    def puntoPlayer2(self):
        if self.puntajePlayer2 == "0":
            self.puntajePlayer2 = "15"
        elif self.puntajePlayer2 == "15":
            self.puntajePlayer2 = "30"
        elif self.puntajePlayer2 == "30":
            self.puntajePlayer2 = "40"
        elif self.puntajePlayer2 == "40" and self.puntajePlayer1 != "40" and self.puntajePlayer1 != "Advantage":
            self.puntajePlayer2 = "Set to Player 2"
        elif self.puntajePlayer2 == "40" and self.puntajePlayer1 == "40" and self.puntajePlayer1 != "Advatange":
            self.puntajePlayer2 = "Advantage"
        elif self.puntajePlayer2 == "40" and self.puntajePlayer1 == "Advantage":
            self.puntajePlayer1 = "40"
        elif self.puntajePlayer2 == "Advantage":
            self.puntajePlayer2 = "Set to Player 2"

    def getScore(self):
        return "Score " + self.puntajePlayer1 + " - " + self.puntajePlayer2
