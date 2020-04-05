from Entities.User import User
from Entities.User import UserState
from datetime import datetime


class UserManagement:
    def __init__(self):
        self.__Users = {}
        self.__CurrentUserId = 0

    def Get(self, username):

        if username in self.__Users:
            return self.__Users[username]

        return None

    def Add(self, username, fullname, password, comment, createdBy):

        if not (self.Get(username) is None):
            raise Exception("User already exists")

        self.__CurrentUserId = self.__CurrentUserId + 1
        user = User(self.__CurrentUserId, username, fullname, password, comment, UserState.OPEN, createdBy)

        self.__Users[user.UserName] = user

        return user

    def Modify(self, username, status, lastUpdatedBy):

        user = self.Get(username)
        if user is None:
            raise Exception("User does not exist.  Can't modify")

        user.Status = status
        user.LastUpdatedBy = lastUpdatedBy
        user.LasMUpdatedAt = datetime.now()
        if status == UserState.CLOSED:
            del self.__Users[username]

    def __contains__(self, username):

        if username in self.__Users:
            return True
        return False
