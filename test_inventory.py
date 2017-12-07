import unittest2 as unittest
from InventoryView import *
import time

class test_inventory(unittest.TestCase):

	def test_product_list(self):
		sample = InventoryDatabase()
		self.addTypeEqualityFunc(list,sample.get_product_list())
		sample.close_connection()

	def test_add_product(self):
		sample = InventoryDatabase()
		sample.add_product('coffee','nestle','bottle',10,10,20)
		sample.close_connection()
		sample = InventoryDatabase()
		products = sample.get_product_list()
		product_name = [x.name for x in products]
		self.assertIn('coffee',product_name)
		sample.close_connection()


	def test_add_quantity(self):
		sample = InventoryDatabase()
		product_list = sample.get_product_list()
		sample.add_product_quantity(product_list[0],10)
		sample.close_connection()
		sample = InventoryDatabase()
		products = sample.get_product_list()
		self.assertEqual(product_list[0].quantity+10,products[0].quantity)
		sample.close_connection()		


if __name__ == '__main__':
	unittest.main()