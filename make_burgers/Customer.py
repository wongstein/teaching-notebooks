
class Customer:
	def __init__(self, name):
		self.name = name
		self.bill = 0
		self.order_list = []
		self.password = 

	def make_order(self, *args): # expecting args to be a Burger or Fries class
		for arg in args:
			self.bill += arg.get_price()
			self.order_list.append(arg)

	def show_order(self):
		for item in self.order_list:
			item.display()

	def show_balance(self):
		return self.bill

