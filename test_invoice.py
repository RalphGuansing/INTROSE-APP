import unittest2 as unittest
from InvoiceView import *

class test_inventory(unittest.TestCase):

	def test_add_invoice(self):
		invo_db = InvoiceDB()
		comp = []
		comp_item = Component("Jolispag", 49, 59, 30)
		comp.append(comp_item)
		comp_item = Component("Jolichiken", 59, 69, 20)
		comp.append(comp_item)
		invo_db.add_invoice(990,200,15,300, 100, "Hericho", datetime.datetime.now(), "30 Days", datetime.datetime.now() + datetime.timedelta(days=30), "Fanalili", comp)
		invo_db.close_connection()

	def test_update_value(self):
		invo_db = InvoiceDB()
		last_invoice = invo_db.get_lastid()
		invo_db.update_value(last_invoice, 660, 120, 20, 250, 265)
		invo_db.close_connection()

	def test_delete_row(self):
		invo_db = InvoiceDB()
		last_invoice = invo_db.get_lastid()
		invo_db.delete_row(last_invoice)
		invo_db.close_connection()

if __name__ == '__main__':
	unittest.main()
