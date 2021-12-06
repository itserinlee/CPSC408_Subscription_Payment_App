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
    
def exit(is_running) -> None:
    print("Goodbye!")
    is_running = False

def run_program(db):
    is_running = True
    while is_running:
        user_choice = start_options()
        if user_choice == 1:
            msg = exit_msg
            client_choice = ui_helper.get_choice([i for i in range(3)], msg + "enter 1 to login, enter to 2 signup:")
            if client_choice == 0:
                exit(is_running)
            elif client_choice == 1:
                user_login(db)
            elif client_choice == 2:
                user_signup(db)
        elif user_choice == 2:
            admin_login()
        elif user_choice == 0:
            # user_login(ui_helper.get_str("Please enter your username:\n"), db)
            exit(is_running)