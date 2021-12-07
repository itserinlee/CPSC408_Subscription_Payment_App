import sys
import os
import names
from random import randrange, uniform
from password_generator import PasswordGenerator
from dotenv import load_dotenv
load_dotenv()

PROJ_DIR_ABS_PATH = os.getenv("PROJ_DIR_ABS_PATH")

try:
        from models.db_model import DB_Model
except ModuleNotFoundError as err:
        print("Fixing sys path..")
        sys.path.insert(0, PROJ_DIR_ABS_PATH)

from models.db_model import DB_Model
from queries.read.queries import QUERIES as RE_QUERIES
from data.data_helper import data_helper as helper

columns = [
        "cust_id","cust_first_name","cust_last_name","cust_username","cust_password","cust_record_create_date",
        "mag_id","mag_name","mag_cost","mag_record_status","mag_record_create_date",
        "prof_cust_cont_id","prof_phone","prof_zip","prof_state","prof_city","prof_street_address",
        "prof_contact_type","prof_record_update_stamp","prof_record_status","prof_start_date","prof_end_date",
        "sub_id","sub_num_mags_mailed","sub_payment_completed","sub_start_date","sub_end_date",
        "pay_id","pay_amount","pay_type","pay_date","pay_card_num","pay_card_code","pay_record_create_date",
        "category"
        ]
db = DB_Model()
def gen_rand_data():
        
        
        mag_ids = helper.get_mag_ids(db)
        cust_ids = helper.get_cust_ids(db)
        pro_ids = helper.get_pro_ids(db)
        subs_ids = helper.get_sub_ids(db)
        pay_ids = helper.get_pay_ids(db)

        # magazine fields
        mag_id = max(mag_ids) + 1
        name_cat_dict =helper.gen_rand_nandcat()
        mag_name = name_cat_dict["name"]
        mag_cat = name_cat_dict["category"]
        mag_rec_status = helper.gen_rand_status()
        mag_create_date = helper.gen_rand_date()
        print(f"******************Magazine******************\n:\
        {mag_id=}, {mag_name=}, {mag_cat=}, {mag_rec_status=}, \
        {mag_create_date=}")

        # customer fields
        cust_id = max(cust_ids) + 1
        cust_name = helper.gen_rand_name()
        cust_first_name = cust_name["first"]
        cust_last_name = cust_name["last"]
        cust_username = helper.gen_valid_username(db, cust_first_name)
        cust_password = helper.gen_rand_pw()
        cust_rec_create_date = helper.gen_rand_date()
        print(f"******************Customer******************:\
        \n{cust_id=}, {cust_first_name=}, {cust_last_name=}, \
        {cust_username=}, {cust_password=}, {cust_rec_create_date=}")

        # profile fields
        pro_id = max(pro_ids) + 1
        pro_phone = helper.gen_rand_phoneno()
        pro_addr_dict = helper.gen_rand_addr()
        pro_zip_code = pro_addr_dict["postalCode"]
        pro_state = pro_addr_dict["state"]
        pro_city = pro_addr_dict["city"]
        pro_addr = pro_addr_dict["address1"]
        pro_contact = helper.gen_rand_status()
        pro_update_date = helper.gen_rand_date()
        pro_record_status = helper.gen_rand_status()
        pro_start_date = helper.gen_rand_date()
        pro_end_date = helper.gen_rand_date()

        print(f"******************Profile******************:\
        \n{pro_id=}, {pro_phone=}, {pro_addr=}, {pro_city=},\
         {pro_state=}, {pro_zip_code=}, {pro_contact=}, {pro_update_date=}\
         {pro_record_status=}, {pro_start_date=}, {pro_end_date=}")
        
        # subscription fields
        sub_id = max(subs_ids) + 1
        sub_num_mags_mailed = randrange(0,21)
        sub_payment_completed = helper.gen_rand_status()
        sub_start_date = helper.gen_rand_date()
        sub_end_date = helper.gen_rand_enddate()
        print(f"******************Subscription******************:\
        \n{sub_id=}, {sub_num_mags_mailed=}, {sub_payment_completed=},\
        {sub_start_date=}, {sub_end_date=}")

        # pay fields
        pay_id = max(pay_ids) + 1
        pay_amount = round(uniform(9.99, 99.99), 2)
        pay_type = helper.gen_rand_status()
        pay_date = helper.gen_rand_date()
        pay_card_num = helper.gen_rand_card()
        pay_card_code = helper.gen_rand_code()
        pay_record_create_date = helper.gen_rand_date()
        print(f"******************Payment******************:\
        {pay_id=}, {pay_amount=}, {pay_type=}, {pay_date=} {pay_card_num=},\
         {pay_card_code=}, {pay_record_create_date=}\n")

        

# gen_rand_data()
# for i in range(3):
#         print(helper.gen_rand_phoneno())

for i in range(2):
       gen_rand_data()

# for i in range(30):
#         print(helper.get_rand_name())
#         print(names.get_full_name())
#         print(helper.gen_rand_nandcat())

# gen_rand_data()
db.destructor()