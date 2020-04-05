import datetime
from enum import Enum


class UserState(Enum):
    OPEN = 1
    CLOSED = 2
    ONHOLD = 3


class User:
    def __init__(self, userId, username, fullname, password, comment, status, createdBy,
                 createdAt=datetime.datetime.now(), lastUpdatedBy=None, lastUpdatedAt=datetime.datetime.now()):
        self.__UserId = userId
        self.__UserName = username
        self.__FullName = fullname
        self.__Password = password
        self.__Comment = comment
        self.__CreatedBy = createdBy
        self.__CreatedAt = createdAt
        self.__Status = status
        if lastUpdatedBy is None:
            self.__LastUpdatedBy = createdBy
        else:
            self.__LastUpdatedBy = lastUpdatedBy
        self.__LastUpdatedAt = lastUpdatedAt

    @property
    def UserId(self):
        return self.__UserId

    @property
    def UserName(self):
        return self.__UserName

    @property
    def FullName(self):
        return self.__FullName

    @property
    def Password(self):
        return self.__Password

    @property
    def Comment(self):
        return self.__Comment

    @property
    def CreatedBy(self):
        return self.__CreatedBy

    @property
    def CreatedAt(self):
        return self.__CreatedAt

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, status):
        self.__Status = status

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
