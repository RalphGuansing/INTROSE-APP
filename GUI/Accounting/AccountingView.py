import datetime
import hashlib
import pandas as pd
import pymysql as sql

class Customer:
	"""This Module is responsible for keeping track of Customer's payables."""

	def __init__(self, customer_id, customer_name, accountsreceivables=[]):
		"""This Module is responsible for keeping track of Customer's payables.
		Attributes:
			customer_id (int): The first parameter, contains the id of the customer.
			customer_name ('str'): The second parameter, contains the name of the customer.
			accountsreceivables (list, optional): The third parameter, contains the list of accountsreceivable.
		"""
		self.customer_id = customer_id
		self.customer_name = customer_name
		self.accountsreceivables = accountsreceivables

	def set_all_receivable(self, ar_list):
		self.accountsreceivables = ar_list

	def add_receivable(self, accountsreceivable):
		self.accountsreceivables.append(accountsreceivable)

	def del_receivable(self, index):
		del self.accountsreceivables[index]


class AccountsReceivable:
	"""This Module is responsible for the receivables of customers."""
		
	def __init__(self, customer_id, date, invoice_id, amount, date_paid=None, pr_no=None, payment=None):
		"""This Module is responsible for keeping track of Customer's payables.
		Attributes:
			customer_id (int): The first parameter, contains the id of the customer.
			customer_name ('str'): The second parameter, contains the name of the customer.
			accountsreceivables (list, optional): The third parameter, contains the list of accountsreceivable.
		"""
		self.customer_id = customer_id
		self.date = date
		self.invoice_id = invoice_id
		self.amount = amount
		self.date_paid = date_paid
		self.pr_no = pr_no
		self.payment = payment

	def edit_entry(self, customer_id=None, date=None, invoice_id=None, amount=None, date_paid=None, pr_no=None, payment=None):

		if customer_id != None:
			self.customer_id = customer_id
			self.date = date
		if invoice_id != None:
			self.invoice_id = invoice_id
		if amount != None:
			self.amount = amount
		if date_paid != None:
			self.date_paid = date_paid
		if pr_no != None:
			self.pr_no = pr_no
		if payment != None:
			self.payment = payment

class AccountsPayable:
	"""This Module is responsible for the receivables of customers."""

	def __init__(self, date, name, id_apv, amount, credits=[]):
		self.date = date
		self.name = name
		self.id_apv = id_apv
		self.amount = amount
		self.credits = credits

	def set_credits(self, credits):
		self.credits = credits

	def edit_entry(self, date=None, name=None, id_apv=None, amount=None):
		if date is not None:
			self.date = date
		if name is not None:
			self.name = name
		if id_apv is not None:
			self.id_apv = id_apv
		if amount is not None:
			self.amount = amount

class Credit:
	"""This Module is responsible for the credit of Accounts payable"""
	def __init__(self,id_apv,type_name,type_value):
		self.id_apv = id_apv
		self.type_name = type_name
		self.type_value = type_value

	def edit_entry(self, id_apv=None,type_name=None,type_value=None):
		if id_apv != None:
			self.id_apv = id_apv
		if type_name != None:
			self.type_name = type_name
		if type_value != None:
			self.type_value = type_value



