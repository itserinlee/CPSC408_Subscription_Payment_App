import mysql.connector
import os
from controllers.db_helper import db_helper
from queries.delete.queries import QUERIES as DEL_QUERIES
from queries.create.queries import QUERIES as CRE_QUERIES
# Gets the MySQL DB credentials from a .env file
from dotenv import load_dotenv
load_dotenv()

class DB_Model():
        def __init__(self): # constructor with connection path to db
                # print("in here")
                # dict containing keys with a value of a list of their respective records
                self.records = {
                        "customers": None,
                        "magazines": None,
                        "payments": None,
                        "profiles": None,
                        "subscriptions": None
                }
                try:
                        self.connection = mysql.connector.connect(
                                # the IP Address of GCP MySQL Instance
                                host=os.getenv("hostname"),
                                user=os.getenv("user"),
                                password=os.getenv("password"),
                                database=os.getenv("database"),
                                port=db_helper.str_to_int(os.getenv("port")),
                                auth_plugin='mysql_native_password'
                        )
                        self.cursor = self.connection.cursor()
                        print("Connection made.")
                        self.check_tables()
                        self.create_tables()
                except mysql.connector.Error as err:
                        print(f"Error: Unable to connect to MySQL.\nPlease re-renter the password for host: {os.getenv('hostname')} and user: root.")
        
        # if the tables exist, they will be dropped
        def check_tables(self):
                self.single_query(DEL_QUERIES["PAY_CHECK_TABLE"])
                self.single_query(DEL_QUERIES["SUB_CHECK_TABLE"])
                self.single_query(DEL_QUERIES["PRO_CHECK_TABLE"])
                self.single_query(DEL_QUERIES["CUST_CHECK_TABLE"])
                self.single_query(DEL_QUERIES["MAG_CHECK_TABLE"])

        # creates all of the tables
        def create_tables(self):
                print("Creating tables...")
                self.single_query(CRE_QUERIES["MAG_CREATE_TABLE"])
                self.single_query(CRE_QUERIES["CUST_CREATE_TABLE"])
                self.single_query(CRE_QUERIES["PRO_CREATE_TABLE"])
                self.single_query(CRE_QUERIES["SUB_CREATE_TABLE"])
                self.single_query(CRE_QUERIES["PAY_CREATE_TABLE"])
                print("Tables have been created.")

        # function to execute a single query with no payload
        def single_query(self,query):
                try:
                        self.cursor.execute(query)
                        self.connection.commit()
                except Exception as err:
                        print(f"Error: An error occurred in trying execute a single query.\n{err}")
        
        # assigns list of tuples to respective key of self.records dict
        def assign_table_recs(self, model_list, table_name):
                table_name = str(table_name)
                self.records[table_name] = db_helper.get_record_list(model_list)

        # function to execute fetch records
        def get_records(self,query):
                try:
                        self.cursor.execute(query)
                        results = self.cursor.fetchall()
                        results = [i[0] for i in results]
                        return results
                except Exception as err:
                        print(f"Error: An error occurred in trying execute a single query.\n{err}")

        # function for bulk inserting records
        def bulk_insert(self, query, records):
                try:
                        self.cursor.executemany(query,records)
                        self.connection.commit()
                        print("Query executed..")
                except Exception as err:
                        print(f"Error: An error occurred in trying bulk insert records.\n{err}")

        def print_records(self):
                record_lists = self.records.values()
                if not any(record_lists):
                        print("No records exit")
                        return
                str_p = "\n"
                for key, value in self.records.items():
                        if value != None:
                                str_p += "\n"
                                str_p += f"******************************List of {key}:******************************\n"
                                for r in value:
                                        str_p += "\n"
                                        str_p += db_helper.tuple_to_str(r)
                                str_p += "\n"
                print(str_p)

       # close connection 
        def destructor(self):
                self.connection.close()

        '''
        # order of table creation
          1) AGENCY
          2) EXPEDITION
          3) ASTRONAUT relies --> AGENCY
          4) ASTRO_EXP relies --> EXPEDITION & ASTRONAUT
        '''