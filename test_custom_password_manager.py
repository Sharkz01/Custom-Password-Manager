import unittest
from io import StringIO
import sys
from custom_password_manager import BasePasswordManger, PasswordMananger

class TestCustomPasswordManager(unittest.TestCase):
    sys.stdout
    sys.stdin

    def setUp(self):
        print("Running setUP method ...")

    def test_old_password(self):
        old_password = BasePasswordManger(["012345","123shd","shado1"],"shado1")
        self.assertEqual(old_password.old_passwords(), "shado1")

    def test_get_password(self):
        current_password = BasePasswordManger("shado1", "shado1")
        self.assertEqual(current_password.get_password(), "Current password is: shado1")

    def test_is_correct(self):
        user_input = input("Please enter password: ")
        is_correct = BasePasswordManger("shado1", "shado1")
        self.assertEqual(is_correct.is_correct(), user_input)

    # def test_set_password(self):
    #     password, security_level, current_password = BasePasswordManger(["012345","123shd","shado1"],"shado1")

    #     if len(password)<6:
    #         self.assertTrue("Password length must be a minimun of 6 characters.\nPassword Change: UNSUCCESSFUL")
    #     elif security_level<2:
    #         self.assertTrue("Password must contain special character with numbers and alphabets.\nPassword Change: UNSUCCESSFUL")
    #     elif password == current_password:
    #         self.assertTrue("Password Change: No Changes Detected")
    #     else:
    #         self.assertTrue("Password Change: SUCCESSFUL")
    
if __name__ == '__main__':
    unittest.main()