class AccountingDB:
	"""This Module is responsible for storing and editing data in the database."""

	def __init__(self):
		"""Method for loading the database."""
		self.connect = sql.connect('localhost','root','p@ssword','introse',autocommit=True) # change for final db
		self.cursor = self.connect.cursor(sql.cursors.DictCursor)

	def add_accountsreceivable(self, accountsreceivable):
		"""Method for adding accounts receivable to the database.
		Args:
			accountsreceivable (class): The first parameter, is the class of a specific receivable
		"""
		ar = accountsreceivable

		self.cursor.execute("select inv_id from accounts_receivable where inv_id ="+str(ar.invoice_id))

		if self.cursor.fetchone() is None:
			insert_statement = """insert into accounts_receivable
	set customer_id="""+ str(ar.customer_id)+""", date='"""+ ar.date +"""',inv_id = """+ str(ar.invoice_id) +""", amount = """+ str(ar.amount) +""""""

			if ar.payment is not None:
				insert_statement += """, date_paid ='"""+ar.date_paid+"""', pr_id = """+str(ar.pr_no)+""", payment ="""+str(ar.payment)+""" """

			print(insert_statement)
			self.cursor.execute(insert_statement)
		else:
			print("ar exists")

	def update_accountsreceivable(self, accountsreceivable):
		"""Method for updating accounts receivable to the database.
		Args:
			accountsreceivable (class): The first parameter, is the class of a specific receivable
		"""
		ar = accountsreceivable

		update_statement = """update accounts_receivable
		set customer_id=""" + str(ar.customer_id) + """, date='""" + ar.date + """',inv_id = """ + str(
			ar.invoice_id) + """, amount = """ + str(ar.amount) + """"""

		if ar.payment is not None:
			update_statement += """, date_paid ='""" + ar.date_paid + """', pr_id = """ + str(ar.pr_no) + """, payment =""" + str(ar.payment) + """ where inv_id="""+str(ar.invoice_id)

		else:
			update_statement += """ where inv_id="""+str(ar.invoice_id)

		print(update_statement)
		self.cursor.execute(update_statement)

	def delete_accountsreceivable(self, accountsreceivable):
		"""Method for deleting accounts receivable to the database.
		Args:
			accountsreceivable (class): The first parameter, is the class of a specific receivable
		"""

		ar = accountsreceivable

		self.cursor.execute("select inv_id from accounts_receivable where inv_id =" + str(ar.invoice_id))

		if self.cursor.fetchone():
			delete_statement = "delete from accounts_receivable where inv_id=" + str(ar.invoice_id)

			print(delete_statement)
			self.cursor.execute(delete_statement)
		else:
			print("ar does not exists")

	def add_accountspayable(self, accountspayable):
		"""Method for adding accounts payable to the database.
		Args:
			accountspayable (class): The first parameter, is the class of a specific payable
		"""
		ap = accountspayable

		self.cursor.execute("select id_apv from accounts_payable where id_apv ="+str(ap.id_apv))

		if self.cursor.fetchone() is None:
			insert_statement = """insert into accounts_payable set date='"""+ str(ap.date) +"""', name = '"""+str(ap.name)+"""', id_apv ="""+str(ap.id_apv)+""", amount = """+ str(ap.amount) +""" """

			print(insert_statement)
			self.cursor.execute(insert_statement)

			credit_statement = """INSERT INTO credit_type (type_name, id_apv, type_value) Values"""
			tempString1 = ",(SELECT id_apv FROM accounts_payable WHERE id_apv = "

			for i,credit in enumerate(ap.credits):
				credit_statement += "('" + credit.type_name + "'" + tempString1 + str(ap.id_apv) + "), " + str(credit.type_value) + ")"

				if i != len(ap.credits) - 1:
					credit_statement += ",\n"
				else:
					credit_statement += ";"

			print(credit_statement)
			self.cursor.execute(credit_statement)  # Execute

		else:
			print("ap exists")

	def update_accountspayable(self, accountspayable):
		"""Method for updating accounts receivable to the database.
		Args:
			accountspayable (class): The first parameter, is the class of a specific payable
		"""
		ar = accountsreceivable

		update_statement = """update accounts_receivable
		set customer_id=""" + str(ar.customer_id) + """, date='""" + ar.date + """',inv_id = """ + str(
			ar.invoice_id) + """, amount = """ + str(ar.amount) + """"""

		if ar.payment is not None:
			update_statement += """, date_paid ='""" + ar.date_paid + """', pr_id = """ + str(
				ar.pr_no) + """, payment =""" + str(ar.payment) + """ where inv_id="""+str(
			ar.invoice_id)

		print(update_statement)
		self.cursor.execute(update_statement)

	def delete_accountspayable(self, accountspayable_id):
		"""Method for deleting accounts payable to the database.
		Args:
			accountspayable_id (int): The first parameter, is the index of an apv
		"""

		self.cursor.execute("select id_apv from accounts_payable where id_apv =" + str(accountspayable_id))

		if self.cursor.fetchone():
			delete_statement = "delete from accounts_payable where id_apv=" + str(accountspayable_id)

			print(delete_statement)
			self.cursor.execute(delete_statement)
		else:
			print("ap does not exists")

	#RECEIVABLES
	def get_customer_names(self):
		select_statement = "select customer_name from customer"

		self.cursor.execute(select_statement)
		temp = self.cursor.fetchall()
		# print(temp)
		return temp

	#FOR ACCOUNTS RECEIVABLE
	def get_customer_details(self, customer_name):
		select_statement = """select customer_name, address from customer where customer_name = '""" + customer_name + """'"""
		self.cursor.execute(select_statement)
		temp = self.cursor.fetchone()
		return temp

	def get_customer_ar(self, customer_name):
		select_statement = """select DATE_FORMAT(date,'%M %e, %Y') AS Date, inv_id,amount 
	        from accounts_receivable 
	        where customer_id = (select customer_id from customer where customer_name = '""" + customer_name + """') and payment is null"""
		self.cursor.execute(select_statement)
		temp = self.cursor.fetchall()
		return temp

	def get_customer_balance(self, customer_name):

		select_statement = """select sum(amount) as balance 
	        from accounts_receivable 
	        where customer_id = (select customer_id from customer where customer_name = '""" + customer_name + """') and payment is null"""

		self.cursor.execute(select_statement)
		temp = self.cursor.fetchone()
		return temp

	def add_payment_ar(self, dia, main):

		ar_Table = main.ar_Table
		invoice_number = ar_Table.item(ar_Table.currentRow(), 1).text()

		date = dia.tDate.text()
		pr_id = dia.tPR.text()
		payment = dia.tPayment.text()


		update_statement = "UPDATE accounts_receivable SET date_paid ='" + date + "', pr_id= '" + str(pr_id) + "',payment= '" + str(payment) + "' WHERE inv_id= " + str(invoice_number) + ";"
		#print(update_statement)
		self.cursor.execute(update_statement)

	#MONTHLY RECEIVABLES

	def del_payment_ar(self, invoice_number):

		update_statement = "UPDATE accounts_receivable SET date_paid = null, pr_id= null,payment= null WHERE inv_id= " + str(invoice_number) + ";"

		print(update_statement)
		self.cursor.execute(update_statement)

	def get_customer_ar_monthly(self, customer_name, month, year):
		select_statement = """select DATE_FORMAT(date,'%M %e, %Y') AS Date, inv_id,amount,DATE_FORMAT(date_paid,'%M %e, %Y') AS date_paid,pr_id,payment
	        from accounts_receivable 
	        where customer_id = (select customer_id from customer where customer_name = '""" + customer_name + """') and MONTH(Date) = """ + str(
			month) + """ and YEAR(Date) = """ + str(year) + """ """

		self.cursor.execute(select_statement)
		temp = self.cursor.fetchall()
		return temp

	def get_customer_beg_monthly(self, customer_name, month, year):

		if month == 1:
			month = 12
			year = year - 1
		else:
			month = month - 1

		select_statement = """select IFNULL(sum(amount), 0) - IFNULL(sum(payment), 0) as balance
	        from accounts_receivable 
	        where customer_id = (select customer_id from customer where customer_name = '""" + customer_name + """') and Date < '""" + str(
			year) + "-" + str(month) + "-31" + """' """

		self.cursor.execute(select_statement)
		temp = self.cursor.fetchone()
		# print(temp)
		# self.widgetFrame.layout.input_beg_balance(temp)
		# print(select_statement)
		return temp

	def get_customer_end_monthly(self, customer_name, month, year):

		select_statement = """select IFNULL(sum(amount), 0) - IFNULL(sum(payment), 0) as balance
	        from accounts_receivable 
	        where customer_id = (select customer_id from customer where customer_name = '""" + customer_name + """') and Date <= '""" + str(
			year) + "-" + str(month) + "-31" + """' """

		self.cursor.execute(select_statement)
		temp = self.cursor.fetchone()

		return temp

	#PAYABLES

	def get_apv_monthly(self, month, year):

		select_statement = """select DATE_FORMAT(date,'%M %e, %Y') as Date, name, id_apv, amount from accounts_payable where month(date) = """ + str(
			month) + """ and year(date) = """ + str(year) + """ """

		self.cursor.execute(select_statement)
		temp = self.cursor.fetchall()

		return temp

	def get_apv_monthly_total(self, month, year):

		select_statement = """select sum(amount) as total from accounts_payable where month(date) = """ + str(
			month) + """ and year(date) = """ + str(year) + """ """

		self.cursor.execute(select_statement)
		temp = self.cursor.fetchone()

		return temp

	def get_apv_details(self, id_apv):
		select_statement = "select DATE_FORMAT(date,'%M %e, %Y') as Date, name, id_apv, amount from accounts_payable where id_apv =" +str(id_apv)
		self.cursor.execute(select_statement)
		return self.cursor.fetchone()

	def get_apv_columns(self, id_apv):
		select_statement = "select type_name, type_value from credit_type where id_apv =" + str(
			id_apv)
		self.cursor.execute(select_statement)
		return self.cursor.fetchall()
	
	#ADD PAYABLES
	def checkAPV_id(self, id_apv):

		""" returns true if it is able to retrieve something from the database """

		select_statement = "Select * from accounts_payable where id_apv = " + str(id_apv)
		self.cursor.execute(select_statement)
		temp = self.cursor.fetchone()
		# print(temp)
		return temp is None

	def db_add_apv(self, ui_):

		""" Checks if the new APV # is already in the database then inserts  """

		#items = self.widgetFrame.layout.get_items()

		items = ui_.get_items()

		if items["id_apv_BOOL"] and items["amount_BOOL"]:
			if self.checkAPV_id(items["id_apv"]):
				self.apv_execute_statement(items["date"], items["name"], items["id_apv"], items["amount"])
				self.apv_credit_execute_statement(items["column_names"], items["column_val"], items["id_apv"])
			# REMOVE LATER

			# self.close()
			else:
				# SHOW ERROR WINDOW
				print("Duplicate APV ID!")
		else:
			self.showMessage("Error Input", "PLEASE INPUT A NUMBER")

	def apv_execute_statement(self, date, name, id_apv, amount):

		"""Executes the insert statement for apv based on the data inputted by the user"""

		insert_statement = 'INSERT INTO accounts_payable (date, name, id_apv, amount) VALUES ( \'' + date + '\',\'' + name + '\',\'' + str(
			id_apv) + '\',\'' + str(amount) + '\');'
		print(insert_statement)
		self.cursor.execute(insert_statement)  # Execute

	def apv_credit_execute_statement(self, column_names, column_val, id_apv):

		credit_statement = """INSERT INTO credit_type (type_name, id_apv, type_value)
	                              Values"""
		tempString1 = ",(SELECT id_apv FROM accounts_payable WHERE id_apv = "

		for i in range(len(column_names)):
			credit_statement += "('" + column_names[i] + "'" + tempString1 + str(id_apv) + "), " + str(
				column_val[i]) + ")"

			if i != len(column_names) - 1:
				credit_statement += ",\n"
			else:
				credit_statement += ";"

		print(credit_statement)
		self.cursor.execute(credit_statement)  # Execute


	def add_group_name(self, groupName):
		insert_statement = "INSERT INTO column_group SET group_name = '" + groupName + "'"
		self.cursor.execute(insert_statement)

	def checkDupe(self, name, num):
		""" This Function Checks if the a name of a Column/Group has a duplicate

            Returns: False if it has a Duplicate, True if unique
        """
		# num = 0 if Column Name
		# num = 1 if Group Name

		if num == 0:
			select_statement = """select id_column
	                            from column_name_table
	                            where column_name = '""" + name + """'"""

		if num == 1:
			select_statement = """select id_group
	                            from column_group
	                            where group_name = '""" + name + """'"""
		if select_statement:
			self.cursor.execute(select_statement)
			temp = self.cursor.fetchone()
			return temp is None

	def add_column_to_group(self, groupName, columnName):
		insert_statement = """ INSERT INTO column_name_table
	           SET column_name = '""" + columnName + """',
	                id_group = (
	               SELECT id_group
	                 FROM column_group
	                WHERE group_name = '""" + groupName + """' )"""

		#print(insert_statement)
		self.cursor.execute(insert_statement)  # Execute

	def get_column_choices(self):
		columns = {}
		group_statement = "select group_name from column_group"
		self.cursor.execute(group_statement)
		tempvar = self.cursor.fetchall()
		temp = [row["group_name"] for row in tempvar]
		# print(temp)
		columns["groups"] = temp

		name_statement = """select g.group_name as 'group', n.column_name as 'name'
	                        from column_group as g, column_name_table as n
	                        where g.id_group = n.id_group"""
		self.cursor.execute(name_statement)
		temp = self.cursor.fetchall()
		# print(temp)
		columns["names"] = temp

		return columns

	def get_column_groups(self):
		group_statement = "select group_name from column_group"
		self.cursor.execute(group_statement)
		tempvar = self.cursor.fetchall()
		temp = [row["group_name"] for row in tempvar]
		# print(temp)
		return temp

	def login(self, username, encoded_plaintext):
		sha = hashlib.sha1(encoded_plaintext)
		password = sha.hexdigest()

		select_statement = """select employee_id, username, concat(first_name, ' ' , last_name) as full_name
	        from employee
	        where username = '""" + username + """' and password = '""" + password + """'"""

		print(select_statement)
		self.cursor.execute(select_statement)

		tempvar = self.cursor.fetchone()
		return tempvar

	def close_connection(self):
			"""Method for closing the database."""
			self.connect.close()
