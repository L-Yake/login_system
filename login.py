from os import sys


# Login using USERNAME/PASSWORD
def login():
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    with open('pass.txt', 'r') as reg_check:
        data = reg_check.read()
        if username in data:
            if password in data:
                print(f'Welcome back {username}')
                sys.exit()


# Register using USERNAME/PASSWORD
def register():
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    with open('pass.txt', mode='a') as pass_keeper:
        # Write information to password file
        pass_keeper.write(username)
        pass_keeper.write(password)
    print('Thank you for registering!')
    sys.exit()


def main():
    # Main_loop()
    log_reg = input('Hello there, would you like to [L]ogin or [R]egister today?\n')

    # Validate user login against pass.txt
    if str.lower(log_reg) == 'l':
        login()

    # Create pass.txt and populate with user input
    elif str.lower(log_reg) == 'r':
        register()

    # Create User Registry if not present
    else:
        error_response = input('It would appear there is no User Registry. Would you like to create one now? (Y/N)\n')
        if str.lower(error_response) == 'y':
            with open('pass.txt', 'w') as pass_keeper:
                pass_keeper.write('File started today!')
                print('Registry complete!')
                sys.exit()

    return main()


main()
