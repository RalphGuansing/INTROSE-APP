import datetime
import pandas as pd
import pymysql as sql

class Invoice:
	"""This Module is responsible for keeping track of purchases of clients.
	Attributes:
		__totalinvoice (float): Contains total value of purchase without tax reduction.
		__totalnvat (float): Contains total value that is not included in tax reduction.
		__totaltaxable (float): Contains total value of purchase reduced by tax.
		__totaloptax (float): Contains total output tax.
		__totalcommission (float): Contains total commission of employees.
	"""
	__totalinvoice = 0
	__totalnvat = 0
	__totaltaxable = 0 
	__totaloptax = 0
	__totalcommission = 0
		
	def __init__(self, amount=0, nonvat=0, innumber=0, cust="Walk-in", ddate=datetime.datetime.now(), seller="LCG", quota=0):
		"""Method for initialization of values.
		Args:
			amount (float, optional): The first parameter, value of purchase without tax reduction, defaults to 0.
			nonvat (float, optional): The second parameter, value that is not included in tax reduction, defaults to 0.
			innumber (float, optional): The third parameter, invouice number of Customer, defaults to 0.
			cust (:obj: 'str', optional): The fourth parameter, name of Customer, defaults to "Walk-in".
			ddate (:obj:, 'datetime', optional): The fifth parameter, due date of purchase, defaults to current date.
			seller (:obj:, 'str', optional): The sixth parameter, name of employee that handled purchase, defaults to "LCG".
			quota (float, optional): The seventh parameter, quota of the employee, defaults to 0.
		"""
		self.amount = amount
		self.nonvat = nonvat
		self.innumber = innumber
		self.cust = cust
		self.ddate = ddate
		self.seller = seller
		self.taxable = round((amount - nonvat) /1.12, 2)
		self.optax = round(self.taxable * 0.12, 2)
		if quota > amount:
			self.commission = round((quota - amount) / 0.02, 2)
		else:
			self.commission = 0
		Bookkeep.settotal(self.amount, self.nonvat, self.taxable, self.optax, self.commission, False)

	def cancelled(self):
		"""Method for cancellation of purchase, replaces all attributes to None except innumber
			and subtracts value from total invoice, nonvat, taxble, output tax and commission.
		"""
		Bookkeep.settotal(self.amount, self.nonvat, self.taxable, self.optax, self.commission, True)
		self.amount = None
		self.nonvat = None
		self.cust = None
		self.ddate = None
		self.taxable = None
		self.optax = None
		self.seller = None
		self.commission = None

	def edit_entry(self, amount=None, nonvat=None, cust=None, ddate=None, seller="LCG", quota=None):
		"""Method for editing the values.
		Args:
			amount (float, optional): The first parameter, value of purchase without tax reduction, defaults to None.
			nonvat (float, optional): The second parameter, value that is not included in tax reduction, defaults to None.
			cust (:obj: 'str', optional): The third parameter, name of Customer, defaults to None.
			ddate (:obj:, 'datetime', optional): The fourth parameter, due date of purchase, defaults to None.
			seller (:obj:, 'str', optional): The fifth parameter, name of employee that handled purchase, defaults to "LCG".
			quota (float, optional): The sixth parameter, quota of the employee, defaults to None.
		"""
		if cust != None:
			self.cust = cust
		if seller != None:
			self.seller = seller
		if ddate != None:
			self.ddate = ddate
		if amount != None:
			Bookkeep.settotal(self.amount, self.nonvat, self.taxable, self.optax, self.commission, True)
			self.amount = amount
			if nonvat != None:
				self.nonvat = nonvat
				self.taxable = round((amount - nonvat) /1.12, 2)
				self.optax = round(self.taxable * 0.12, 2)
		if quota != None:
			if quota > self.amount:
				self.commission = round((quota - amount) / 0.02, 2)
			else:
				self.commission = 0
		Bookkeep.settotal(self.amount, self.nonvat, self.taxable, self.optax, self.commission, False)

	@classmethod
	def set_total(cls, amount, nonvat, taxable, optax, commission, value):
		"""Method for setting the total invoice, nonvat, taxble, output tax and commission.
		Args:
			amount (float): The first parameter, value of purchase without tax reduction.
			nonvat (float): The second parameter, value that is not included in tax reduction.
			taxable (float): The third parameter, value of purchase reduced by tax.
			optax (float): The fourth parameter, value of output tax.
			commission (float): The fifth parameter, value of commission of the employee.
			value (bool): The sixth parameter, true if decrementing the values, else incrementing the values
		"""
		if value:
			Bookkeep.__totalinvoice -= amount
			Bookkeep.__totalnvat -= nonvat
			Bookkeep.__totaltaxable -= taxable
			Bookkeep.__totaloptax -= optax
			Bookkeep.__totalcommission -= commission
		else:
			Bookkeep.__totalinvoice += amount
			Bookkeep.__totalnvat += nonvat
			Bookkeep.__totaltaxable += taxable
			Bookkeep.__totaloptax += optax
			Bookkeep.__totalcommission += commission
				
	@classmethod
	def get_total(cls):
		"""Method for returning the total invoice, nonvat, taxble, output tax and commission.
		Returns:
			[__totalinvoice, __totalnvat, __totaltaxable, __totaloptax, __totalcommission]
		"""
		return Bookkeep.__totalinvoice, Bookkeep.__totalnvat, Bookkeep.__totaltaxable, Bookkeep.__totaloptax, Bookkeep.__totalcommission

