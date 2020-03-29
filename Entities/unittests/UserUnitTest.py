import unittest
import Entities.User


class TestUser(unittest.TestCase):

    def test_newuser(self):
        user = Entities.User.User(1,'estigum','Erik Stigum','Test123', 'This is a test Account', 1,'system')
        self.assertEqual(user.UserName, 'estigum')
        self.assertEqual(user.Password, 'Test123')
        self.assertEqual(user.UserId, 1)
        self.assertEqual(user.Comment, 'This is a test Account')
        self.assertEqual(user.Status, 1)
        self.assertEqual(user.FullName, 'Erik Stigum')
        self.assertEqual(user.CreatedBy, 'system')
        self.assertEqual(user.LastUpdatedBy, 'system')


if __name__ == '__main__':
    unittest.main()
