import names
import datetime
import random
import randomname
from os import stat
from password_generator import PasswordGenerator
from random_address import real_random_address
from queries.read.queries import QUERIES as RE_QUERIES
from categories import CATEGORIES

class data_helper():
        SEED=8
        pwo = PasswordGenerator()
        pwo.minlen = 4
        pwo.maxlen = 6
        pwo.minschars = 0
        random.seed(SEED)
        lst_categories = CATEGORIES

        # DB tables IDs accessor methods
        @staticmethod
        def get_mag_ids(db):
                return db.get_record_ids(RE_QUERIES["MAG_GET_IDS"])
        @staticmethod
        def get_cust_ids(db):
                return db.get_record_ids(RE_QUERIES["CUST_GET_IDS"])
        @staticmethod
        def get_pro_ids(db):
                return db.get_record_ids(RE_QUERIES["PRO_GET_IDS"])
        @staticmethod
        def get_sub_ids(db):
                return db.get_record_ids(RE_QUERIES["SUB_GET_IDS"])
        @staticmethod
        def get_pay_ids(db):
                return db.get_record_ids(RE_QUERIES["PAY_GET_IDS"])

        # helper methods for generating values for the different table attributes
        @staticmethod
        def gen_rand_pw(pwo=pwo):
                return pwo.generate()

        @staticmethod
        def gen_rand_status():
                return random.randrange(0, 1)

        @staticmethod
        def gen_rand_num(x=20, y=300):
                return random.randrange(x, y)
        
        @staticmethod
        def gen_rand_date(s_year = 2000, s_m = 1, s_d=1, e_year=2021, e_m=12, e_d=31):
                # src: https://www.kite.com/python/answers/how-to-generate-a-random-date-between-two-dates-in-python
                start_date = datetime.date(s_year, s_m, s_d)
                end_date = datetime.date(e_year, e_m, e_d)

                time_between_dates = end_date - start_date
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)
                random_date = start_date + datetime.timedelta(days=random_number_of_days)
                return random_date
        
        @staticmethod
        def gen_rand_addr():
                return real_random_address()
        # rand_add = real_random_address()
        # zip_code = rand_add['postalCode']
        # state = rand_add['state']
        # city = rand_add['city']
        # street_addr = rand_add['address1']
        # contact_type = randint(0,1)

        @staticmethod
        def gen_rand_nandcat(categories=lst_categories):
                get_rand_cat = lambda : categories[random.randrange(0, len(categories) - 1)]
                rand_cat = get_rand_cat()
                rand_name = randomname.get_name(noun=(rand_cat))
                return { "name": rand_name, "category": rand_cat } 
