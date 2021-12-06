from models.parser import Parser
from models.db_model import DB_Model
from queries.create.queries import QUERIES as CRE_QUERIES

def main():
    # connects to MySQL DB, removes tables (if exits), and creates tables
    db = DB_Model()

    parser = Parser()
    # parses table records / instances into Python lists
    parser.process_file()
    # assign the record lists to their respective MySQL tables
    # assigning magazine records
    db.assign_table_recs(parser.magazines, "magazine")
    db.bulk_insert(CRE_QUERIES['MAG_INSERT_RECS'], db.records["magazine"])
    # assigning customer records
    db.assign_table_recs(parser.customers, "customer")
    db.bulk_insert(CRE_QUERIES["CUST_INSERT_RECS"], db.records['customer'])
    
    db.assign_table_recs(parser.profiles, "profile")
    db.bulk_insert(CRE_QUERIES["PRO_INSERT_RECS"], db.records['profile'])

    db.print_records()
    db.destructor()

if __name__ == "__main__":
    main()