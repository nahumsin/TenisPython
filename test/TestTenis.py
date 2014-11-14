import unittest
import sys
sys.path.append("app")
from Tenis import Tenis


class TestTenis(unittest.TestCase):

    def testScore(self):
        match = Tenis()
        self.assertIn("Score", match.getScore())

    def testPuntoPlayer1With0(self):
        match = Tenis()
        match.puntajePlayer1 = "0"
        match.puntajePlayer2 = "0"
        match.puntoPlayer1()
        self.assertEqual("15", match.puntajePlayer1)

    def testPuntoPlayer1With15(self):
        match = Tenis()
        match.puntajePlayer1 = "15"
        match.puntajePlayer2 = "0"
        match.puntoPlayer1()
        self.assertEqual("30", match.puntajePlayer1)

    def testPuntoPlayer1With30(self):
        match = Tenis()
        match.puntajePlayer1 = "30"
        match.puntajePlayer2 = "0"
        match.puntoPlayer1()
        self.assertEqual("40", match.puntajePlayer1)

    def testPuntoPlayer1With40(self):
        match = Tenis()
        match.puntajePlayer1 = "40"
        match.puntajePlayer2 = "0"
        match.puntoPlayer1()
        self.assertEqual("Set to Player 1", match.puntajePlayer1)

    def testPuntPlayer2With0(self):
        match = Tenis()
        match.puntajePlayer1 = "0"
        match.puntajePlayer2 = "0"
        match.puntoPlayer2()
        self.assertEqual("15", match.puntajePlayer2)

    def testPuntoPlayer2With15(self):
        match = Tenis()
        match.puntajePlayer1 = "0"
        match.puntajePlayer2 = "15"
        match.puntoPlayer2()
        self.assertEqual("30", match.puntajePlayer2)

    def testPuntoPlayer2With30(self):
        match = Tenis()
        match.puntajePlayer1 = "0"
        match.puntajePlayer2 = "30"
        match.puntoPlayer2()
        self.assertEqual("40", match.puntajePlayer2)

    def testPuntoPlayer2With40(self):
        match = Tenis()
        match.puntajePlayer1 = "0"
        match.puntajePlayer2 = "40"
        match.puntoPlayer2()
        self.assertEqual("Set to Player 2", match.puntajePlayer2)

    def testPuntoPlayer1WithDeuce(self):
        match = Tenis()
        match.puntajePlayer1 = "40"
        match.puntajePlayer2 = "40"
        match.puntoPlayer1()
        self.assertEqual("Advantage", match.puntajePlayer1)

    def testPuntoPlayer2WithDeuce(self):
        match = Tenis()
        match.puntajePlayer1 = "40"
        match.puntajePlayer2 = "40"
        match.puntoPlayer2()
        self.assertEqual("Advantage", match.puntajePlayer2)

    def testPuntoPlayer1WithAdvantage(self):
        match = Tenis()
        match.puntajePlayer1 = "Advantage"
        match.puntajePlayer2 = "40"
        match.puntoPlayer1()
        self.assertEqual("Set to Player 1", match.puntajePlayer1)

    def testPuntoPlayer2WithAdvantage(self):
        match = Tenis()
        match.puntajePlayer1 = "40"
        match.puntajePlayer2 = "Advantage"
        match.puntoPlayer2()
        self.assertEqual("Set to Player 2", match.puntajePlayer2)

    def testPuntoPlayer1IfPlayer2Advantage(self):
        match = Tenis()
        match.puntajePlayer1 = "40"
        match.puntajePlayer2 = "Advantage"
        match.puntoPlayer1()
        self.assertEqual("40", match.puntajePlayer2)

    def testPuntoPlayer2IfPlayer1Advantage(self):
        match = Tenis()
        match.puntajePlayer1 = "Advantage"
        match.puntajePlayer2 = "40"
        match.puntoPlayer2()
        self.assertEqual("40", match.puntajePlayer1)

if __name__ == '__main__':
    unittest.main()
