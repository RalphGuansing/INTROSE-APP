import datetime

class Bookkeep:
	"""This Module is responsible for keeping track of purchases of clients.
	Attributes:
		__totalinvoice (float): Contains total value of purchase without tax reduction.
		__totalnvat (float): Contains total value that is not included in tax reduction.
		__totaltaxable (float): Contains total value of purchase reduced by tax.
		__totaloptax (float): Contains total output tax.
		__totalcommission (float): Contains total commission of employees.
		__currdate (:obj: 'datetime'): Contains the current date.
	"""
	__totalinvoice = 0
	__totalnvat = 0
	__totaltaxable = 0 
	__totaloptax = 0
	__totalcommission = 0
	__currdate = datetime.datetime.now()
		
	def __init__(self, amount=0, nonvat=0, innumber=0, cust="Walk-in", ddate=datetime.datetime.now(), seller=None, quota=0 ):
		"""Method for initialization of values.
		Args:
			amount (float, optional): The first parameter, value of purchase without tax reduction, defaults to 0.
			nonvat (float, optional): The second parameter, value that is not included in tax reduction, defaults to 0.
			innumber (float, optional): The third parameter, invouice number of Customer, defaults to 0.
			cust (:obj: 'str', optional): The fourth parameter, name of Customer, defaults to "Walk-in".
			ddate (:obj:, 'datetime', optional): The fifth parameter, due date of purchase, defaults to current date.
			seller (:obj:, 'str', optional): The sixth parameter, name of employee that handled purchase, defaults to None.
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
			commission = round((quota - amount) / 0.02, 2)
			self.commission = commission
		else:
			self.commission = 0
		Bookkeep.settotal(self.amount, self.nonvat, self.taxable, self.optax, self.commission)

	def cancelled(self):
		"""Method for cancellation of purchase, replaces all attributes to None excepter innumber
			and subtracts value from total invoice, nonvat, taxble, output tax and commission.
		"""
		Bookkeep.__totalinvoice -= self.amount
		Bookkeep.__totalnvat -= self.nonvat
		Bookkeep.__totaltaxable -= self.taxable
		Bookkeep.__totaloptax -= self.optax
		Bookkeep.__totalcommission -= self.commission
		self.amount = None
		self.nonvat = None
		self.cust = None
		self.ddate = None
		self.taxable = None
		self.optax = None
		self.seller = None
		self.commission = None

	def resettot(self):
		"""Method for resetting all total values to 0."""
		Bookkeep.__totalinvoice = 0
		Bookkeep.__totalnvat = 0
		Bookkeep.__totaltaxable = 0
		Bookkeep.__totaloptax = 0
		Bookkeep.__totalcommission = 0

	def checkddate(self):
		"""Method for checking the due date and notification."""
		if Bookkeep.__currdate.day == self.ddate.day - 1:
			print("pop-up notice gui")
		# 	output gui here #


		# 				    #
		pass

	def report(self):
		"""Method for creation of monthly report."""
		if Bookkeep.__currdate.day == 1:
			print("generate report and reset value")
		# 	print total and reset total
		# 	if possible create excel of total per month w/graph
		pass
		
	def settotal(amount, nonvat, taxable, optax, commission):
		"""Method for setting the total invoice, nonvat, taxble, output tax and commission.
		Args:
			amount (float): The first parameter, value of purchase without tax reduction.
			nonvat (float): The second parameter, value that is not included in tax reduction.
			taxable (float): The third parameter, value of purchase reduced by tax.
			optax (float): The fourth parameter, value of output tax.
			commission (float): The fifth parameter, value of commission of the employee.
		"""
		Bookkeep.__totalinvoice += amount
		Bookkeep.__totalnvat += nonvat
		Bookkeep.__totaltaxable += taxable
		Bookkeep.__totaloptax += optax
		Bookkeep.__totalcommission += commission

	def gettotal(self):
		"""Method for returning the total invoice, nonvat, taxble, output tax and commission.

		Returns:
			[__totalinvoice, __totalnvat, __totaltaxable, __totaloptax, __totalcommission]
		"""
		return Bookkeep.__totalinvoice, Bookkeep.__totalnvat, Bookkeep.__totaltaxable, Bookkeep.__totaloptax, Bookkeep.__totalcommission
