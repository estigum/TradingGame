from datetime import datetime

class AccountTransactionType:
    DEPOSIT = 1
    WITHDRAWAL = 2
    INTEREST = 3
    MARGINCALL = 4


class AccountTransactionStatus:
    PENDING = 1
    COMPLETE = 2
    CANCELLED = 3


class AccountTransaction:
    def __init__(self, accountId, amount, type, status, createdBy, createdAt=datetime.now(), lastUpdatedBy=None,
                 lastUpdatedAt=datetime.now()):
        self.__AccountId = accountId
        self.__Amount = amount
        self.__Type = type
        self.__Status = status
        self.__CreatedBy = createdBy
        self.__CreatedAt = createdAt
        if lastUpdatedBy is None:
            self.__LastUpdatedBy = createdBy
        else:
            self.__LastUpdatedBy = lastUpdatedBy
        self.__LastUpdatedAt = lastUpdatedAt

    @property
    def AccountId(self):
        return self.__AccountId

    @property
    def Amount(self):
        return self.__Amount

    @Amount.setter
    def Amount(self, amount):
        self.__Amount = amount

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, type):
        self.__Type = type

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, status):
        self.__Status = status

    @property
    def CreatedBy(self):
        return self.__CreatedBy

    @property
    def CreatedAt(self):
        return self.__CreatedAt

    @property
    def LastUpdatedBy(self):
        return self.__LastUpdatedBy

    @property
    def LastUpdatedAt(self):
        return self.__LastUpdatedAt

    @LastUpdatedBy.setter
    def LastUpdatedBy(self, lastUpdatedBy):
        self.__LastUpdatedBy = lastUpdatedBy

    @LastUpdatedAt.setter
    def LastUpdatedAt(self, lastUpdatedAt):
        self.__LastUpdatedAt = lastUpdatedAt
