import pandas as pd
import pymysql as sql

### Inventory View
class Inventory:

	"""This module stores all the products"""

	def __init__(self, products):

		"""Constructor
		Args:
			products ([]): list of products to be stored in the inventory

		"""

		self.products = products

	def add_product(self, product):

		"""add product to the inventory
		Args:
			product (Product): product to be added in the inventory

		"""

		self.products.append(product)

	def add_product_quantity(self, product, quantity):

		"""add a certain quantity to the product
		Args:
			product (Product): chosen product
			quantity (int): amount to be added

		"""

		a = [prod.add_quantity(quantity) for prod in self.products if prod == product ]


	def get_products(self):

		"""returns the list of products
		Returns:
			[self.products]

		"""

		return self.products

	def get_product_count(self):

		"""returns the number of products in the inventory
		Returns:
			[len(self.products)]

		"""

		return len(self.products)

class InventoryDatabase:

	"""Responsible for retrieving and updating data in the database"""

	def __init__(self):

		"""Default constructor"""

		self.connect = sql.connect('localhost','root','root','introse',autocommit=True)
		self.df_inv = pd.read_sql('SELECT * FROM introse.inventory;',self.connect)
		self.df_inv = self.df_inv.drop(['idinventory'],axis=1)
		self.df_inv['productName'] = self.df_inv['productName'].astype('str')

	def get_product_list(self):

		"""returns the product list from the database
		Returns:
			[product_list]
		"""

		product_list = [Product(row[1][0],row[1][1],row[1][2],row[1][3],row[1][4],row[1][5],row[1][6]) for row in self.df_inv.iterrows()]
		return product_list

class Product:

	"""Represents the products"""

	def __init__(self, name, supplier, packaging, perunitprice, retailprice, quantity, lastupdated):

		"""Constructor
		Args:
			name (string): name of the product
			supplier (string): name of the supplier
			packaging (string): packaging type
			perunitprice (float): price of the product
			retailprice (float): retail price of the product
			quantity (int): amount
			lastupdated (datetime): when was the quantity updated
		"""

		self.name = name
		self.supplier = supplier
		self.packaging = packaging
		self.perunitprice = perunitprice
		self.retailprice = retailprice
		self.quantity = quantity
		self.lastupdated = lastupdated

	def add_quantity(self, quantity):

		"""updates the quantity of the product
		Args:
		quantity (int): amount

		"""

		self.quantity += quantity

	def __str__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + str(self.perunitprice) + '\n' + 'Retail Price: ' + str(self.retailprice)

	def __repr__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + str(self.perunitprice) + '\n' + 'Retail Price: ' + str(self.retailprice)

