from Entities.Account import Account
from Entities.Account import AccountState
from Entities.AccountTransaction import AccountTransaction
from Entities.AccountTransaction import AccountTransactionStatus
from Entities.AccountTransaction import AccountTransactionType
from datetime import datetime


class AccountManagement:
    def __init__(self):
        self.__Accounts = dict()
        self.___UserAccounts = dict()
        self.__AccountTransactions = dict();
        self.__LastTransId = 0
        self.__LastAccountId = 0

    @property
    def LastTransId(self):
        return self.__LastTransId;

    @property
    def LastAccountId(self):
        return self.__LastAccountId

    def Get(self, accountId):

        if accountId in self.__Accounts:
            return self.__Accounts[accountId]

        return None

    def UserAccountByCcyExist(self, userId, ccy):
        if userId in self.___UserAccounts:
            userAccounts = self.___UserAccounts[userId]
            if ccy in userAccounts:
                return True
        return False

    def GetNextAccountId(self):
        self.__LastAccountId =  self.LastAccountId + 1

        return self.__LastAccountId

    def GetNextTransactionId(self):
        self.__LastTransId = self.LastTransId + 1

        return self.__LastTransId

    def GetUserAccounts(self, userId):
        if userId in self.___UserAccounts:
            return self.___UserAccounts[userId]

        return None

    def Add(self, userId, ccy, amount, createdBy):

        if self.UserAccountByCcyExist(userId, ccy):
            raise Exception("Account already exist for userId =" + str(userId) + " and currency =" + ccy)

        account = Account(self.GetNextAccountId(), userId, ccy, amount, AccountState.OPEN, createdBy)

        self.__Accounts[account.AccountId] = account

        if userId in self.___UserAccounts:
            userAccounts = self.___UserAccounts[userId]
            userAccounts[account.Ccy] = account
        else:
            userAccounts = dict()
            userAccounts[account.Ccy] = account
            self.___UserAccounts[userId] = userAccounts

        self.AddTransaction(account.AccountId, amount, AccountTransactionType.DEPOSIT, AccountTransactionStatus.COMPLETE, createdBy)

        return account

    def AddTransaction(self, accountId, amount, type, status, createdBy):

        trans = AccountTransaction(self.GetNextTransactionId(), accountId, amount, type, status, createdBy)

        if accountId in self.__AccountTransactions:
            tranList = self.__AccountTransactions[accountId]
            tranList[trans.TransId] = trans
        else:
            tranList = dict()
            tranList[trans.TransId] = trans
            self.__AccountTransactions[accountId] = tranList

    def Depost(self, userId, ccy, amount, lastUpdatedBy):

        if not self.UserAccountByCcyExist(userId, ccy):
            raise Exception("You don't have an account for userId " + str(userId) + " and currency " + ccy)

        userAccounts = self.___UserAccounts[userId]
        ccyAccount = userAccounts[ccy]
        ccyAccount.Amount = ccyAccount.Amount + amount
        ccyAccount.LastUpdatedBy = lastUpdatedBy
        ccyAccount.LastUpdatedAt = datetime.now()

        self.AddTransaction(ccyAccount.AccountId, amount, AccountTransactionType.DEPOSIT, AccountTransactionStatus.COMPLETE, lastUpdatedBy)

    def Withdrawal(self, userId, ccy, amount, lastUpdatedBy):
        if not self.UserAccountByCcyExist(userId, ccy):
            raise Exception("You don't have an account for userId " + str(userId) + " and currency " + ccy)

        userAccounts = self.___UserAccounts[userId]
        ccyAccount = userAccounts[ccy]
        if ccyAccount.Amount < amount:
            raise Exception("You don't have enough money in account for currency " + ccy
                            + " for a withdrawal")

        ccyAccount.Amount = ccyAccount.Amount - amount
        ccyAccount.LastUpdatedBy = lastUpdatedBy
        ccyAccount.LastUpdatedAt = datetime.now()

        self.AddTransaction(ccyAccount.AccountId, amount, AccountTransactionType.WITHDRAWAL,
                            AccountTransactionStatus.COMPLETE, lastUpdatedBy)

    def MarginCall(self, userId, ccy, amount, lastUpdatedBy):
        if not self.UserAccountByCcyExist(userId, ccy):
            raise Exception("You don't have an account for userId " + str(userId) + " and currency " + ccy)

        userAccounts = self.___UserAccounts[userId]
        ccyAccount = userAccounts[ccy]
        if ccyAccount.Amount < amount:
            raise Exception("You don't have enough money in account for currency " + ccy
                            + " for a margin call")

        ccyAccount.Amount = ccyAccount.Amount - amount
        ccyAccount.LastUpdatedBy = lastUpdatedBy
        ccyAccount.LastUpdatedAt = datetime.now()

        self.AddTransaction(ccyAccount.AccountId, amount, AccountTransactionType.MARGINCALL,
                            AccountTransactionStatus.COMPLETE, lastUpdatedBy)


