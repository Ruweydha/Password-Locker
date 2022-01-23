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
    User.delete_user(user) 
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

def del_password(account):
    '''
    Function to delete a password
    '''
    Credentials.delete_password(account)

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

def main():
    print("Welcome to Password locker") 
    print('*' *50)   

    print("What would you like to do? \n ")
    while True:

        print("Use this short codes:\n LG-Login\n CU- Create user\n DU- display users \n FU- find user \n EX-exit \n ")
        short_code = input().upper()
        print('\n') 

        if short_code == 'LG':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = find_user(username)

            if user.user_name == username and user.password == password:
                print("Logged in \n")

                while True:

                    print(f"Welcome {username}, Use the following short codes to select their corresponding values.\n SP- Save new password \n DELP - Delete password \n DISP- Display saved passwords \n LO- Log out \n")

                    picked_choice = input().upper()

                    if picked_choice == 'SP':
                        print("New account")
                        print("-" *20)
                        
                        account = input("Account name: ")
                        password = input("Password: ")

                        save_password(create_password(account, password))
                        print('\n')

                    elif picked_choice == 'DELP':
                        account = input("Enter the name of the password you want to delete:  ") 
                        if check_existing_password(account):
                            remove_account = find_password(account)
                            del_password(remove_account) 
                            print("Password and account deleted successfully \n")
                        else:
                            print(f"{account} Does not exist \n")

                    elif picked_choice == 'DISP':
                        if display_passwords():
                            print("Here is a list of all your passwords :")
                            print('\n')

                            for acc in display_passwords():
                            
                                print(f"Account: {acc.account} : password:{acc.password} \n")
                                print('\n')

                        else:
                            print('\n')
                            print('No password saved yet \n')  
                    elif picked_choice == 'LO':
                        print('Au revoir :^) !') 
                        print('\n')
                        break

            elif user.user_name != username or user.password != password :
                print("Wrong credentials") 
                print('\n')
            else:
                print("Enter a valid account") 
                print('\n')                             

        elif short_code == 'CU':
            print("New account")
            print('*'*20)

            f_name = input("First name: ")
            l_name = input("Last name : ")
            username = input("Username: ")
            password = input("Password: ")

            save_user(create_user(f_name, l_name, username, password))
            print('\n')
            print(f"New user {f_name} {l_name} created")
            print("*" *50)

            while True:
                print(f"Welcome {username}, Use the following short codes to select their corresponding values.\n SP- Save new password \n DELP - Delete password \n DISP- Display saved passwords \n LO- Log out \n")
                choice = input().upper()
                if choice == 'SP':
                    print("New account")
                    print('*' *20)

                    account = input("Account: ")
                    password = input ("Password: ")

                    save_password(create_password(account, password))
                    print('\n')

                elif choice == 'DELP':
                    account = input("Enter the name of the password you want to delete:  ") 
                    if check_existing_password(account):
                        remove_account = find_password(account)
                        del_password(remove_account) 
                        print("Password and account deleted successfully \n")
                    else:
                        print(f"{account} Does not exist \n")

                elif choice == 'DISP':
                    if display_passwords():
                        print("Here is a list of all your contacts ")
                        print('\n')

                        for acc in display_passwords():
                            print(f"Account: {acc.account} : password:{acc.password} \n")

                    else:
                            print('No password saved yet \n')
                elif choice == 'LO':
                    print('Au revoir :^) !') 
                    print('\n')
                    break   

        elif short_code == 'DU':
            if display_users():
                print("Here is a list of all your users \n ") 

                for user in display_users():
                    print(f"{user.first_name} {user.last_name}  {user.user_name} {user.password} \n ")
            else:
                print("You don't have an user saved yet \n") 

        elif short_code == 'FU':
            search_username = input("Enter the username you want to search for: ")   
            if check_existing_users(search_username):
                search_username = find_user(search_username)
                print(f"{search_username.first_name} {search_username.last_name}\n") 

            else:
                print("That user doesn't exist") 

        elif short_code == 'EX':
            print("Au revoir :^) !")
            break
        else:
            print("I really didn't get that. Please use short codes\n")

 
if __name__ == '__main__':
    main()           
