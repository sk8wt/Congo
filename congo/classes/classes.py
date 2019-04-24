
class Merch:
	def __init__(self, name, price, desc, num_avail, img):
		self.name = name
		self.price=price
		self.image=img
		self.num_avail = num_avail
		self.desc = desc


class Merchant:
	def __init__(self, m_id, name, rating):
		self.name = name
		self.m_id = m_id
		self.rating = rating

class Creditcard:
	def __init__(self, cc_number, cc_name, cc_expDate, cc_secCode):
		self.cc_number = cc_number
		self.cc_name = cc_name
		self.cc_expDate = cc_expDate
		self.cc_secCode = cc_secCode

class Customer:
	def __init__(self, name, dob, addr, cc_number):
		self.name = name
		self.dob = dob
		self.addr = addr
		self.cc_number = cc_number

class Orders:
	def __init__(self, name, dob, addr, cc_number):
		self.name = name
		self.dob = dob
		self.addr = addr
		self.cc_number = cc_number

class Reviews:
	def __init__(self, id, data, ts, rating, merch_id):
		self.id = id
		self.data =
		self.ts = ts
		self.rating = rating
		self.merch_id = merch_id

class Sells:
	def __init__(self, id, merch_id, m):
		self.id = id
		self.merch_id = merch_id
		self.m = m
