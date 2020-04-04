import unittest
from Services.UserManagement import  UserManagement
from Entities.User import UserState


class TestUserManagement(unittest.TestCase):

    def test_adduser(self):

        um = UserManagement()
        user = um.Add('estigum', 'Erik Stigum', 'test123', 'This is my account', 'usermanagment')
        self.assertEqual(user.UserName, 'estigum')
        self.assertEqual(user.FullName, 'Erik Stigum')
        self.assertEqual(user.Password, 'test123')
        self.assertEqual(user.Comment, 'This is my account')
        self.assertEqual(user.Status, UserState.OPEN)

    def test_tryaddsameuseragian(self):
        um = UserManagement()
        um.Add('estigum', 'Erik Stigum', 'test123', 'This is my account', 'usermanagment')
        try:
            um.Add('estigum', 'Erik Stigum', 'test123', 'This is my account', 'usermanagment')
        except Exception as e:
            self.assertEqual(e.args[0], "User already exists")

    def test_getuserexist(self):
        um = UserManagement()
        um.Add('estigum', 'Erik Stigum', 'test123', 'This is my account', 'usermanagment')
        user = um.Get('estigum')
        self.assertNotEqual(user, None)

    def test_getusernotexist(self):
        um = UserManagement()
        um.Add('estigum', 'Erik Stigum', 'test123', 'This is my account', 'usermanagment')
        user = um.Get('cstigum')
        self.assertEqual(user, None)

    def test_modifyuser(self):
        um = UserManagement()
        um.Add('estigum', 'Erik Stigum', 'test123', 'This is my account', 'usermanagment')
        um.Modify('estigum', UserState.CLOSED, 'usermanagment')
        user = um.Get('estigum')
        self.assertEqual(user, None)

    def test_modifyusernotexist(self):
        um = UserManagement()
        um.Add('estigum', 'Erik Stigum', 'test123', 'This is my account', 'usermanagment')
        try:
            um.Modify('cstigum', UserState.CLOSED, 'usermanagment')
        except Exception as e:
            self.assertEqual(e.args[0], "User does not exist.  Can't modify")


if __name__ == '__main__':
    unittest.main()
