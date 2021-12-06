from controllers.ui_helper import ui_helper
from controllers.db_helper import db_helper
from queries.read.queries import QUERIES as RE_QUERIES

def stat_options():
        msg = "Choose from the following options:\n1) View average costs of magazines by category.\
                \n2) View all customers.\n3) View magazines by years."
        return db_helper.str_to_int(ui_helper.get_choice([i for i in range(1, 4)], msg=msg))

