from controllers.db_helper import db_helper
from controllers.ui_helper import ui_helper

exit_msg = "Enter 0 to exit, "
# show user options
def start_options(msg="1 if user, 2 if admin: "):
    msg = exit_msg + msg
    return ui_helper.get_choice([i for i in range(3)], msg)

def user_options(msg):
    return ui_helper.get_choice([i for i in range(4)])

def admin_options(msg):
    return ui_helper.get_choice([i for i in range(4)])
    
while True:
    user_choice = start_options()
    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 0:
        print("Goodbye!")
        break