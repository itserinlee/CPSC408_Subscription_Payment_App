from controllers.ui_helper import ui_helper
from controllers.db_helper import db_helper
from queries.read.queries import QUERIES as RE_QUERIES

def stat_options():
        msg = "Choose from the following options:\n1) View all magazines.\
                \n2) View all customers.\n3) View average costs of magazines by category. \
                \n4) View magazines by year.\n5) View customers' info by city. \
                \n6) View all account information of customers.\
                \n7) View all magazine information."
        return db_helper.str_to_int(ui_helper.get_choice([i for i in range(1, 8)], msg=msg))

def handle_stat_options(choice, db):
        if choice == 1:
                print_all_magazines(db)
        elif choice == 2:
                print_all_customers(db)
        elif choice == 3:
                print_mags_avg_cost_cat(db)
        elif choice == 4:
                print_magazines_by_year(db)
        elif choice == 5:
                print_customers_by_city(db)
        elif choice == 6:
                view_all_custpro(db)
        elif choice == 7:
                view_all_magsub(db)

def print_all_customers(db):
        db_helper.print_records(db.get_records(RE_QUERIES["CUST_GET_ALL"]), ["First Name, Last Name, Username"])

def print_all_magazines(db):
        db_helper.print_records(db.get_records(RE_QUERIES["MAGS_GET_ALL"]), ["Magazine Name"])

def print_mags_avg_cost_cat(db):
        db_helper.print_records(db.get_records(RE_QUERIES["MAGS_AVG_COST_BY_CAT"]), ["Category, Count of Category, Average Cost"])

def print_magazines_by_year(db):
        dist_years = db.get_records(RE_QUERIES["MAGS_GET_DIST_YEARS"])
        pars_dist_years = [i[0] for i in dist_years]
        pars_dist_years = sorted(pars_dist_years, reverse=True)
        year_input = ui_helper.get_valid_year(pars_dist_years)
        year_input = str(year_input) + "-%"
        db_helper.print_records(db.get_records_payload(RE_QUERIES["MAGS_COUNT_BY_YEAR"], (year_input, )), [f"Number of Magazines (Year - {year_input})"])

def print_customers_by_city(db):
        dist_cities = db.get_records(RE_QUERIES["GET_DIST_CITIES"])
        pars_dist_cities = [i[0] for i in dist_cities]
        pars_dist_cities = sorted(pars_dist_cities)
        city_input = ui_helper.get_valid_city(pars_dist_cities)
        db.cursor.callproc("CustByCity", (city_input, ))
        temp_results = db.cursor.stored_results()
        results = []
        for r in temp_results:
                results = [e for e in r.fetchall()]
        db_helper.print_records(results, ["customer_id full_name username date_joined"])

def view_all_custpro(db):
        db_helper.print_records(db.get_records(RE_QUERIES["GET_ALL_CUSTPRO"]),
         ["customer_id profile_id full_name username password phone_no zip_code state city street_addr contact_type date_acc_updated active date_acc_created date_acc_deleted"])

def view_all_magsub(db):
        db_helper.print_records(db.get_records(RE_QUERIES["GET_ALL_MAGSUB"]),
         ["mag_id mag_name mag_cost mag_category cust_id num_mags_received sub_id start_date end_date"])

