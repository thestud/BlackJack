from Player import Player
from Dealer import Dealer
from Deck import Deck
from Card import Card

class Game():
	"""docstring for Game"f __init__(self, arg):
		super(Game,.__init__()
		self.arg = arg
	"""
	def __init__(self):
		self.player = Player("Player",100)
		self.dealer = Dealer("CPU-Dealer")
		self.deck_of_cards = Deck()

	def playOfTheDealer():
		while self.dealer.score() < 17:
				pass	

	def startTheGame(self):
		#player needs to bet
		print("___New Hand___")
		self.dealer.hit(self.deck_of_cards.playCard())
		self.player.hit(self.deck_of_cards.playCard())	
		self.dealer.hit(self.deck_of_cards.playCard())
		self.player.hit(self.deck_of_cards.playCard())	

	def displayGame(self,dealerReveal=False):
		print("")
		print(self.dealer.name + "'s hand: ") 
		if dealerReveal == False:
			self.dealer.showCard(0)
			#print("???")
			Card.displayBlankCard()
		else:
			self.dealer.showHand()
			print(self.dealer.name + " score = " + str(self.dealer.score()))
		print("-------")	
		print(self.player.name + "'s hand: ") 
		self.player.showHand()
		print(self.player.name + " score = " + str(self.player.score()))
		print(self.player.name + " bank = " + str(self.player.bank))
		print("")

	def checkForBlackJack(self):
		if self.dealer.score() == 21:
			print(self.dealer.name + " wins")
			return True

		if self.player.score() == 21:
			print(self.player.name + " wins")
			self.player.bank = self.betAmount*3
			return True
		return False 	

	def inputFromThePlayer(self):
		result = input("j to hit:\nf to hold:\nq to Quit:\n")
		return result

	def main(self):
		playing = True
		while playing == True:
			self.dealer.clearHand()
			self.player.clearHand()

			try:
				self.betAmount = float(input("What do you want to bet?: "))
			except:
				print("quitting the game")
				playing = False
				break

			if self.player.bet(self.betAmount) == False:
				print("GET OUT OF THE CASINO!!")	
				playing = False
				break

			self.startTheGame()
			self.displayGame()
			
			playingHand = True
			while playingHand == True:
				
				if self.checkForBlackJack() == True:
					playingHand = False
					break

				result = self.inputFromThePlayer() 

				if result == "q":
					playing = False
					playingHand = False

				if result == "j":
					self.player.hit(self.deck_of_cards.playCard())
					self.displayGame()

					if self.player.bust() == True:
						print(self.player.name + " loses!")	
						playingHand = False
						break

				if result == "f":
					#print("dealer's score = " + str(self.dealer.score())
					self.displayGame(True)
					while self.dealer.score() < 17 and self.dealer.bust() == False:
						self.dealer.hit(self.deck_of_cards.playCard())
						self.displayGame(True)

						if self.dealer.bust() == True:
							print(self.dealer.name + " loses!")	
							self.player.bank = self.betAmount*2
							playingHand = False
							break

						if self.dealer.score() > self.player.score():
							print(self.player.name + " loses!")	
							playingHand = False
							break

						if self.dealer.score() == self.player.score():
							print("There is a draw")
							playingHand = False
							break

					if self.dealer.score() < self.player.score():
						print(self.player.name + " wins!")
						self.player.bank = self.betAmount*2	
						break

					if self.dealer.score() > self.player.score():
						print(self.player.name + " loses!")	
						break

if __name__ == '__main__':
	my_game = Game()
	my_game.main()

