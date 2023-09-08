

class Customer:
	def __init__(self, name: str):
		self.name = name
		self.reservations = []

	def make_reservation(self):
		print("I'm making a reservation!")
