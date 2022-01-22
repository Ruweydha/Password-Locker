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