from controllers.db_helper import db_helper
from controllers.ui_helper import ui_helper
from views.auth import *

run_program = True
exit_msg = "Enter 0 to exit, "
# show user options
def start_options(msg="1 if user, 2 if admin: "):
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
    
while run_program:
    user_choice = start_options()
    if user_choice == 1:
        pass
        # admin_login()
    elif user_choice == 2:
        pass
    elif user_choice == 0:
        print("Goodbye!")
        run_program = False