class Loan:

    def __init__(self, cryptouserid, loanid, currency, amount, interest):
        self.__cryptouserid = cryptouserid
        self.__loanid = loanid
        self.__currency = currency
        self.__amount = amount
        self.__interest = interest

    @property
    def cryptouserid(self):
        return self.__cryptouserid

    @property
    def loanid(self):
        return self.__loanid

    @property
    def currency(self):
        return self.__currency

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def interest(self):
        return self.__interest

    @interest.setter
    def interest(self, interest):
        self.__interest = interest


class Bank:

    def __init__(self, bankid, name, comment, maxloanamount, dailyinterestrate):
        self.__bankid = bankid
        self.__name = name
        self.__comment = comment
        self.__maxloanamount = maxloanamount
        self.__dailyinterestrate = dailyinterestrate
        self.__loans = {}

    @property
    def bankid(self):
        return self.__bankid

    @property
    def name(self):
        return self.__name

    @property
    def comment(self):
        return self.__comment

    @property
    def maxamount(self):
        return self.__maxloanamount

    @maxamount.setter
    def maxamount(self, maxamount):
        self.__maxloanamount = maxamount

    @property
    def dailyinterestrate(self):
        return self.__dailyinterestrate

    @dailyinterestrate.setter
    def dailyinterestrate(self, dailyinterestrate):
        self.__dailyinterestrate = dailyinterestrate

    def addLoan(self, loan):
        if loan.cryptouserid in self.__loans:
            print("This loan already exist for " + str(loan.cryptouserid))
            return False
        else:
            self.__loans[loan.cryptouserid] = loan
            return True

    def borrow(self, cryptouserid, amount):
        if cryptouserid in self.__loans:
            loan = self.__loans[cryptouserid]
            newamount = loan.amount + amount
            if newamount > self.__maxloanamount:
                return False, "You can't borrow that much. Denied"
            loan.amount = newamount
            return True, "Approved"
        return False, "Can't find loanId. Open new loan"

    def calcdailyinterest(self):
        for cryptouserid in self.__loans:
            loan = self.__loans[cryptouserid]
            daily = loan.amount * self.__dailyinterestrate * (1.0/365.0)
            loan.interest = loan.interest + daily

    def getloan(self, cryptouserid):
        if cryptouserid in self.__loans:
            return True, self.__loans[cryptouserid]
        return False, "Can't find user"

