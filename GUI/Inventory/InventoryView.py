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
		self.df_inv['productName'] = self.df_inv['productName'].astype('str')
		self.cursor = self.connect.cursor()


	def get_product_list(self):

		"""returns the product list from the database
		Returns:
			[product_list]
		"""

		product_list = [Product(row[1][0],row[1][1],row[1][2],row[1][3],row[1][4],row[1][5],row[1][6],row[1][8],row[1][7]) for row in self.df_inv.iterrows()]
		return product_list


	def close_connection(self):
		"""closes the connection to the database"""
		self.connect.close()


	def add_product(self, name, supplier, packaging, per_unit_price, retail_price, quantity, vatable):

		"""add product to the inventory
		Args:
			name (string): product to be added in the inventory
			supplier (string): supplier of the product
			packaging (string): packaging type of the product
			per_unit_price (float): per unit price of the product
			retail_price (float): retail price of the product
			quantity (int): quantity of the product
			vatable (boolean): is the product vatable or non vatable
		"""
		###Check if the product already exists
		
		if self.cursor.execute("SELECT * FROM introse.inventory WHERE productName = '" + name + "'") == 0:
			self.cursor.execute("INSERT INTO `introse`.`inventory` (`productName`, `supplier`, `packagingType`, `perunitprice`, `retailprice`, `quantity`, `lastupdated`, `vatable`) VALUES ('" + name + "', '" + supplier + "', '" + packaging + "', '" + str(per_unit_price) + "', '" + str(retail_price) + "', '" + str(quantity) + "', '" + str(datetime.datetime.now()) + "', '" + str(vatable) + "');")
			self.connect.begin()
		else:
			print('Product has already been added')


	def update_product(self,name,packaging,per_unit_price):

		"""updates a specific product
		Args:
			name (string): name of the product
			packaging (string): packaging type of the product
			per_unit_price (float): per unit price of the product
		"""

		if self.is_product_available(name,packaging):
			self.cursor.execute("UPDATE `introse`.`inventory` SET `packagingType`='" + str(packaging) + "',`perunitprice`='" + str(per_unit_price) + "', `lastupdated`='" + str(datetime.datetime.now()) + "' WHERE `productName`='" + str(name) + "' and `packagingType`='" + str(packaging) + "';")
			self.connect.begin()
			return True
		else:
			return False	

	def is_product_available(self,name,packaging):

		"""checks if the product exists in the database
		Args:
			name (string): name of the product
		"""

		if self.cursor.execute("SELECT * FROM introse.inventory WHERE productName = '" + name + "' and packagingType = '" + packaging + "'") != 0:
			return True
		else:
			return False		

	def edit_product(self, product_id, name, supplier, packaging, per_unit_price, retail_price, vatable):

		"""edits the current values of the product
		Args:
			product_id (int): id of the product
			name (string): name of the product
			supplier (string): supplier of the product
			packaging (string): packaging type
			per_unit_price (float): unit price
			retail_price (float): retail price of the product
			vatable (boolean): is the product vatable
		"""

		self.cursor.execute("UPDATE `introse`.`inventory` SET `productName`='" + name
			+ "', `supplier`='" + str(supplier)
			+ "', `packagingType`='" + str(packaging)
			+ "', `perunitprice`='" + str(per_unit_price)
			+ "', `retailprice`='" + str(retail_price)
			+ "', `vatable`='" + str(vatable) 
			+ "' WHERE `idinventory`='" 
			+ str(product_id) + "';")

	def add_product_quantity(self, name, packaging, quantity):

		"""add a certain quantity to the product
		Args:
			product (Product): chosen product
			quantity (int): amount to be added

		"""

		if self.is_product_available(name, packaging):
			temp_product = list(filter(lambda x: x.name == name, self.get_product_list()))
			self.cursor.execute("UPDATE `introse`.`inventory` SET `quantity`='" + str((temp_product[0].quantity + quantity)) + "', `lastupdated`='" + str(datetime.datetime.now()) + "' WHERE `productName`='" + str(name) + "' and `packagingType`='" + str(packaging) + "';")
			self.connect.begin()
			return True
		else:
			return False

	def reduce_product_quantity(self, product_id, decrement):
		"""reduce the quantity of a product
		Args:
			product_id (int): id of the product
			decrement (int): reduce product quantity by this number
		"""
		temp_product = list(filter(lambda x: x.id == product_id, self.get_product_list()))
		self.cursor.execute("UPDATE `introse`.`inventory` SET `quantity`='" + str((temp_product[0].quantity - decrement)) + "', `lastupdated`='" + str(datetime.datetime.now()) + "' WHERE `idinventory`='" + str(product_id) + "';")
		self.connect.begin()

class Product:

	"""Represents the products"""

	def __init__(self, id, name, supplier, packaging, per_unit_price, retail_price, quantity, vatable, last_updated):

		"""Constructor
		Args:
			name (string): name of the product
			supplier (string): name of the supplier
			packaging (string): packaging type
			perunitprice (float): price of the product
			retailprice (float): retail price of the product
			quantity (int): amount
			lastupdated (datetime): when was the quantity updated
			vatable (boolean): is vatable
		"""

		self.id = id
		self.name = name
		self.supplier = supplier
		self.packaging = packaging
		self.per_unit_price = per_unit_price
		self.retail_price = retail_price
		self.quantity = quantity
		self.vatable = vatable
		self.last_updated = last_updated


	def __str__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + str(self.per_unit_price) + '\n' + 'Retail Price: ' + str(self.retail_price)

	def __repr__(self):
		return self.name + '\n' + 'Packaging Type: ' + self.packaging + '\n' + 'Unit Price: ' + str(self.per_unit_price) + '\n' + 'Retail Price: ' + str(self.retail_price)

if __name__ == '__main__':
	###open database
	# sample = InventoryDatabase()
	# temp = sample.get_product_list()
	# print(sample.edit_product(20,'water flakes','nestle','plastic',10,10,1))
	# sample.close_connection()
	sample = 'sky flakes, plastic'
	print(sample.split(', '))














