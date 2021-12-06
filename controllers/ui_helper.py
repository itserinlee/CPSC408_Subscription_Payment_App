from controllers.db_helper import db_helper

class ui_helper():

        @staticmethod
        def get_choice(lst, msg, break_line=True):    # there is a bug in here somewhere
                lam = lambda: "\n" if break_line == True else " "
                end_loop = False
                while end_loop == False:
                        choice = input(msg + lam())
                        if choice.isdigit() == False:
                                print("Incorrect option (enter an int). Try again")
                                continue
                        if int(choice) not in lst:
                                print("Incorrect option. Try again")
                                continue
                        end_loop = True
                return db_helper.str_to_int(choice)
        
        @staticmethod
        def get_str(msg):
                user_input = input(msg)
                return user_input
