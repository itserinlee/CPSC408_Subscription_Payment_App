from models.parser import Parser
from models.db_model import DB_Model
from queries.create.queries import QUERIES as CRE_QUERIES
from views.root import run_program

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
    # assigning profile records
    db.assign_table_recs(parser.profiles, "profile")
    db.bulk_insert(CRE_QUERIES["PRO_INSERT_RECS"], db.records['profile'])
    # assigning subscription records
    db.assign_table_recs(parser.subscriptions, "subscription")
    db.bulk_insert(CRE_QUERIES["SUB_INSERT_RECS"], db.records['subscription'])
    # assigning payment records
    db.assign_table_recs(parser.payments, "payment")
    db.bulk_insert(CRE_QUERIES["PAY_INSERT_RECS"], db.records['payment'])

    # db.print_records()

    run_program(db)
    db.destructor()

if __name__ == "__main__":
    main()