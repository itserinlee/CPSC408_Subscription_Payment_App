# represents an Agency table of the DB
class Customer():
        def __init__(self, cust_cont_id, cust_id, phone_num, zip_code, state, city, street_address, contact_type, start_date, end_date, rec_status, rec_create_stamp) -> None: #specified return type, this is void
                self.cust_cont_id = cust_cont_id # primary key, customer content id
                self.cust_id = cust_id # foreign key to customer that this profile belongs
                self.phone_num = phone_num
                self.zip_code = zip_code
                self.state = state 
                self.city = city 
                self.street_address = street_address 
                self.contact_type = contact_type
                self.start_date = start_date
                self.end_date = end_date
                self.rec_status = rec_status # if profile is active or expired, if they are still around or not
                self.rec_create_stamp = rec_create_stamp # date record created

        def set_id(self, cust_cont_id):
                self.cust_cont_id = cust_cont_id

        def get_fields(self):
                if self.id == None:
                        return tuple([self.cust_id, self.phone_num, self.zip_code, self.state, self.city, self.street_address, self.contact_type, self.start_date, self.end_date, self.rec_status, self.rec_create_stamp])
                return tuple([self.cust_cont_id, self.cust_id, self.phone_num, self.zip_code, self.state, self.city, self.street_address, self.contact_type, self.start_date, self.end_date, self.rec_status, self.rec_create_stamp])

        def __str__(self) -> str:
            str_ret = f"\nCustomer Profile:\nID: {str(self.cust_cont_id)}\n"
            str_ret += f"\nCustomer ID: {self.cust_id}\n"
            str_ret += f"\nPhone Number: {self.phone_num}\n"
            str_ret += f"\nStreet Address: {self.street_address}\n"
            str_ret += f"\nCity: {self.city}\n"
            str_ret += f"\nState: {self.state}\n"
            str_ret += f"\nZip Code: {self.zip_code}\n"
            str_ret += f"\nStart Date: {str(self.start_date)}\n"
            str_ret += f"\nEnd Date: {str(self.end_date)}\n"
            str_ret += f"\nAccount Active?: {self.rec_status}\n"
            str_ret += f"\nDate Record Created: {str(self.rec_create_stamp)}\n"
            
            return str_ret