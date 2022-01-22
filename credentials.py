from keyring import delete_password


class Credentials:
    '''
    Class that generates instances of credentials
    '''
    passwords = []
    def __init__(self, account, password):
        '''
        __init__ method that helps us define properties for our objects
        Args:
          account = New credentials account
          password = New credentials password
        '''

        self.account = account
        self.password = password

    def save_password(self):
        '''
        save_password method that saves credential objects into passwords
        ''' 
        Credentials.passwords.append(self)  

    def delete_password(self):
        '''
        delete_password method to delete a saved password from the passwords list
        '''
        Credentials.passwords.remove(self) 

    @classmethod
    def find_by_account(cls, accountName) :
        '''
        Method that takes in account and returns the password that matches the account
        Args:
          account: Account to search for
        Returns:
          Password of the mentioned account  
        ''' 
        for password in cls.passwords:
            if password.account == accountName:
                return password  

    @classmethod
    def password_exist(cls, accountName) :
        '''
        Method that checks if a password exists from the password list
        ''' 
        for password in cls.passwords:
            if password.account == accountName:
                return True              
        return False 

    @classmethod
    def display_passwords(cls):
        '''
        Method that displays the passwords list
        ''' 
        return cls.passwords          