class User:
    """
    Class that generates new instances of users.
    """
    users =[]
    def __init__(self, first_name, last_name, user_name, password):
        """
        ___init__ method that helps us define proprrties for our objects
        Args:
        user_name: New user username
        first_name: New user first name
        last_name: New user last name
        password: New user password
        """
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save_user method that saves user objects into users
        '''
        User.users.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the contact_list
        ''' 
        User.users.remove(self)   

    @classmethod  
    def find_by_username(cls, name):
        '''
        Method that takes in username and returns a user that matches the username

        Args:
          username: username to search 
        
        Returns:
          User that matches the username
        '''
        for user in cls.users:
            if user.user_name == name:
                return user    
    
    @classmethod
    def user_exist(cls, name):
        '''
        Method that checks if a contact exists form the contact list

        Args:
          username: Username to search for
        Returns:
          Boolean: True or false depending if the user exists
        '''
        for user in cls.users:
            if user.user_name == name:
                return True
        return False 
    @classmethod
    def display_users(cls):
        '''
        Method that displays the users list
        '''
        return cls.users
