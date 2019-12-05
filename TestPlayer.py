import unittest
from Player import Player
from Card import Card

class TestPlayer(unittest.TestCase):
	"""docstring for TestPlayer"unittest.TestCasef __init__(self, arg):
		super(TestPlayer,unittest.TestCase.__init__()
		self.arg = arg
	"""
	def setupTestPlayer(self):
		self.player = Player("Player")

	def testOneCardOneAces(self):
		self.setupTestPlayer()
		self.player.hit(Card(1,Card.getSuite(1),None))	
		self.assertEqual(self.player.score(),11)

	def testTwoCards(self):
		self.setupTestPlayer()
		self.player.hit(Card(2,Card.getSuite(1),None))
		self.player.hit(Card(2,Card.getSuite(2),None))	
		self.assertEqual(self.player.score(),4)

	def testTwoCardsOneKing(self):
		self.setupTestPlayer()
		self.player.hit(Card(2,Card.getSuite(1),None))
		self.player.hit(Card(13,Card.getSuite(2),None))	
		self.assertEqual(self.player.score(),12)

	def testTwoCardsOneAceOneKing(self):
		self.setupTestPlayer()
		self.player.hit(Card(1,Card.getSuite(1),None))
		self.player.hit(Card(13,Card.getSuite(2),None))	
		self.assertEqual(self.player.score(),21)

	def testThreeCardsOneAceTwoKings(self):
		self.setupTestPlayer()
		self.player.hit(Card(1,Card.getSuite(1),None))
		self.player.hit(Card(13,Card.getSuite(2),None))	
		self.player.hit(Card(13,Card.getSuite(1),None))
		self.assertEqual(self.player.score(),21)

	def testABust(self):
		self.setupTestPlayer()
		self.player.hit(Card(13,Card.getSuite(1),None))
		self.player.hit(Card(13,Card.getSuite(2),None))	
		self.player.hit(Card(13,Card.getSuite(3),None))
		self.assertEqual(self.player.score(),30)
		self.assertEqual(self.player.bust(),True)

	def testAnotherBust(self):
		self.setupTestPlayer()
		self.player.hit(Card(8,Card.getSuite(3),None))
		self.player.hit(Card(3,Card.getSuite(2),None))	
		self.player.hit(Card(5,Card.getSuite(4),None))
		self.player.hit(Card(8,Card.getSuite(1),None))
		self.assertEqual(self.player.score(),24)

if __name__ == '__main__':
	unittest.main()