class FoodItem():
	def __init__(self, name, price = 1):
		self.price = price
		self.name = name

	def get_price(self):
		return self.price

	def get_item_name(self):
		return self.name

	def display(self):
		print(f"{self.name} {self.price}")

	def new_function(self):
		print("HI NEW FUNCTIOn")