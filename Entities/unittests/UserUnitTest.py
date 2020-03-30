import unittest
from Entities.User import User
from Entities.User import UserState
import datetime


class TestUser(unittest.TestCase):

    def test_newuser(self):
        user = User(1, 'estigum', 'Erik Stigum', 'Test123', 'This is a test Account', UserState.OPEN, 'system')
        self.assertEqual(user.UserName, 'estigum')
        self.assertEqual(user.Password, 'Test123')
        self.assertEqual(user.UserId, 1)
        self.assertEqual(user.Comment, 'This is a test Account')
        self.assertEqual(user.Status, UserState.OPEN)
        self.assertEqual(user.FullName, 'Erik Stigum')
        self.assertEqual(user.CreatedBy, 'system')
        self.assertEqual(user.LastUpdatedBy, 'system')

    def test_lastupdatedbychanged(self):
        user = User(1, 'estigum', 'Erik Stigum', 'Test123', 'This is a test Account', UserState.OPEN, 'system')
        user.LastUpdatedBy = 'cstigum'
        self.assertEqual(user.LastUpdatedBy, 'cstigum')

    def test_existinguser(self):
        testdate = datetime.datetime.now()
        user = User(1,'estigum','Erik Stigum','Test123', 'This is a test Account', UserState.OPEN,'system', testdate, 'estigum', testdate)
        self.assertEqual(user.UserName, 'estigum')
        self.assertEqual(user.Password, 'Test123')
        self.assertEqual(user.UserId, 1)
        self.assertEqual(user.Comment, 'This is a test Account')
        self.assertEqual(user.Status, UserState.OPEN)
        self.assertEqual(user.FullName, 'Erik Stigum')
        self.assertEqual(user.CreatedBy, 'system')
        self.assertEqual(user.CreatedAt, testdate)
        self.assertEqual(user.LastUpdatedBy, 'estigum')
        self.assertEqual(user.LastUpdatedAt, testdate)

    def test_closeduser(self):
        testdate = datetime.datetime.now()
        user = User(1, 'estigum', 'Erik Stigum', 'Test123', 'This is a test Account', UserState.OPEN, 'system', testdate, 'estigum', testdate)
        user.Status = UserState.CLOSED
        self.assertEqual(user.Status, UserState.CLOSED)


if __name__ == '__main__':
    unittest.main()
