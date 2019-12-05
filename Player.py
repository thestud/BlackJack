from Hand import Hand

class Player():
	"""docstring for Playedef __init__(self, arg):
		super
		(Player).__init__()
		self.arg = arg
	"""	
	def __init__(self,name,bank):
		self.hand = Hand()
		self.name = name
		self.bank = bank

	def hit(self,card):
		self.hand.hit(card)

	def score(self):
		if self.hand.score(True) < 22:
			return self.hand.score(True)
		elif self.hand.score(True) > 21:
			if self.hand.score(False) < 22:
				return self.hand.score(False)
		elif self.hand.score(True) == 21:
			return self.hand.score(True) 
		elif self.hand.score(True) > 21:
			return self.hand.score(True)
		else:
			#print("does it even get here")
			return self.hand.score(False)

		#print("Too far!")
		return self.hand.score(False) 

	def showCard(self,index):
		self.hand.showCard(index)

	def showHand(self):
		self.hand.showHand()

	def clearHand(self):
		self.hand.clearHand()

	def bust(self):
		return self.hand.bust()

	def bet(self,amount):
		if amount < self.bank:
			self.bank -= amount
			return True
		else:
			print("You are broke!")
			return False 
