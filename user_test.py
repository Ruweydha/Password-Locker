import unittest #importing the Unit test
from user import User

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self) :
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User("Ruweydha", "Abdinoor", "Rads", "1234")


if __name__ == '__main__':
    unittest.main()         