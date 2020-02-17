import collections

User = collections.namestuple('CryptoUser','UserId UserName, Password, Comment')


class Position:
    def __init__(self,userid, currency, amount):
        self.__userId = userid
        self.__currency = currency
        self.__amount = amount

    @property
    def currency(self):
        return self.__currency;

    @property
    def userid(self):
        return self.__userid

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,amount):
        self.__amount = amount
