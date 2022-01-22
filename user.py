class User:
    """
    Class that generates new instances of users.
    """
    users =[]
    def __init__(self, user_name, first_name, last_name, password):
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