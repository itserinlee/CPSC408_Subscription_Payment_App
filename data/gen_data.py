import sys
import os
import names

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
        "cust_id","cust_first_name","cust_last_name","cust_username","cust_password",
        "cust_record_create_date","mag_id","mag_name","mag_cost","mag_record_status",
        "mag_record_create_date","prof_cust_cont_id","prof_phone","prof_zip","prof_state",
        "prof_city","prof_street_address","prof_contact_type","prof_record_update_stamp",
        "prof_record_status","prof_start_date","prof_end_date","sub_id","sub_num_mags_mailed",
        "sub_payment_completed","sub_start_date","sub_end_date","pay_id","pay_amount",
        "pay_type","pay_date","pay_card_num","pay_card_code","pay_record_create_date","category"
        ]
db = DB_Model()
def gen_rand_data():
        
        
        mag_ids = helper.get_mag_ids(db)
        cust_ids = helper.get_cust_ids(db)
        pro_ids = helper.get_pro_ids(db)
        subs_ids = helper.get_sub_ids(db)
        pay_ids = helper.get_pay_ids(db)

        cust_id = cust_ids[-1] + 1
        cust_name = helper.gen_rand_name()
        cust_first_name = cust_name["first"]
        cust_last_name = cust_name["last"]
        cust_username = helper.gen_rand_pw() + "-" + cust_first_name
        cust_password = helper.gen_rand_pw()
        cust_rec_create_date = helper.gen_rand_date()

        print(f"{cust_id=}, {cust_first_name=}, {cust_last_name=}, {cust_username=}, {cust_password=}, {cust_rec_create_date=}")

        

pwo = PasswordGenerator()
pwo.minlen = 4
pwo.maxlen = 6
pwo.minschars = 0

for i in range(5):
        gen_rand_data()

# for i in range(30):
#         print(helper.get_rand_name())
#         print(names.get_full_name())
#         print(helper.gen_rand_nandcat())

# gen_rand_data()
db.destructor()