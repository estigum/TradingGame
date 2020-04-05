import unittest
from Services.AccountManagement import AccountManagement


class AccountManagementUnitTest(unittest.TestCase):

    def test_addAccount(self):
        am = AccountManagement()
        account = am.Add(1, "USD", 5000, "estigum")
        self.assertEqual(account.AccountId, 1)
        self.assertEqual(account.UserId, 1)
        self.assertEqual(account.Amount, 5000)
        self.assertEqual(account.CreatedBy, "estigum")
        self.assertEqual(account.LastUpdatedBy, "estigum")

    def test_accountExist(self):
        am = AccountManagement()
        am.Add(1, "USD", 5000, "estigum")
        self.assertEqual(am.UserAccountByCcyExist(1, "USD"), True)

    def test_accountDoesNotExist(self):
        am = AccountManagement()
        am.Add(1, "USD", 5000, "estigum")
        self.assertEqual(am.UserAccountByCcyExist(1, "GBP"), False)

    def test_deposit(self):
        am = AccountManagement()
        am.Add(1, "USD", 5000, "estigum")
        am.Depost(1, "USD", 10000, "cstigum")
        account = am.Get(1)
        self.assertEqual(account.Amount, 15000)
        self.assertEqual(account.LastUpdatedBy, "cstigum")

    def test_depositAccountDoesNotExist(self):
        try:
            am = AccountManagement()
            am.Depost(1, "GBP", 5000, "cstigum")
        except Exception as e:
            self.assertEqual(e.args[0], "You don't have an account for userId 1 and currency GBP")

    def test_withdrawal(self):
        am = AccountManagement()
        am.Add(1, "USD", 5000, "estigum")
        am.Withdrawal(1, "USD", 3000, "cstigum")
        account = am.Get(1)
        self.assertEqual(account.Amount, 2000)
        self.assertEqual(account.LastUpdatedBy, "cstigum")

    def test_withdrawalAccountDoesNotExist(self):
        try:
            am = AccountManagement()
            am.Withdrawal(1, "GBP", 5000, "cstigum")
        except Exception as e:
            self.assertEqual(e.args[0], "You don't have an account for userId 1 and currency GBP")

    def test_withdrawalException(self):
        try:
            am = AccountManagement()
            am.Add(1, "USD", 5000, "estigum")
            am.Withdrawal(1, "USD", 13000, "cstigum")
        except Exception as e:
            self.assertEqual(e.args[0], "You don't have enough money in account for currency USD for a withdrawal")

    def test_marginCall(self):
        am = AccountManagement()
        am.Add(1, "USD", 5000, "estigum")
        am.MarginCall(1, "USD", 3000, "cstigum")
        account = am.Get(1)
        self.assertEqual(account.Amount, 2000)
        self.assertEqual(account.LastUpdatedBy, "cstigum")

    def test_marginCallAccountDoesNotExist(self):
        try:
            am = AccountManagement()
            am.MarginCall(1, "GBP", 5000, "cstigum")
        except Exception as e:
            self.assertEqual(e.args[0], "You don't have an account for userId 1 and currency GBP")

    def test_marginCallException(self):
        try:
            am = AccountManagement()
            am.Add(1, "USD", 5000, "estigum")
            am.MarginCall(1, "USD", 13000, "cstigum")
        except Exception as e:
            self.assertEqual(e.args[0], "You don't have enough money in account for currency USD for a margin call")


if __name__ == '__main__':
    unittest.main()
