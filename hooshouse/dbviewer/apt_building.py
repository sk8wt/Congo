
class apt_building:
    def __init__(self, address, units, name, year):
        self.address = address
        self.units = units
        self.name = name
        self.year = year

class landlord:
    def __init__(self, company_name, office_address, phone_number, email_address):
        self.company_name =company_name
        self.office_address = office_address
        self.phone_number = phone_number
        self.email_address = email_address
        self.apt_address = apt_address

class unit:
    def __init__(self, address, apt_number, occupied, furnished,sq_footage, num_bathrooms, num_bedrooms, internet, laundry, kitchen):
        self.address =address
        self.apt_number = apt_number
        self.occupied = occupied
        self.furnished = furnished
        self.sq_footage =sq_footage
        self.num_bathrooms = num_bathrooms
        self.num_bedrooms = num_bedrooms
        self.internet = internet
        self.laundry = laundry
        self.kitchen = kitchen

class lease:
    def __init__(self, computing_id, apt_address, apt_number, rent_amount, term):
        self.computing_id = computing_id
        self.apt_address = apt_address
        self.apt_number = apt_number
        self.rent_amount = rent_amount
        self.term = term
class tenant:
    def __init__(self, computing_id, name, perm_address, cur_address, phone_num, email_address):
        self.computing_id = computing_id
        self.name = name
        self.perm_address = perm_address
        self.cur_address = cur_address
        self.phone_num = phone_num
        self.email_address = email_address


class available_apt:
    def __init__(self, building_name, address, count):
        self.building_name = building_name
        self.address = address
        self.count = count
