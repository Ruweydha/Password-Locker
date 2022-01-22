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

if __name__ == '__main__':
    unittest.main() 