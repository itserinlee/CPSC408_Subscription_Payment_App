from controllers.db_helper import db_helper
from controllers.ui_helper import ui_helper
from views.auth import *
from views.admin import *

starter_msg = "Choose from the following options (enter integer value only):\n"
exit_msg = "0) Exit\n"
# show user options
def start_options(msg="1) if you are a client user\n2) if you are a admin user"):
    msg = starter_msg + exit_msg + msg
    return ui_helper.get_choice([i for i in range(3)], msg)

# while loop that executes for the duration of the program until user decides to login
def run_program(db):
    is_running = True
    exit = lambda: print("Goodbye"); False

    while is_running:
        user_choice = start_options()
        if user_choice == 1:
            msg = starter_msg + exit_msg
            client_choice = ui_helper.get_choice([i for i in range(3)], msg + "1) Login\n2) Signup")
            if client_choice == 0:
                is_running = exit()
            elif client_choice == 1:
                user_login(db)
            elif client_choice == 2:
                user_signup(db)
                print("Redirecting you to the main menu...")
        elif user_choice == 2:
            admin_login()
            msg = starter_msg + exit_msg
            admin_choice = ui_helper.get_choice([i for i in range(3)], msg + "1) View statistics\n2) Modify records")
            if admin_choice == 0:
                is_running = exit()
            elif admin_choice == 1:
                handle_stat_options(stat_options(), db)
            elif admin_choice == 2:
                print("Redirecting you to the main menu...")
                pass
        elif user_choice == 0:
            # user_login(ui_helper.get_str("Please enter your username:\n"), db)
            is_running = exit()