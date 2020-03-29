import datetime


class User:
    def __init__(self, userId, username, fullname, password, comment, status, createdBy, createdAt, lastUpdatedBy, lastUpdatedAt):
        self.__UserId = userId
        self.__UserName = username
        self.__FullName = fullname
        self.__Password = password
        self.__Comment = comment
        self.__CreatedBy = createdBy
        self.__CreatedAt = createdAt
        self.__Status = status
        self.__LastUpdatedBy = lastUpdatedBy
        self.__LastUpdatedAt = lastUpdatedAt

    def __init__(self, userId, username, fullname, password, comment, status, createdBy):
        self.__UserId = userId
        self.__UserName = username
        self.__FullName = fullname
        self.__Password = password
        self.__Comment = comment
        self.__CreatedBy = createdBy
        self.__CreatedAt = datetime.datetime.now()
        self.__Status = status
        self.__LastUpdatedBy = createdBy
        self.__LastUpdatedAt = datetime.datetime.now()

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
