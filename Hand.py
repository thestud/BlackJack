from Card import Card

class Hand():
	"""
	"""
	def __init__(self):
		self.cards = []

	def score(self,ace_is_eleven=False):
		#hands_score = sum(self.cards)
		#ordered_hand = set(self.cards)
		if len(self.cards) == 0:
			print("no cards")
			return 0

		hands_score = 0
		if ace_is_eleven == False:
			for card in self.cards:
				if card.number > 10:
					hands_score += 10
				else:
					hands_score += card.number
		elif ace_is_eleven == True:
			for card in self.cards:
				if card.number == 1:
					hands_score += 11
				elif card.number > 10:
					hands_score += 10
				else:
					hands_score += card.number
		#print("hands_score = " + str(hands_score))
		return hands_score

	def bust(self):
		if self.score(True) < 22:
			return False
		elif self.score(True) > 21:
			if self.score(False) < 22:
				return False
		return True

	def hit(self,card):
		self.cards.append(card)

	def clearHand(self):
		self.cards = []

	def blackJack(self):
		if self.score(False) == 21 or self.score(True) == 21:
			return True
		else:
			return False

	def showHand(self):
		for card in self.cards:
			#print(card)
			card.displayCard()

	def showCard(self,index):
		if index < len(self.cards):
			#print(self.cards[index])
			self.cards[index].displayCard()
		else:
			print("index is out of range")

#if __name__ == '__main__':
#	test_hand = Hand()
#	test_hand.hit(Card(1,Card.getSuite(1),None))
#	test_hand.hit(Card(11,Card.getSuite(2),None))
#	print("score is with ace = 1, = " + str(test_hand.score()))
#	print("score is with ace = 11, = " + str(test_hand.score(True)))