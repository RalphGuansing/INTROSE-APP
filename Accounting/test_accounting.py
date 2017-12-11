import unittest2 as unittest
from AccountingView import *
class test_accounting(unittest.TestCase):
    #ACCOUNTS RECEIVABLES
    def test_add_ar(self):
        arDB = AccountingDB()
        ar_list = []

        customer = Customer(1,"Kingsroad vet")

        ar = AccountsReceivable(1, '2017-12-8', 2198, 500, date_paid=None, pr_no=None, payment=None)
        ar_list.append(ar)
        ar = AccountsReceivable(1, '2017-12-9', 2199, 600, '2017-12-10', 200, 600)
        ar_list.append(ar)
        ar = AccountsReceivable(2, '2017-12-9', 2200, 2000, date_paid=None, pr_no=None, payment=None)
        ar_list.append(ar)
        ar = AccountsReceivable(1, '2017-12-9', 2201, 1352.55, date_paid=None, pr_no=None, payment=None)
        ar_list.append(ar)

        ar = AccountsReceivable(2, '2017-12-7', 3254, 5496.23, date_paid=None, pr_no=None, payment=None)
        ar_list.append(ar)
        ar = AccountsReceivable(2, '2017-12-7', 3255, 98200.50, date_paid=None, pr_no=None, payment=None)
        ar_list.append(ar)
        ar = AccountsReceivable(2, '2017-12-8', 3256, 3567.55, date_paid=None, pr_no=None, payment=None)
        ar_list.append(ar)

        for i in ar_list:
            arDB.add_accountsreceivable(i)
        arDB.close_connection()

    def test_update_ar(self):
        arDB = AccountingDB()
        ar_list = []

        customer = Customer(1, "Kingsroad vet")

        ar = AccountsReceivable(1, '2017-12-8', 2198, 500.98, date_paid=None, pr_no=None, payment=None)
        # ar = AccountsReceivable(1, '2017-12-9', 2199, 600, '2017-12-10', 200, 600)
        # ar_list.append(ar)


        arDB.update_accountsreceivable(ar)
        arDB.close_connection()


    def test_delete_ar(self):
        arDB = AccountingDB()
        ar_list = []

        customer = Customer(1, "Kingsroad vet")

        ar = AccountsReceivable(None, None, 2200, None, None, None, None)
        # ar = AccountsReceivable(1, '2017-12-9', 2199, 600, '2017-12-10', 200, 600)
        # ar_list.append(ar)

        if False:
            arDB.delete_accountsreceivable(ar)
        arDB.close_connection()

    # ACCOUNTS PAYABLES
    def test_add_ap(self):
        apDB = AccountingDB()
        credit_list = []

        credit = Credit(5,"Meals and Snacks",16250.00)
        credit_list.append(credit)
        credit = Credit(5,"Gas and Oil",16250.00)
        credit_list.append(credit)

        ap = AccountsPayable('2017-12-8', 'Ralph Guansing', 5,32500.00)
        ap.set_credits(credit_list)

        apDB.add_accountspayable(ap)

        apDB.close_connection()
    def test_update_ap(self):
        apDB = AccountingDB()
        credit_list = []

        id_apv = 5

        credit = Credit(id_apv, "Meals and Snacks", 16250.00)
        credit_list.append(credit)
        credit = Credit(id_apv, "Gas and Oil", 16250.00)
        credit_list.append(credit)



        ap = AccountsPayable('2017-12-8', 'Ralph EDITED2 Guansing', id_apv, 32500.00)
        ap.set_credits(credit_list)

        apDB.delete_accountspayable(id_apv)
        apDB.add_accountspayable(ap)

        apDB.close_connection()

    def test_delete_ap(self):
        apDB = AccountingDB()

        #ap = AccountsPayable('2017-12-8', 'Ralph Guansing', 5, 32500.00)
        #ap.set_credits(credit_list)

        apDB.delete_accountspayable(5)

        apDB.close_connection()


if __name__ == '__main__':
    unittest.main()
