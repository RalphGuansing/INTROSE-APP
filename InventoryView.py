import pandas as pd
import pymysql as sql
import datetime

### Inventory View
class Inventory:

	"""This module stores all the products"""

	def __init__(self, products, cursor):

		"""Constructor
		Args:
			products ([]): list of products to be stored in the inventory
			cursor: cursor to the database

		"""

		self.products = products


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
		#self.df_inv = self.df_inv.drop(['idinventory'],axis=1)
		self.df_inv['productName'] = self.df_inv['productName'].astype('str')
		self.cursor = self.connect.cursor()


	def get_product_list(self):

		"""returns the product list from the database
		Returns:
			[product_list]
		"""

		product_list = [Product(row[1][0],row[1][1],row[1][2],row[1][3],row[1][4],row[1][5],row[1][6],row[1][7]) for row in self.df_inv.iterrows()]
		return product_list


	def close_connection(self):
		"""closes the connection to the database"""
		self.connect.close()


	def add_product(self, name, supplier, packaging, perunitprice, retailprice, quantity):

		"""add product to the inventory
		Args:
			product (Product): product to be added in the inventory

		"""
		###Check if the product already exists
		if self.cursor.execute("SELECT * FROM introse.inventory WHERE productName = '" + name + "'") == 0:
			self.cursor.execute("INSERT INTO `introse`.`inventory` (`productName`, `supplier`, `packagingType`, `perunitprice`, `retailprice`, `quantity`, `lastupdated`) VALUES ('" + name + "', '" + supplier + "', '" + packaging + "', '" + str(perunitprice) + "', '" + str(retailprice) + "', '" + str(quantity) + "', '" + str(datetime.datetime.now()) + "');")
		else:
			print('Product has already been added')


	def add_product_quantity(self, product, quantity):

		"""add a certain quantity to the product
		Args:
			product (Product): chosen product
			quantity (int): amount to be added

		"""
		if self.cursor.execute("SELECT * FROM introse.inventory WHERE productName = '" + product.name + "'") != 0:
			temp_product = list(filter(lambda x: x.name == product.name, self.products))
			self.cursor.execute("UPDATE `introse`.`inventory` SET `quantity`='" + str((temp_product[0].quantity + quantity)) + "', `lastupdated`='" + str(datetime.datetime.now()) + "' WHERE `idinventory`='" + str(temp_product[0].id) + "';")
			#a = [prod.add_quantity(quantity) for prod in self.products if prod == product ]
		else:
			print('product does not exist!')


class Product:

	"""Represents the products"""

	def __init__(self, id, name, supplier, packaging, perunitprice, retailprice, quantity, lastupdated):

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

		self.id = id
		self.name = name
		self.supplier = supplier
		self.packaging = packaging
		self.perunitprice = perunitprice
		self.retailprice = retailprice
		self.quantity = quantity
		self.lastupdated = lastupdated


	def __str__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + str(self.perunitprice) + '\n' + 'Retail Price: ' + str(self.retailprice)

	def __repr__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + str(self.perunitprice) + '\n' + 'Retail Price: ' + str(self.retailprice)

if __name__ == '__main__':
	sample = InventoryDatabase()
	inv = Inventory(sample.get_product_list(), sample.cursor)
	print(sample.get_product_list()[0])
	inv.add_product_quantity(sample.get_product_list()[0],30)
	inv.add_product('yakult','nestle','bottle',10,10,20)
	sample.close_connection()















