from controllers.ui_helper import ui_helper
from controllers.db_helper import db_helper
from queries.read.queries import QUERIES as RE_QUERIES

# user specific methods which are all done by username
def present_options():
        msg = "Choose from the following options:\n1) View all subscriptions.\
                \n2) View magazine catalog.\n3) Add subscription (by id). \
                \n4) Delete account.\n0) Logout."
        return  db_helper.str_to_int(ui_helper.get_choice([i for i in range(0, 5)], msg=msg))

# view subscriptions
def get_subscriptions(db, username):
        db_helper.print_records(db.get_records_payload(RE_QUERIES["SUB_GET_BY_USERNAME"], (username, )), 
        ["Magazine, Cost (per month), Start Date, End Date"])

# view magazine catalog
def display_mag_catalog(db):
        db_helper.print_records(db.get_records(RE_QUERIES["MAGS_GET_CATALOG"]), 
        ["Order ID, Magazine Name, Cost, Category"])

# add subscriptions (add by magazine id)
        # pay for magazine, which enters amount payed in payment
        # and ttriggers an update to the subscription table

                # prompt user if they want to cancel transaction
# def add_subscription(db, username, mag_id):
#         db_helper.print_records(db.get_records_payload(RE_QUERIES["MAGS_GET_CATALOG"]), 
#         ["Order ID, Magazine Name, Cost, Category"])
#         return None

# delete account (does a soft delete)
def delete_account(username):
        return None
