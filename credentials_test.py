from select import select
import unittest
from credentials import Credentials
 
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self) :
        '''
        tearDown method that does clean up after each test case has run
        '''
        Credentials.passwords = []

    def setUp(self):
        '''
        Set up method to run before each test case
        ''' 
        self.new_credential = Credentials("Instagram", "12345") 

    def test_init(self):
        '''
        test_init method to test if the object is initialized properly
        ''' 
        self.assertEqual(self.new_credential.account, "Instagram")  
        self.assertEqual(self.new_credential.password, "12345")   
    
    def test_save_password(self):
        '''
        test_save_password test case to test if the credentials object is saved into the passwords list
        '''
        self.new_credential.save_password()
        self.assertEqual(len(Credentials.passwords),1)

    def test_save_multiple_passwords(self):
        '''
        test_save_multiple_passwords to check if we can save multiple credentials objects into passwords list.
        '''  
        self.new_credential.save_password()
        test_password = Credentials("Twitter", "5678")  
        test_password.save_password()
        self.assertEqual(len(Credentials.passwords),2)
    
    def test_delete_password(self):
        '''
        test_delete_password to test if we can remove a password
        ''' 
        self.new_credential.save_password()
        test_password = Credentials("ruuuuu", "2345")
        test_password.save_password()

        self.new_credential.delete_password()
        self.assertEqual(len(Credentials.passwords),1)
if __name__ == '__main__':
    unittest.main() 