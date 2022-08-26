import unittest
from  Day2.Rock_paper_scissor1 import rock_paper_scissor
class Addtest(unittest.TestCase):
    def testAdd1(self):
        self.assertEqual('player2 wins',rock_paper_scissor('rock','paper'))
    def testAdd2(self):
        self.assertEqual('player1 wins',rock_paper_scissor('rock', 'scissor'))
    def testAdd3(self):
            self.assertEqual('player wins', rock_paper_scissor('rock', 'scissor'))