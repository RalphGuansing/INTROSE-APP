import datetime

class Bookkeep:
	totalinvoice = 0 ## will update every transaction
	totalvat = 0
	totaltaxable = 0 
	totalnvat = 0 ##
	currdate = datetime.datetime.now() - datetime.timedelta(days=3) #will update everyday, date will be placed at driver
		
	def __init__(self, amount=0, nonvat=0, innumber=0, cust="Walk-in", ddate=datetime.datetime.now()): #get values from inputs or db
		self.amount = amount
		self.nonvat = nonvat
		self.innumber = innumber
		self.cust = cust
		self.ddate = ddate
		
		# print(Bookkeep.currdate.day)
		# Bookkeep.report(self)
		# Bookkeep.checkddate(self)

		self.taxable = round((amount - nonvat) /1.12, 2)
		self.nvat = round(self.taxable * 0.12, 2)
		
		Bookkeep.totalinvoice += amount
		Bookkeep.totalvat += self.nvat
		Bookkeep.totaltaxable += self.taxable
		Bookkeep.totaltaxable += self.nonvat


	def cancelled(self):
		Bookkeep.totalinvoice -= amount
		Bookkeep.totalvat -= self.nvat
		Bookkeep.totaltaxable -= self.taxable
		Bookkeep.totaltaxable -= self.nonvat
		self.amount = None
		self.nonvat = None
		self.cust = None
		self.ddate = None
		self.taxable = None
		self.nvat = None

	def resettot(self):
		Bookkeep.totalinvoice = 0
		Bookkeep.totalvat = 0
		Bookkeep.totaltaxable = 0
		Bookkeep.totaltaxable = 0

	def checkddate(self):
		if Bookkeep.currdate.day == self.ddate.day - 1:
			print("pop-up notice gui")
		# 	output gui here #


		# 				    #
		pass

	def report(self):
		if Bookkeep.currdate.day == 1:
			print("generate report and reset value")
		# 	print total and reset total
		# 	if possible create excel of total per month w/graph
		pass 

if __name__ == '__main__':
	# wew = Bookkeep(amount=570.00)
	wew = Bookkeep(amount=570.00, nonvat=0, innumber=279, cust="Willy Ubaldo", ddate= datetime.datetime.now() + datetime.timedelta(days=1))
	print(wew.cust, wew. amount, wew.nonvat, wew.nvat, wew.taxable, wew.innumber, wew.ddate.strftime("%Y-%m-%d %I:%M"),"\n")

	# wat = Bookkeep(1800.00, 0, 280, "Alex Visconde", None)
	# print(wat.cust, wat. amount, wat.nonvat, wat.innumber, wat.ddate,"\n")

	# rat = Bookkeep(500.00, 0, 281, "Baby Lim", None)
	# print(rat.cust, rat. amount, rat.nonvat, rat.innumber, rat.ddate,"\n")



	# bklist = []

	# bklist.append(wew)
	# bklist.append(wat)
	# bklist.append(rat)

	# for num in bklist:
	# 	print(num.cust, num.amount, num.nonvat, num.nvat, num.taxable, num.innumber, num.ddate.strftime("%Y-%m-%d %I:%M"),"\n")

	# print("total invoice: ", Bookkeep.totalinvoice)
	# print("total VAT: ", Bookkeep.totalvat)
	# print("total taxable: ", Bookkeep.totaltaxable)

	s = datetime.datetime.now()
	print(s.strftime("%Y-%m-%d %I:%M"))
	
	d = s - datetime.timedelta(days=3) + datetime.timedelta(days=29)
	print(d.strftime("%Y-%m-%d %I:%M"))

	print(d.day - 1)

	# d = datetime.datetime.strptime(s, '%m/%d/%Y') + datetime.timedelta(days=1)
	# print (d)

	# wew = Bookkeep(300, 100)
	# print(type(wew.amount))
	# print ("Total Employee", wew.amount)
	# print("wew: ", wew.totalinvoice)

	# meh = Bookkeep(400, 200)
	# print(type(meh.amount))
	# print ("Total Employee", meh.amount)
	# print("meh: ", meh.totalinvoice)
	
	
	# print("hotdog: ", Bookkeep.totalinvoice)
	# master = Bookkeep(0,0)

	# print("master: ", master.totalinvoice)
	# print("Reset total \n")

	# master.resettot()
	# print("wew: ", wew.totalinvoice)
	# print("meh: ", meh.totalinvoice)
	# print("master: ", master.totalinvoice)
	# print("hotdog: ", Bookkeep.totalinvoice)

	# universal deletion across same classes



	


	# get from db:
	# list of receipts
	# cash receipts
	# due dates of sales charge
	# provisional receipts

	# track due date func() 

	
	# invoice number creation
	# due date notification
	# total ammount, VAT, taxable report after 30 days

	# input		input
	# taxable = invoice - non vat
	# vat = taxable * 0.12