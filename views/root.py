from controllers.db_helper import db_helper
from controllers.ui_helper import ui_helper
from views.auth import *

exit_msg = "Enter 0 to exit, "
# show user options
def start_options(msg="1 if client, 2 if admin: "):
    msg = exit_msg + msg
    return ui_helper.get_choice([i for i in range(3)], msg, False)

def user_options():
    msg = "1 to login, 2 to signup: "
    msg = exit_msg + msg
    return ui_helper.get_choice([i for i in range(3)])

def admin_options():
    msg = "1 to login: "
    msg = exit_msg + msg
    return ui_helper.get_choice([i for i in range(4)])

# while loop that executes for the duration of the program until user decides to login
def run_program(db):
    is_running = True
    exit = lambda: print("Goodbye"); False
    while is_running:
        user_choice = start_options()
        if user_choice == 1:
            msg = exit_msg
            client_choice = ui_helper.get_choice([i for i in range(3)], msg + "enter 1 to login, enter to 2 signup:")
            if client_choice == 0:
                is_running = exit()
            elif client_choice == 1:
                user_login(db)
            elif client_choice == 2:
                user_signup(db)
        elif user_choice == 2:
            admin_login()
        elif user_choice == 0:
            # user_login(ui_helper.get_str("Please enter your username:\n"), db)
            is_running = exit()