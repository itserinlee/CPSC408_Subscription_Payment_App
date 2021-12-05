# import Python classes that represent the MySQL Tables
from models.record_types.Customer import Customer
from models.record_types.Magazine import Magazine
from models.record_types.Payment import Payment
from models.record_types.Profile import Profile
from models.record_types.Subscription import Subscription
# import helper
from controllers.db_helper import db_helper

# Python class for parsing the csv data into Python data structures
class Parser():
        def __init__(self, file_name="data/Flat.csv"):
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

                # lists that store the instances of the tables
                self.customers = []
                self.magazines = []
                self.payments = []
                self.profiles = []
                self.subscriptions = []

        # assigns column/attribute indexes from the csv file
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
                                self.process_curr_list(curr_line_list)
        
        def process_curr_list(self, curr_line_list):
                # declare curr attr vars
                cur_customer = None
                cur_magazine = None
                cur_profile = None
                cur_subscription = None
                cur_payment = None
                        
                # ***** Create Model Instances *****
                cur_customer = Customer(curr_line_list[0], curr_line_list[1], curr_line_list[2], curr_line_list[3],curr_line_list[4],curr_line_list[5])
                
                cur_magazine = Magazine(curr_line_list[6],curr_line_list[7],curr_line_list[8],curr_line_list[9],curr_line_list[10])
                
                cur_profile = Profile(curr_line_list[11], curr_line_list[0], curr_line_list[12], curr_line_list[13], curr_line_list[14], curr_line_list[15], curr_line_list[16], curr_line_list[17], curr_line_list[20], curr_line_list[21], curr_line_list[19], curr_line_list[18])
                
                cur_subscription = Subscription(curr_line_list[22], curr_line_list[6], curr_line_list[0], curr_line_list[23], curr_line_list[24], curr_line_list[25], curr_line_list[26])
                
                cur_payment = Payment(curr_line_list[27], curr_line_list[22], curr_line_list[28], curr_line_list[30], curr_line_list[29], curr_line_list[31], curr_line_list[32], curr_line_list[33])
                
                
                
                # append model instances to their respective lists
                        # these are only checked by iD
                if db_helper.is_duplicate(cur_customer.cust_id, self.customers) == False:
                        self.customers.append(cur_customer)
                        
                if db_helper.is_duplicate(cur_magazine.mag_id, self.magazines) == False:
                        self.magazines.append(cur_magazine)
                        
                if db_helper.is_duplicate(cur_profile.cust_id, self.profiles) == False:
                        self.profiles.append(cur_profile)
                        
                if db_helper.is_duplicate(cur_subscription.sub_id, self.subscriptions) == False:
                        self.subscriptions.append(cur_subscription)
                        
                if db_helper.is_duplicate(cur_payment.pay_id, self.payments) == False:
                        self.payments.append(cur_payment)
                


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
                # self.assign_indexes()
                # get and assign agency data from .csv file
                self.process_agency()

        # invokes all process methods
        def process(self):
                # get and assign data from .csv file
                self.process_file()

        def __str__(self) -> str:
            str = f"**********List of Customers:**********\n"
            customer_str = [i.__str__() for i in self.customers]
            for i in customer_str:
                    str += i
            str += f"\n**********List of Payments:**********\n"
            payment_str = [i.__str__() for i in self.payments]
            for i in payment_str:
                    str += i
            str += f"\n**********List of Profiles:**********\n"
            profile_str = [i.__str__() for i in self.profiles]
            for i in profile_str:
                    str += i
            str += f"\n**********List of Subscriptions:**********\n"
            subscription_str = [i.__str__() for i in self.subscriptions]
            for i in subscription_str:
                    str += i
            str += f"\n**********List of Magazines:**********\n"
            magazine_str = [i.__str__() for i in self.magazines]
            for i in magazine_str:
                    str += i
            return str
            