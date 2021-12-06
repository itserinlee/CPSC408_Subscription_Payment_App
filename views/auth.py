from controllers.ui_helper import ui_helper
from queries.read.queries import QUERIES as RE_QUERIES

AUTH_PW = "password"

# method for authenticating the admin user
def admin_login(pw):
        is_authenticated = False
        while is_authenticated == False:
                if pw == AUTH_PW:
                        print("Correct, password. You are authenticated.")
                        is_authenticated = True
                else:
                        pw = ui_helper.get_str("Incorrect, password. Please re-enter password:\n")
                        continue

def user_login(username, db):
        is_authenticated = False
        while is_authenticated == False:
                if pw == AUTH_PW:
                        print("Correct, password. You are authenticated.")
                        is_authenticated = True
                else:
                        pw = ui_helper.get_str("Incorrect, password. Please re-enter password:\n")
                        continue

# def username_exists(username) -> bool:

