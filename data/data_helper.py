from os import stat


from queries.read.queries import QUERIES as RE_QUERIES

class data_helper():
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