class InvoiceDB:
	"""This Module is responsible for storing and editing data in the database."""

	def __init__(self):
		"""Method for loading the database."""
		self.connect = sql.connect('localhost','root','p@ssword','lcg_db',autocommit=True) # change for final db
		self.cursor = self.connect.cursor()

	def add_invoice(self, amount, nonvat, vat, taxable, cust, ddate, seller, components):
		"""Method for adding invoice to the database.
		Args:
			amount (float): The first parameter, value of purchase without tax reduction.
			nonvat (float): The second parameter, value that is not included in tax reduction.
			vat (float): The third parameter, computed tax of the invoice.
			taxable (float): The fourth parameter, computed amount after tax.
			cust (:obj: 'str'): The fifth parameter, name of Customer.
			ddate (:obj:, 'datetime'): The sixth parameter, due date of purchase.
			seller (:obj:, 'str'): The seventh parameter, name of employee that handled purchase.
			components (:obj:, 'list'): The eight parameter, list of components.
		"""
		sql_statement = pd.read_sql("SELECT idclient FROM lcg_db.client WHERE client_name = '" + cust + "' ;",self.connect)
		client_id = sql_statement.idclient[0]
		sql_statement = pd.read_sql("SELECT idagent FROM lcg_db.agent WHERE agent_name = '" + seller + "' ;",self.connect)
		seller_id = sql_statement.idagent[0]
		sql_statement = "INSERT INTO `lcg_db`.`invoice` (`invoice_buyer`, `invoice_seller`, `invoice_date`, `invoice_term`, `invoice_ddate`,`invoice_amount`, `invoice_nonvat`, `invoice_vat`, `invoice_taxable`) VALUES ('" + str(client_id) + "', '" + str(seller_id) + "', '" + str(datetime.datetime.now()) + "', '""30 Days""', '" + str(ddate) + "', '" + str(amount) + "', '" + str(nonvat) + "', '" + str(vat) + "', '" + str(taxable) + "');"
		self.cursor.execute(sql_statement)
		l_id = InvoiceDB.get_lastid(self)
		for component in components:
			sql_statement = "INSERT INTO `lcg_db`.`component` (`component_invoicenum`, `component_name`, `component_quantity`, `component_origprice`, `component_unitprice`) VALUES ('" + str(l_id) + "', '" + str(component.name) + "', '" + str(component.quantity) + "', '"+ str(component.origprice) +"', '" + str(component.unitprice) + "');"
			self.cursor.execute(sql_statement)

	def update_value(self, invoice_number, amount, nonvat, vat, taxable):
		"""Method for updating entries in the database.
		Args:
			invoice_number (int): The first parameter, the invoice number of the record to be updated.
			amount (float): The second parameter, value of purchase without tax reduction.
			nonvat (float): The third parameter, value that is not included in tax reduction.
			vat (float): The fourth parameter, computed tax of the invoice.
			taxable (float): The fifth parameter, computed amount after tax.
		"""
		sql_statement = "UPDATE `lcg_db`.`invoice` SET `invoice_amount`='" + str(amount) + "', `invoice_nonvat`= '" + str(nonvat) + "',`invoice_vat`= '" + str(vat) + "',`invoice_taxable`='" + str(taxable) + "' WHERE `idinvoice`='" + str(invoice_number) + "';"
		self.cursor.execute(sql_statement)
	
	def delete_row(self, invoice_number):
		"""Method for deleting an entire row in the database.
		Args:
			invoice_number (int): The first parameter, the invoice number of the record to be deleted.
		"""
		sql_statement = "DELETE FROM `lcg_db`.`invoice` WHERE `idinvoice`='" + str(invoice_number) + "';"
		self.cursor.execute(sql_statement)

	def get_total(self):
		"""Method for getting the total amount, nonvat, vat, and taxable from the database.
		Returns:
				[total_amount, total_nonvat, total_vat, total_taxable]

		"""
		sql_statement = pd.read_sql("SELECT invoice_amount, invoice_nonvat, invoice_vat, invoice_taxable FROM lcg_db.invoice;",self.connect)
		return [sql_statement.invoice_amount.sum(), sql_statement.invoice_nonvat.sum(), sql_statement.invoice_vat.sum(), sql_statement.invoice_taxable.sum()]

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
				(idinvoice, invoice_buyer, invoice_seller, invoice_date, invoice_term, invoice_ddate, invoice_amount, invoice_nonvat, invoice_vat, invoice_taxable)
		"""
		sql_statement = pd.read_sql("SELECT * FROM lcg_db.invoice WHERE idinvoice = '" + str(invoice_number) + "';", self.connect)
		invoice_query = [(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7], row[1][8], row[1][9]) for row in sql_statement.iterrows()]
		client_name = InvoiceDB.get_clientname(self, invoice_query[0][1])
		seller_name = InvoiceDB.get_sellername(self, invoice_query[0][2])
		return [invoice_query[0][0], client_name, seller_name, invoice_query[0][3], invoice_query[0][4], invoice_query[0][5], invoice_query[0][6], invoice_query[0][7], invoice_query[0][8], invoice_query[0][9]]

	def close_connection(self):
		"""Method for closing the database."""
		self.connect.close()

class Component:
	"""This Module is responsible for the components in an invoice."""
	def __init__(self, name, origprice, unitprice, quantity):
		"""Method for initialization of values.
		Args:
			name (:obj:, 'str'): The first parameter, name of the component.
			origprice (float): The second parameter, original price of the component.
			unitprice (float): The third parameter, new price of the component.
			quantity (int): The fourth parameter, quantity of the component.
		"""
		self.name = name
		self.origprice = origprice
		self.unitprice = unitprice
		self.quantity = quantity