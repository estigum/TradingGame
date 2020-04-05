import unittest
from Entities.AccountTransaction import AccountTransaction
from Entities.AccountTransaction import AccountTransactionStatus
from Entities.AccountTransaction import AccountTransactionType
from datetime import datetime


class AccountTransactionTest(unittest.TestCase):

    def test_addAccountTransaction(self):

        created = datetime.now()
        at = AccountTransaction(5, 1, 5000, AccountTransactionType.DEPOSIT, AccountTransactionStatus.COMPLETE, "bank", created)

        self.assertEqual(at.TransId, 5)
        self.assertEqual(at.AccountId, 1)
        self.assertEqual(at.Amount, 5000)
        self.assertEqual(at.Type, AccountTransactionType.DEPOSIT)
        self.assertEqual(at.Status, AccountTransactionStatus.COMPLETE)
        self.assertEqual(at.CreatedBy, "bank")
        self.assertEqual(at.CreatedAt, created)


if __name__ == '__main__':
    unittest.main()
