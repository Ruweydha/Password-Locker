import unittest #importing the Unit test
from user import User

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self) :
        '''
        tearDown method that does clean up after each test case has run
        '''
        User.users = []

    def setUp(self) :
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User("Ruweydha", "Abdinoor", "Rads", "1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''  
        self.assertEqual(self.new_user.first_name, "Ruweydha")
        self.assertEqual(self.new_user.last_name, "Abdinoor")
        self.assertEqual(self.new_user.user_name, "Rads") 
        self.assertEqual(self.new_user.password, "1234") 
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)


if __name__ == '__main__':
    unittest.main()         