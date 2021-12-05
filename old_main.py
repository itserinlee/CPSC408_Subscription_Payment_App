from models.parser import Parser
from queries import QUERIES
def main():
        db = DB_Model()
        parser = Parser(file_name="data/magazine.csv")
        # assigns indexes and list of agencies
        parser.pre_process()
        # insert agency before creating any other table
        db.assign_table_recs(parser.agencies, “agency”)
        db.bulk_insert(QUERIES[‘INSERT_AGENCY’], db.records[‘agency’])
        print(“The agency table has been populated.“)
        # fetch agency IDs and update parser agency list
        agency_ids = db.get_records(QUERIES[“GET_AGENCY_ID”])
        parser.assign_agency_ids(agency_ids)
        db.assign_table_recs(parser.agencies, “agency”)
        # generates lists of expeditions, astronauts, astro_expeditions
        parser.process()
        # assign expeditions
        db.assign_table_recs(parser.expeditions, “expedition”)
        db.bulk_insert(QUERIES[‘INSERT_EXPEDITION’], db.records[‘expedition’])
        print(“The expedition table has been populated.“)
        # assign astronauts
        db.assign_table_recs(parser.astronauts, “astronaut”)
        db.bulk_insert(QUERIES[‘INSERT_ASTRONAUT’], db.records[‘astronaut’])
        print(“The astronaut table has been populated.“)
        # assign astronaut_expeds
        db.assign_table_recs(parser.astro_expeds, “astro_expedition”)
        db.bulk_insert(QUERIES[‘INSERT_ASTRO_EXPED’], db.records[‘astro_expedition’])
        print(“The astro_expedition table has been populated.“)
if __name__ == “__main__“:
        main()

