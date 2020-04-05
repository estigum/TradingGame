from datetime import datetime
from enum import Enum


class AccountState(Enum):
    OPEN = 1
    CLOSED = 2
    ONHOLD = 3


class Account:
    def __init__(self, accountId, userId, ccy, amount, status, createdBy, createdAt=datetime.now(), lastUpdatedBy=None, lastUpdatedAt=datetime.now()):
        self.__UserId = userId
        self.__AccountId = accountId
        self.__Ccy = ccy
        self.__Amount = amount
        self.__Status = status
        self.__CreatedBy = createdBy
        self.__CreatedAt = createdAt
        if lastUpdatedBy is None:
            self.__LastUpdatedBy = createdBy
        else:
            self.__LastUpdatedBy = lastUpdatedBy
        self.__LastUpdatedAt = lastUpdatedAt

    @property
    def UserId(self):
        return self.__UserId

    @property
    def AccountId(self):
        return self.__AccountId

    @property
    def Ccy(self):
        return self.__Ccy

    @property
    def Amount(self):
        return self.__Amount

    @Amount.setter
    def Amount(self, amount):
        self.__Amount = amount

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
