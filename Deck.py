from Card import Card
import random

class Deck():
	"""docstring for ClassName"""
	
	deck = []

	def __init__(self):
		self.createDeck()

	def createDeck(self):
		for i in range(1,5):
			for x in range(1, 14):
				if x > 10:
					face_card = Card.getFaceCard(x)
				else: 
					face_card = None
				self.deck.append(Card(x,Card.getSuite(i),face_card))
		self.shuffleDeck()

	def shuffleDeck(self):
		random.shuffle(self.deck)

	def playCard(self):
		if self.getCardsLeft() > 0:
			return self.deck.pop()

	def getCardsLeft(self):
		return len(self.deck)

#if __name__ == '__main__':
#		new_deck = Deck()
#		for card in new_deck.deck:
#			print card
#		print new_deck.playCard()
#		print new_deck.playCard()
#		print new_deck.playCard()
