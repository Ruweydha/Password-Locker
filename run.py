import imp
from user import User
from credentials import Credentials

def create_user(first_name, last_name, user_name, password):
    '''
    function to create a new user
    '''
    new_user = User(first_name, last_name, user_name, password)
    return new_user

def save_user(user):
    '''
    Function to save a user
    '''  
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''  
    user.delete_user() 
def find_user(name):
    '''
    Function that finds an account by username and returns the user
    ''' 
    return User.find_by_username(name)  

def check_existing_users(name):
    '''
    Function to check if a user exists with that username and returns a boolean
    '''
    return User.find_by_username(name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users() 

def create_password(account, password):
    '''
    Function to create a new password
    ''' 
    new_password = Credentials(account, password)
    return new_password  

def save_password(password):
    '''
    Function to save a password
    '''
    password.save_password()

def del_password(password):
    '''
    Function to delete a password
    '''
    password.delete_password()

def  find_password(name):
    '''
    Function to find a password by the account and returns the password
    '''   
    return Credentials.find_by_account(name)

def check_existing_password(name):
    '''
    Function to check if password exists and returns a boolean
    '''
    return Credentials.password_exist(name)

def display_passwords():
    '''
    Function to display all passwords stored
    '''
    return Credentials.display_passwords()