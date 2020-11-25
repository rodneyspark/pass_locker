import unittest
from user import User
from info import Info

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('john','mwangi','johnmwagi@gmail.com')
        
    def test1(self):
        self.assertEqual(self.new_user.fname,'john')
        self.assertEqual(self.new_user.lname, 'mwangi')
        self.assertEqual(self.new_user.email,'johnmwangi@gmail.com')
        
    def test_save_user(self):
        self.new_user.save_user()
        
        
    def tearDown(self):
        User.save_userlist = []
    
    def test_delete_user(self):
        self.new_user.save_user()
        test_data = User('rodney','gakuru','rodneygakuru@gmail.com')
        test_data.save_user()
        self.assertEqual(len(User.save_userlist),2)
    
    def test_display_user(self):
        self.assertEqual(User.display_users(),User.save_userlist)
if __name__ == '__main__':
    unittest.main()