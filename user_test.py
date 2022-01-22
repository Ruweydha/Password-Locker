import unittest #importing the Unit test
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

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

    def test_save_multiple_users(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects in our users list
        ''' 
        self.new_user.save_user()
        test_user = User("Test", "User", "testUser", "2000")   
        test_user.save_user()
        self.assertEqual(len(User.users), 2)
    
    def test_delete_user(self):
        '''
        test_delete-user to test if we can remove a user from our users list
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "testU", "4321")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.users),1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''  
        self.new_user.save_user()
        test_user = User("Test", "User", "testU", "123456") 
        test_user.save_user()

        found_user = User.find_by_username("testU")
        self.assertEqual(found_user.user_name, test_user.user_name) 

    def test_user_exist(self):
        '''
        Test to return a boolean incase we cannot find the user
        ''' 
        self.new_user.save_user()
        test_user = User ("Test", "User", "U_test", "abcde")
        test_user.save_user() 

        user_exists = User.user_exist("U_test") 
        self.assertTrue(user_exists) 

    def test_display__all_users(self):
        '''
        Method that returns a list of all contacts saved
        '''
        self.assertEqual(User.display_users(), User.users)    

if __name__ == '__main__':
    unittest.main()         