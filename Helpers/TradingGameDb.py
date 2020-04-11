from mysql import connector


class TradingGameDb(object):

    def __init__(self, user, password, host):
        self.__Host = host
        self.__User = user
        self.__Password = password
        self.__Db = None

    @property
    def Host(self):
        return self.__Host

    @property
    def User(self):
        return self.__User

    @property
    def Password(self):
        return self.__Password

    @property
    def Db(self):
        return self.__Db

    def Connect(self):
        self.__Db = connector.connect(
            host=self.Host,
            user=self.User,
            passwd=self.Password
        )
        print(self.Db)

    def ChangeDb(self, dbname):
        myCursor = self.Db.cursor()
        myCursor.execute("use " + dbname)
        self.Db.commit()

    def Update(self, sqlString):
        myCursor = self.Db.cursor()
        myCursor.execute(sqlString)
        self.Db.commit()

    def Select(self, sqlString):
        myCursor = self.Db.cursor()
        myCursor.execute(sqlString)
        return myCursor.fetchall()
