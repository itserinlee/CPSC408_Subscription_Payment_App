from controllers.db_helper import db_helper

class ui_helper():

        @staticmethod
        def get_choice(lst, msg, break_line=True):    # there is a bug in here somewhere
                lam = lambda: "\n" if break_line == True else " "
                choice = input(msg + lam())
                # can input be made int(input()) or no bc it contains string?
                while choice.isdigit() == False:
                        print("Incorrect option. Try again")
                        choice = input("Enter choice number: ")
                while int(choice) not in lst:
                        print("Incorrect option. Try again")
                        choice = input("Enter choice number: ")
                return db_helper.str_to_int(choice)