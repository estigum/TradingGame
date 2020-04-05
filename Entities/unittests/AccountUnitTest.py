import unittest
from Entities.Account import Account
from Entities.Account import AccountState
from datetime import datetime


class TestAccount(unittest.TestCase):

    def test_addAccount(self):
        created = datetime.now()
        account = Account(1, 1, "USD", 25000000, AccountState.OPEN, "estigum",created)
        self.assertEqual(account.AccountId, 1)
        self.assertEqual(account.UserId, 1)
        self.assertEqual(account.Ccy, "USD")
        self.assertEqual(account.Amount, 25000000)
        self.assertEqual(account.Status, AccountState.OPEN)
        self.assertEqual(account.CreatedBy, "estigum")
        self.assertEqual(account.LastUpdatedBy, "estigum")
        self.assertEqual(account.CreatedAt, created)

    def test_lastUpdatedBy(self):
        created = datetime.now()
        account = Account(1, 1, "USD", 25000000, AccountState.OPEN, "estigum",created)
        account.LastUpdatedBy = "cstigum"
        self.assertEqual(account.LastUpdatedBy, "cstigum")

    def test_amountUpdated(self):
        created = datetime.now()
        account = Account(1, 1, "USD", 25000000, AccountState.OPEN, "estigum",created)
        account.LastUpdatedBy = "cstigum"
        account.Amount = 15000000
        self.assertEqual(account.Amount, 15000000)
        self.assertEqual(account.LastUpdatedBy, "cstigum")




if __name__ == '__main__':
    unittest.main()
