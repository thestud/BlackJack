class Card():
	"""docstring for Card"""

	def __init__(self,number,suite,face_card):
		self.number = number
		self.suite = suite
		self.face_card = face_card

	@staticmethod
	def getSuite(index):
		SUITE_HEARTS = "HEARTS"
		SUITE_DIAMONDS = "DIAMONDS"
		SUITE_SPADES = "SPADES"
		SUITE_CLUBS = "CLUBS"

		if index == 1:
			return SUITE_HEARTS
		if index == 2:
			return SUITE_DIAMONDS
		if index == 3:
			return SUITE_SPADES
		if index == 4:
			return SUITE_CLUBS

	@staticmethod
	def getFaceCard(index):
		FACE_CARD_KING = "KING"
		FACE_CARD_QUEEN = "QUEEN"
		FACE_CARD_JACK = "JACK"

		if index == 11:
			return FACE_CARD_JACK
		if index == 12:
			return FACE_CARD_QUEEN
		if index == 13:
			return FACE_CARD_KING

	def __str__(self):
		if self.number == 1:
			name_of_card = "Ace"
		elif self.number > 10:
			name_of_card = self.face_card
		else:
			name_of_card = str(self.number)
		return name_of_card + " of " + self.suite

	def formatNumber(self,number):
		if number < 10:
			return " " + str(number)
		else:
			return str(number)

	def formatCardNumber(self):
		if self.number < 11:
			return self.formatNumber(self.number)
		
		return self.face_card

	def formatTopRow(self):
		if self.number < 10:
			print("|" + str(self.number) + "     |")
		elif self.number == 10:
			print("|" + str(self.number) + "    |")
		elif self.number == 11:
			print("|" + self.face_card + "  |")
		elif self.number == 12:
			print("|" + self.face_card + " |")
		elif self.number == 13:
			print("|" + self.face_card + "  |")

	def formatBottomRow(self):
		if self.number < 10:
			print("|     " + str(self.number) + "|")
		elif self.number == 10:
			print("|    " + str(self.number) + "|")
		elif self.number == 11:
			print("|  " + self.face_card + "|")
		elif self.number == 12:
			print("| " + self.face_card + "|")
		elif self.number == 13:
			print("|  " + self.face_card + "|")

	def formatSuites(self):
		if self.suite == Card.getSuite(2):
			print("|DIAMON|")
		elif self.suite == Card.getSuite(4):
			print("|" + self.suite + " |")
		else:
			print("|" + self.suite + "|")

	def displayCard(self):
		print("/------\\")
		self.formatTopRow()
		print("|      |")
		self.formatSuites()
		self.formatBottomRow()
		print("\\------/")

	@staticmethod
	def displayBlankCard():
		print("/------\\")
		print("|- - - |")
		print("| - -  |")
		print("|- - - |")
		print("| - -  |")
		print("\\------/")

		