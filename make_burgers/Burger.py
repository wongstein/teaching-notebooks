
import FoodItem

from FoodItem import FoodItem

class Burger(FoodItem):
	def __init__(self):
		self.name = "Burger"
		self.price = 5
		self.ingredients = []

	def add_ingredients(self, *args):
		for arg in args:
			self.ingredients.append(arg)
