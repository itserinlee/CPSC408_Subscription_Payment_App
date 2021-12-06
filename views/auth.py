from controllers.ui_helper import ui_helper
from queries.read.queries import QUERIES as RE_QUERIES

AUTH_PW = "password"

# method for authenticating the admin user
def admin_login():
        pw = ui_helper.get_str("Please enter admin password:\n")
        is_authenticated = False
        while is_authenticated == False:
                if pw == AUTH_PW:
                        print("Correct, password. You are authenticated.")
                        is_authenticated = True
                else:
                        pw = ui_helper.get_str("Error: Incorrect, password. Please re-enter password:\n")
                        continue

# method for user logging into the database
def user_login(db):
        username = ui_helper.get_str("Please enter your username:\n")
        is_authenticated = False
        while is_authenticated == False:
                if username_exists(username, db) == False:
                        username = ui_helper.get_str("Error: Username does not exist. Please re-enter username:\n")
                        continue
                password = ui_helper.get_str("Please enter your password:\n")
                if password != get_user_password(username, db):
                        print("Error: Incorrect password - please try again, goodbye.")
                        continue
                print(f'''Correct, password. You are authenticated.
                \nWelcome {username}!\n''')
                is_authenticated = True
                
# user login helper methods
def username_exists(username, db):
        return db.get_record(RE_QUERIES["CUST_GET_BY_USERNAME"], tuple([username, ]), "username") != None

def get_user_password(username, db):
        return db.get_record(RE_QUERIES["CUST_GET_BY_USERNAME"], tuple([username, ]), "username")[4]

# method for user to sign up for an account
def user_signup(db):
        is_created = False
        while is_created == False:
                username = ui_helper.get_str("Enter a username:\n")
                if username_exists(username, db):
                        print(f"Error: username - {username} - already exists.")
                        continue
                first_name = ui_helper.get_str("Enter your first name: ")
                last_name = ui_helper.get_str("Enter your last name: ")
                name = last_name + ", " + first_name
                password = ui_helper.get_str("Enter a password: ")
                print(f"Username - {username}, Name - {name}, Password - {password}")
                choice = ui_helper.get_choice([0,1], "Enter 1 to confirm your choices, 0 to restart:")
                if choice == 0:
                        continue
                is_created = True
                