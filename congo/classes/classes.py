
class Merch:
	def __init__(self, name, price, desc, num_avail, img):
		self.name = name
		self.price=price
		self.image=img
		self.num_avail = num_avail
		self.desc = desc


class Merchant:
	def __init__(self, name):
		self.name = name
		# TODO: put list of item IDs seller sells here.