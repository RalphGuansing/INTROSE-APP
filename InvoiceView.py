import datetime
import pandas as pd
import pymysql as sql

class Invoice:
	"""This Module is responsible for keeping track of purchases of clients."""

	def __init__(self, cust="Walk-in", issue_date=datetime.datetime.now(),terms=None, seller="LCG"):
		"""Method for initialization of values.
		Args:
			cust (:obj: 'str', optional): The first parameter, name of Customer, defaults to "Walk-in".
			issue_date (:obj:, 'datetime', optional): The second parameter, date of issuance of invoice, defaults to current date.
			terms (:obj: ,'str' optional): The third parameter, terms of the invoice, defaults to None.
			seller (:obj:, 'str', optional): The fourth parameter, name of employee that handled purchase, defaults to "LCG".
		"""
		self.cust = cust
		self.issue_date = issue_date
		self.terms = terms
		if terms == "30 Days":
			self.ddate = issue_date + datetime.deltatime(days=30)
		elif terms == "60 Days":
			self.ddate = issue_date + datetime.deltatime(days=60)
		elif terms == "90 Days":
			self.ddate = issue_date + datetime.deltatime(days=90)
		elif terms == "1 year":
			self.ddate = issue_date + datetime.deltatime(days=365)
		self.seller = seller

