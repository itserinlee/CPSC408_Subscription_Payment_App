import mysql.connector
import os
from controllers.db_helper import db_helper
from queries import QUERIES
# Gets the MySQL DB credentials from a .env file
from dotenv import load_dotenv
load_dotenv()

class DB_Model():
        def __init__(self): # constructor with connection path to db
                # print("in here")
                # dict containing keys with a value of a list of their respective records
                self.records = {
                        "agency": None,
                        "expedition": None,
                        "astronaut": None,
                        "astro_expedition": None
                }
                try:
                        self.connection = mysql.connector.connect(
                                # the IP Address of GCP MySQL Instance
                                host=os.getenv("hostname"),
                                user=os.getenv("user"),
                                password=os.getenv("password"),
                                database=os.getenv("database"),
                                port=3306
                        )
                        self.cursor = self.connection.cursor()
                        print("Connection made.")
                        self.check_tables()
                        self.create_tables()
                except mysql.connector.Error as err:
                        print(f"Error: Unable to connect to MySQL.\nPlease re-renter the password for host: {os.getenv('hostname')} and user: root.")
        
        # if the tables exist, they will be dropped
        def check_tables(self):
                self.single_query(QUERIES["CHECK_ASTRO_EXPED"])
                self.single_query(QUERIES["CHECK_ASTRONAUT"])
                self.single_query(QUERIES["CHECK_EXPEDITION"])
                self.single_query(QUERIES["CHECK_AGENCY"])

        # creates all of the tables
        def create_tables(self):
                print("Creating tables...")
                self.single_query(QUERIES["CREATE_AGENCY"])
                self.single_query(QUERIES["CREATE_EXPEDITION"])
                self.single_query(QUERIES["CREATE_ASTRONAUT"])
                self.single_query(QUERIES["CREATE_ASTRO_EXPED"])
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