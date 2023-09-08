

from datetime import datetime, timedelta


class CarRental:
	def __init__(self, this_id: int, model: str):
		self.id = this_id
		self.model = model 
		self.calendar = {}

	def check_availablility(self):
		print("I'm checking!")

	def block_time(self):
		print("I'm blocking time!")

	def make_unavaialble(self):
		pass