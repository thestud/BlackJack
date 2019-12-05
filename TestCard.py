import unittest
from Card import Card

class TestCard(unittest.TestCase):
	"""docstring for ClassName"""
	def testOneNumber(self):
		card = Card(1,Card.getSuite(1),None)
		card.displayCard() 

	def testTen(self):
		card = Card(10,Card.getSuite(1),None)
		card.displayCard() 

	def testJack(self):
		card = Card(11,Card.getSuite(1),Card.getFaceCard(11))
		card.displayCard() 

	def testQueen(self):
		card = Card(12,Card.getSuite(1),Card.getFaceCard(12))
		card.displayCard() 

	def testKing(self):
		card = Card(13,Card.getSuite(1),Card.getFaceCard(13))
		card.displayCard() 

	def testSuites(self):
		card = Card(5,Card.getSuite(1),None)
		card.displayCard() 
		card = Card(5,Card.getSuite(2),None)
		card.displayCard() 
		card = Card(5,Card.getSuite(3),None)
		card.displayCard() 
		card = Card(5,Card.getSuite(4),None)
		card.displayCard() 

if __name__ == '__main__':
	unittest.main()