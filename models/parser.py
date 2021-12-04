# import Python classes that represent the MySQL Tables
from models.agency import Agency
from models.expedition import Expedition
from models.astronaut import Astronaut
from models.astro_expedition import AstroExpedition
from models.staging_model import StagingModel
# import helper
from controllers.db_helper import db_helper

# Python class for parsing the csv data into Python data structures
class Parser():
        def __init__(self, file_name="expeditionData.csv"):
                self.temp_file = None
                self.file_name = file_name
                # validate file name is valid
                try:
                        self.temp_file = open(self.file_name , 'r')
                        print(f"File - {self.file_name} is a valid file to read from.")
                # if error, let user know
                except OSError as err:
                        print(f"Error: could not open file - {self.file_name }.\n{err}")
                        return
                # if no error, close the file
                finally:
                        self.temp_file.close()
                self.temp_file = None
                # ***** FIELDS *****
                self.exped_i = None
                self.astro_i = None
                self.age_i = None
                self.gend_i = None
                self.nat_i = None
                self.dur_i = None
                self.agen_i = None
                self.agen_org_i = None
                self.temp_file = None

                # lists that store the instances of the tables
                self.agencies = []
                self.expeditions = []
                self.astronauts = []
                self.astro_expeds = []

        # assigns column/attribute indexes from the csv file
        def assign_indexes(self):
                with open(self.file_name, 'r') as file:
                        first_line_list = file.readline().strip().split(",")
                        # print(first_line_list)
                        for index, name in enumerate(first_line_list):
                                if name == "Expedition":
                                        self.exped_i = index
                                elif name == "Astronaut":
                                        self.astro_i = index
                                elif name == "Age":
                                        self.age_i = index
                                elif name == "Gender":
                                        self.gend_i = index
                                elif name == "Nationality":
                                        self.nat_i = index
                                elif name == "Duration":
                                        self.dur_i = index
                                elif name == "Agency":
                                        self.agen_i = index
                                elif name == "agencyOrigin":
                                        self.agen_org_i = index
                                else:
                                        pass
        # ***** METHODS *****
                # ***** METHODS *****
        def process_agency(self):
                with open(self.file_name, 'r') as file:
                        # next skips the first line
                        next(file)
                        for index, curr_agency_line in enumerate(file, start=1):
                                # list of values from csv file
                                curr_agency_line_list = curr_agency_line.strip().split(",")
                                # print(curr_agency_line_list)
                                self.process_agency_list(curr_agency_line_list)

        def process_agency_list(self, curr_line_list):
                # declare curr attr vars
                curr_agen = None
                curr_agen_org = None

                for index, val in enumerate(curr_line_list):
                        # assign curr attr values
                        if index == self.agen_i:
                                curr_agen = val
                        elif index == self.agen_org_i:
                                curr_agen_org = val
                        else:
                                pass
                        
                # ***** Create Agency Instances *****
                curr_agen_inst = Agency(None, curr_agen, curr_agen_org)

                # append model instances to their respective lists
                if db_helper.is_duplicate_agency(curr_agen_inst.name, curr_agen_inst.origin, self.agencies) == False:
                        self.agencies.append(curr_agen_inst)
        
        # given a list of agency ids, assign it to agency instance
        def assign_agency_ids(self, agency_ids):
                for index, curr_id in enumerate(agency_ids):
                        self.agencies[index].set_id(curr_id)

        # given a list of agency ids, assign it to agency instance
        def assign_astronaut_ids(self, astronaut_ids):
                for index, curr_id in enumerate(astronaut_ids):
                        self.astronauts[index].set_id(curr_id)

        def process_file(self):
                with open(self.file_name, 'r') as file:
                        # next skips the first line
                        next(file)
                        for index, curr_line in enumerate(file, start=1):
                                # list of values from csv file
                                curr_line_list = curr_line.strip().split(",")
                                # print(curr_line_list)
                                self.process_curr_list(curr_line_list, index)
        
        def process_curr_list(self, curr_line_list, curr_index):
                # declare curr attr vars
                curr_exped = None
                curr_astro = None
                curr_age = None
                curr_gend = None
                curr_nat = None
                curr_dur = None
                curr_agen = None
                curr_agen_org = None

                for index, val in enumerate(curr_line_list):
                        # assign curr attr values
                        if index == self.exped_i:
                                curr_exped = int(val)
                        elif index == self.astro_i:
                                curr_astro = val
                        elif index == self.age_i:
                                curr_age = int(val)
                        elif index == self.gend_i:
                                curr_gend = val
                        elif index == self.nat_i:
                                curr_nat = val
                        elif index == self.dur_i:
                                curr_dur = int(val)
                        elif index == self.agen_i:
                                curr_agen = val
                        elif index == self.agen_org_i:
                                curr_agen_org = val
                        else:
                                pass
                        
                # ***** Create Model Instances *****
                # instantiate expedition instance
                curr_exped_inst = Expedition(curr_exped, curr_dur)
                # instantiate astronaut instance
                curr_astro_inst = Astronaut(curr_index, curr_astro, curr_age, 
                        db_helper.get_agency_id(curr_agen, curr_agen_org, self.agencies))
                curr_astro_exped_inst = AstroExpedition(curr_index, curr_exped, curr_index)
                
                # append model instances to their respective lists
                if db_helper.is_duplicate(curr_exped_inst.id, self.expeditions) == False:
                        self.expeditions.append(curr_exped_inst)
                if db_helper.is_duplicate_astronaut(curr_astro_inst.name, curr_astro_inst.age, 
                        curr_astro_inst.agency_id, self.astronauts) == False:
                        self.astronauts.append(curr_astro_inst)
                if db_helper.is_duplicate_astro_exped(curr_astro_exped_inst.expedition_id, 
                        curr_astro_exped_inst.astronaut_id, self.astro_expeds) == False:
                        self.astro_expeds.append(curr_astro_exped_inst)

        # each AstroExpedition in the list is missing its respective Astronaut and Expedition
        def process_astr_exp(self):
                for index, curr_astro_exped in enumerate(self.astro_expeds):
                              astronaut = self.get_astro_by_id(curr_astro_exped.astronaut_id)
                              curr_astro_exped.astronaut = astronaut
                              expedition = self.get_exped_by_id(curr_astro_exped.expedition_id)
                              curr_astro_exped.expedition = expedition
                              
        # given an astro id, return astronaut
        def get_astro_by_id(self, astro_id):
                for curr_astro in self.astronauts:
                        if curr_astro.id == astro_id:
                                return curr_astro

        # given an exped id, return expedition
        def get_exped_by_id(self, exped_id):
                for curr_exped in self.expeditions:
                        if curr_exped.id == exped_id:
                                return curr_exped

        # invokes all process methods
        def pre_process(self):
                # assign col fields their respective col indexes
                self.assign_indexes()
                # get and assign agency data from .csv file
                self.process_agency()

        # invokes all process methods
        def process(self):
                # assign col fields their respective col indexes
                self.assign_indexes()
                # get and assign data from .csv file
                self.process_file()

        def __str__(self) -> str:
            str = f"**********List of Agencies:**********\n"
            agency_str = [i.__str__() for i in self.agencies]
            for i in agency_str:
                    str += i
            str += f"\n**********List of Expeditions:**********\n"
            expedition_str = [i.__str__() for i in self.expeditions]
            for i in expedition_str:
                    str += i
            str += f"\n**********List of Astronauts:**********\n"
            astronaut_str = [i.__str__() for i in self.astronauts]
            for i in astronaut_str:
                    str += i
            str += f"\n**********List of AstroExpeditions:**********\n"
            astro_exp_str = [i.__str__() for i in self.astro_expeds]
            for i in astro_exp_str:
                    str += i
            return str
            