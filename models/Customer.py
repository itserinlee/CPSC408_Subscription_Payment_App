# represents an Agency table of the DB
class Customer():
        def __init__(self, cust_id, first_name, last_name, username, password, rec_create_stamp) -> None:
                self.cust_id = cust_id # primary key
                self.first_name = first_name
                self.last_name = last_name
                self.username = username
                self.password = password
                self.rec_create_stamp = rec_create_stamp # date record created

        def set_id(self, cust_id):
                self.cust_id = cust_id

        def get_fields(self):
                if self.id == None:
                        return tuple([self.first_name, self.last_name, self.username, self.password, self.rec_create_stamp])
                return tuple([self.cust_id, self.first_name, self.last_name, self.username, self.password, self.rec_create_stamp])

        def __str__(self) -> str:
            str_ret = f"\nCustomer:\nID: {str(self.cust_id)}\n"
            str_ret += f"\nFirst Name: {self.first_name}\n"
            str_ret += f"\nLast Name: {self.last_name}\n"
            str_ret += f"\nUsername: {self.username}\n"
            str_ret += f"\nPassword: {self.password}\n"
            str_ret += f"\nDate Record Created: {str(self.rec_create_stamp)}\n"
            
            return str_ret