class InvoiceDB:
	"""This Module is responsible for storing and editing data in the database."""

	def __init__(self):
		"""Method for loading the database."""
		self.connect = sql.connect('localhost','root','p@ssword','lcg_db',autocommit=True) # change for final db
		self.cursor = self.connect.cursor()

	def add_invoice(self, cust, issue_date, terms, ddate, seller, components):
		"""Method for adding invoice to the database.
		Args:
			cust (:obj: 'str'): The first parameter, name of Customer.
			issue_date (:obj:, 'datetime'): The second parameter, date of issuance of invoice, defaults to current date.
			terms (:obj: 'str') The third parameter, terms of the invoice
			ddate (:obj:, 'datetime'): The fourth parameter, due date of purchase.
			seller (:obj:, 'str'): The fifth parameter, name of employee that handled purchase.
			components (:obj:, 'list'): The sixth parameter, list of components.
		"""
		total_amount = total_nonvat = total_vat = total_taxable = total_profit = 0
		sql_statement = pd.read_sql("SELECT idclient FROM lcg_db.client WHERE client_name = '" + cust + "' ;",self.connect)
		client_id = sql_statement.idclient[0]
		sql_statement = pd.read_sql("SELECT idagent FROM lcg_db.agent WHERE agent_name = '" + seller + "' ;",self.connect)
		seller_id = sql_statement.idagent[0]
		for component in components:
			total_amount += component.amount
			total_nonvat += component.nonvat
			total_vat += component.vat
			total_taxable += component.taxable
			total_profit += component.profit
		sql_statement = "INSERT INTO `lcg_db`.`invoice` (`invoice_buyer`, `invoice_seller`, `invoice_date`, `invoice_term`, `invoice_ddate`,`invoice_amount`, `invoice_nonvat`, `invoice_vat`, `invoice_taxable`, `invoice_profit`) VALUES ('" + str(client_id) + "', '" + str(seller_id) + "', '" + str(issue_date) + "', '" + terms + "', '" + str(ddate) + "', '" + str(total_amount) + "', '" + str(total_nonvat) + "', '" + str(total_vat) + "', '" + str(total_taxable) + "', '" + str(total_profit) + "');"
		self.cursor.execute(sql_statement)
		l_id = InvoiceDB.get_last_id(self)
		for component in components:
			sql_statement = "INSERT INTO `lcg_db`.`component` (`component_invoicenum`, `component_name`, `component_unit`, `component_quantity`, `component_origprice`, `component_unitprice`, `component_amount`, `component_nonvat`, `component_vat`, `component_taxable`, `component_profit`) VALUES ('" + str(l_id) + "', '" + str(component.name) + "', '" + str(component.unit) + "', '" + str(component.quantity) + "', '"+ str(component.origprice) +"', '" + str(component.unitprice) + "', '" + str(component.amount) + "', '" + str(component.nonvat) + "', '" + str(component.vat) + "', '" + str(component.taxable) + "', '" + str(component.profit) + "');"
			self.cursor.execute(sql_statement)

	def update_value(self, invoice_number, components):
		"""Method for updating entries in the database.
		Args:
			invoice_number (int): The first parameter, the invoice number of the record to be updated.
			components (:obj:, 'list'): The second parameter, list of components.
		"""
		# if delete elemment all values are 0 to deleter row
		# loop tru components then update

		# loop agen for total for invoice
		total_amount = total_nonvat = total_vat = total_taxable = total_profit = 0
		for component in components:
			total_amount += component.amount
			total_nonvat += component.nonvat
			total_vat += component.vat
			total_taxable += component.taxable
			total_profit += component.profit
			if component.quantity == 0:
				InvoiceDB.delete_row(self,component_number=component.id)
			else:
				sql_statement = "UPDATE `lcg_db`.`component` SET `component_quantity`='" + str(component.quantity) + "', `component_amount`='" + str(component.amount) + "', `component_nonvat`='" + str(component.nonvat) + "', `component_vat`='" + str(component.vat) + "', `component_taxable`='" + str(component.taxable) + "', `component_profit`='" + str(component.profit) + "' WHERE `idcomponent`= '" + str(component.id) + "';"
				self.cursor.execute(sql_statement)

		sql_statement = "UPDATE `lcg_db`.`invoice` SET `invoice_amount`='" + str(total_amount) + "', `invoice_nonvat`= '" + str(total_nonvat) + "',`invoice_vat`= '" + str(total_vat) + "',`invoice_taxable`='" + str(total_taxable) + "',`invoice_profit`='" + str(total_profit) + "' WHERE `idinvoice`='" + str(invoice_number) + "';"
		self.cursor.execute(sql_statement)
	
	def delete_row(self, invoice_number=0, component_number=0):
		"""Method for deleting an entire row in the database.
		Args:
			invoice_number (int): The first parameter, the invoice number of the record to be deleted, defaults to 0.
			component_number (int): The second parameter, the component number of the record to be deleted, defaults to 0.
		"""
		if invoice_number != 0:
			sql_statement = "DELETE FROM `lcg_db`.`invoice` WHERE `idinvoice`='" + str(invoice_number) + "';"
			self.cursor.execute(sql_statement)
		if component_number != 0:
			sql_statement = "DELETE FROM `lcg_db`.`component` WHERE `idcomponent`='" + str(component_number) + "';"
			self.cursor.execute(sql_statement)

	def get_total(self):
		"""Method for getting the total amount, nonvat, vat, and taxable from the database.
		Returns:
				[total_amount, total_nonvat, total_vat, total_taxable, total_profit]

		"""
		sql_statement = pd.read_sql("SELECT invoice_amount, invoice_nonvat, invoice_vat, invoice_taxable, invoice_profit FROM lcg_db.invoice;",self.connect)
		return [sql_statement.invoice_amount.sum(), sql_statement.invoice_nonvat.sum(), sql_statement.invoice_vat.sum(), sql_statement.invoice_taxable.sum(), sql_statement.invoice_profit.sum()]

	def get_client_name(self, client_id=None):
		"""Method for getting the client names from the database.
		Args:
			client_id (int, optional): The first parameter, checks if looking for specific client, defaults to None.
		Returns:
				[client_name], if seller_id is None
				client_name, if otherwise
		"""
		if client_id == None:
			sql_statement = pd.read_sql("SELECT client_name, client_address FROM lcg_db.client ORDER BY client_name;",self.connect)
			return [(row[1][0], row[1][1]) for row in sql_statement.iterrows()]
		else:
			sql_statement = pd.read_sql("SELECT client_name, client_address FROM lcg_db.client WHERE idclient = '" + str(client_id) + "';",self.connect)
			return sql_statement.client_name[0]

	def get_seller_name(self, seller_id=None):
		"""Method for getting the client names from the database.
		Args:
			seller_id (int, optional): The first parameter, checks if looking for specific seller, defaults to None.
		Returns:
				[seller_name], if seller_id is None
				seller_name, if otherwise
		"""
		if seller_id == None:
			sql_statement = pd.read_sql("SELECT agent_name FROM lcg_db.agent ORDER BY agent_name;",self.connect)
			return [row[1][0] for row in sql_statement.iterrows()]
		else:
			sql_statement = pd.read_sql("SELECT agent_name FROM lcg_db.agent WHERE idagent = '" + str(seller_id) + "' ;",self.connect)
			return sql_statement.agent_name[0]

	def get_last_id(self):
		"""Method for getting the recent id from the database.
		Returns:
				idinvoice
		"""
		sql_statement = pd.read_sql("SELECT idinvoice FROM lcg_db.invoice ORDER BY idinvoice DESC;",self.connect)
		return sql_statement.idinvoice[0]

	def get_query(self, invoice_number):
		"""Method for getting the query of invoice number from the database.
		Args:
			invoice_number (int): The first parameter, invoice number to be searched.
		Returns:
				(idinvoice, invoice_buyer, invoice_seller, invoice_date, invoice_term, invoice_ddate, invoice_amount, invoice_nonvat, invoice_vat, invoice_taxable, invoice_profit, component)
		"""
		sql_statement = pd.read_sql("SELECT * FROM lcg_db.invoice WHERE idinvoice = '" + str(invoice_number) + "';", self.connect)
		invoice_query = [(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7], row[1][8], row[1][9], row[1][10]) for row in sql_statement.iterrows()]
		sql_statement2 = pd.read_sql("SELECT * FROM lcg_db.component WHERE component_invoicenum = '" + str(invoice_number) + "';", self.connect)
		invoice_query2 = [(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7], row[1][8], row[1][9], row[1][10], row[1][11]) for row in sql_statement2.iterrows()]
		client_name = InvoiceDB.get_client_name(self, invoice_query[0][1])
		seller_name = InvoiceDB.get_seller_name(self, invoice_query[0][2])
		return [invoice_query[0][0], client_name, seller_name, invoice_query[0][3], invoice_query[0][4], invoice_query[0][5], invoice_query[0][6], invoice_query[0][7], invoice_query[0][8], invoice_query[0][9], invoice_query[0][10], invoice_query2]

	def close_connection(self):
		"""Method for closing the database."""
		self.connect.close()

