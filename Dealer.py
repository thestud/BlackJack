from Player import Player

class Dealer(Player):
	"""docstring for Dealer"""
	def __init__(self, name):
		Player.__init__(self,name,0)
		#self.hand = Hand()
		#self.name = name

	def showHand(self):
		self.hand.showHand()

#if __name__ == '__main__':
#	dealer = Dealer("CPU")
	