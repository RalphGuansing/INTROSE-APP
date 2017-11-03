
### Inventory View
class Inventory:

	### suppliers - list of suppliers
	### products - list of products
	def __init__(self, suppliers, products):
		Inventory.products = products

	def __init__(self):
		self.products = []

	def add_product(self, product):
		self.products.append(product)

	def add_product_quantity(self, product, quantity):
		x = 0
		for tempproduct in self.products:
			if tempproduct == product:
				self.products[x].add_quantity(quantity)
				break
			x += 1

	def get_products(self):
		return self.products

	def get_product_count(self):
		return len(self.products)


class Supplier:
	
	def __init__(self, name, address, email, contactnumber):
		self.name = name
		self.address = address
		self.email = email
		self.contactnumber = contactnumber

	def __str__(self):
		return self.name + '\n' + 'Address: ' + self.address + '\n' + 'Email: ' + self.email + '\n' + 'Contact Number: ' + self.contactnumber

	def __repr__(self):
		return self.name + '\n' + 'Address: ' + self.address + '\n' + 'Email: ' + self.email + '\n' + 'Contact Number: ' + self.contactnumber


class Product:

	def __init__(self, name, supplier, packaging, perunitprice, retailprice, quantity, lastupdated):
		self.name = name
		self.supplier = supplier
		self.packaging = packaging
		self.perunitprice = perunitprice
		self.retailprice = retailprice
		self.quantity = quantity
		self.lastupdated = lastupdated

	def add_quantity(self, quantity):
		self.quantity += quantity

	def __str__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + self.perunitprice + '\n' + 'Retail Price: ' + self.retailprice

	def __repr__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + self.perunitprice + '\n' + 'Retail Price: ' + self.retailprice