class Component:
	"""This Module is responsible for the components in an invoice.
	Attributes:
		__totalinvoice (float): Contains total value of purchase without tax reduction.
		__totalnvat (float): Contains total value that is not included in tax reduction.
		__totaltaxable (float): Contains total value of purchase reduced by tax.
		__totalvat (float): Contains total output tax.
		__totalprofit (float): Contains total profit.
	"""
	__totalinvoice = 0
	__totalnvat = 0
	__totaltaxable = 0 
	__totalvat = 0
	__totalprofit = 0

	def __init__(self, name, origprice, unitprice, quantity, unit, id_comp=0, nonvat=0):
		"""Method for initialization of values.
		Args:
			name (:obj:, 'str'): The first parameter, name of the component.
			origprice (float): The second parameter, original price of the component.
			unitprice (float): The third parameter, new price of the component.
			quantity (int): The fourth parameter, quantity of the component.
			unit (:obj:, 'str'): The fifth parameter, unit of measure of the component.
			id_comp (int, optional): The sixth parameter, id of the component, defaults to 0.
			nonvat (float, optional): The seventh parameter, nonvat of the component, defaults to 0.
		"""
		self.id = id_comp
		self.name = name
		self.origprice = origprice
		self.unitprice = unitprice
		self.quantity = quantity
		self.unit = unit
		self.amount = quantity * unitprice
		self.nonvat = nonvat
		self.taxable = round((self.amount - self.nonvat) /1.12, 2)
		self.vat = round(self.taxable * 0.12, 2)
		self.profit = self.taxable - self.origprice
		Component.set_total(self.amount, self.nonvat, self.taxable, self.vat, self.profit, False)

	def cancelled(self):
		"""Method for cancellation of purchase, replaces all attributes to None except innumber
			and subtracts value from total invoice, nonvat, taxble, output tax and commission.
		"""
		Component.set_total(self.amount, self.nonvat, self.taxable, self.vat, self.profit, True)
		self.quantity = 0
		self.amount = 0
		self.nonvat = 0
		self.taxable = 0
		self.vat = 0
		self.profit = 0

	def edit_entry(self, quantity, nonvat=0):
		"""Method for editing the values.
		Args:
			quantity (int): The first parameter, quantity of the component.
			nonvat (float, optional): The second parameter, nonvat of the component, defaults to 0.
		"""
		Component.set_total(self.amount, self.nonvat, self.taxable, self.vat, self.profit, True)
		self.quantity = quantity
		self.amount = quantity * self.unitprice
		self.nonvat = nonvat
		self.taxable = round((self.amount - self.nonvat) /1.12, 2)
		self.vat = round(self.taxable * 0.12, 2)
		if self.taxable == 0:
			self.profit = 0
		else:
			self.profit = self.taxable - self.origprice
		Component.set_total(self.amount, self.nonvat, self.taxable, self.vat, self.profit, False)

	@classmethod
	def set_total(cls, amount, nonvat, taxable, vat, profit, value):
		"""Method for setting the total amount, nonvat, taxble, and output tax.
		Args:
			amount (float): The first parameter, value of purchase without tax reduction.
			nonvat (float): The second parameter, value that is not included in tax reduction.
			taxable (float): The third parameter, value of purchase reduced by tax.
			vat (float): The fourth parameter, value of output tax.
			profit (float): The fifth parameter, profit from invoice.
			value (bool): The sixth parameter, true if decrementing the values, else incrementing the values
		"""
		if value:
			Component.__totalinvoice -= amount
			Component.__totalnvat -= nonvat
			Component.__totaltaxable -= taxable
			Component.__totalvat -= vat
			Component.__totalprofit -= profit
		else:
			Component.__totalinvoice += amount
			Component.__totalnvat += nonvat
			Component.__totaltaxable += taxable
			Component.__totalvat += vat
			Component.__totalprofit += profit
				
	@classmethod
	def get_total(cls):
		"""Method for returning the total invoice, nonvat, taxble, output tax and commission.
		Returns:
			[__totalinvoice, __totalnvat, __totaltaxable, __totalvat, __totalprofit]
		"""
		return Component.__totalinvoice, Component.__totalnvat, Component.__totaltaxable, Component.__totalvat, Component.__totalprofit
