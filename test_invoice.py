import unittest2 as unittest
from InvoiceView import *

class test_inventory(unittest.TestCase):

	def test_add_invoice(self):
		invo_db = InvoiceDB()
		comp = []
		comp_item = Component("Jolispag", 49, 59, 30, "mL")
		comp.append(comp_item)
		comp_item = Component("Jolichiken", 59, 69, 20, "mL")
		comp.append(comp_item)
		invo_db.add_invoice(990,200,15,300, 100, "Hericho", datetime.datetime.now(), "30 Days", datetime.datetime.now() + datetime.timedelta(days=30), "Fanalili", comp)
		invo_db.close_connection()

	def test_update_value(self):
		invo_db = InvoiceDB()
		invo_query = invo_db.get_query(23)
		invo_components = []
		last_invoice = invo_db.get_lastid()
		for component in invo_query[11]:
			temp_comp = Component(invo_query[2],invo_query[5],invo_query[6],invo_query[4],invo_query[3], id_comp=invo_query[0], nonvat=invo_query[8])
			if temp_comp.id == 28:
				temp_comp.edit_entry(25, 0)
			invo_components.append(temp_comp)
		invo_db.update_value(23, invo_components)
		invo_db.close_connection()

	def test_delete_row(self):
		invo_db = InvoiceDB()
		last_invoice = invo_db.get_lastid()
		invo_db.delete_row(invoice_number=last_invoice)
		invo_db.close_connection()

if __name__ == '__main__':
	unittest.main()
