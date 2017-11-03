
### Inventory View
class Inventory:

	### products - list of products
	def __init__(self, products):
		Inventory.products = products

	def add_product(self, product):
		self.products.append(product)

	def add_product_quantity(self, product, quantity):
		a = [prod.add_quantity(quantity) for prod in self.products if prod == product ]


	def get_products(self):
		return self.products

	def get_product_count(self):
		return len(self.products)

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
