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
        
        @staticmethod
        def get_phone_no():
                lst = [i for i in range(10)]
                end_loop = False
                while end_loop == False:
                        choice = input("Enter a 10 digit phone number of this format: XXX-XXX-XXXX:\n")
                        if False in [i.isdigit() == True for i in choice.replace('-', '')]:
                                print("Incorrect option (enter integers). Try again")
                                continue
                        if len(choice) != 12:
                                print("Incorrect number of digits. Try again")
                                continue
                        end_loop = True
                return choice
