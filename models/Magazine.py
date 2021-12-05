# represents an Agency table of the DB
class Customer():
        def __init__(self, mag_id, magazine_name, cost, start_date, end_date, rec_status, rec_create_stamp) -> None: #specified return type, this is void
                self.mag_id = mag_id # primary key
                self.magazine_name = magazine_name
                self.cost = cost
                self.start_date = start_date
                self.end_date = end_date
                self.rec_status = rec_status # if magazine is active or expired, if they are still around or not
                self.rec_create_stamp = rec_create_stamp # date record created

        def set_id(self, mag_id):
                self.mag_id = mag_id

        def get_fields(self):
                if self.id == None:
                        return tuple([self.magazine_name, self.cost, self.start_date, self.end_date, self.rec_status, self.rec_create_stamp])
                return tuple([self.mag_id, self.magazine_name, self.cost, self.start_date, self.end_date, self.rec_status, self.rec_create_stamp])

        def __str__(self) -> str:
            str_ret = f"\nMagazine:\nID: {str(self.mag_id)}\n"
            str_ret += f"\nName: {self.magazine_name}\n"
            str_ret += f"\nCost: {self.cost}\n"
            str_ret += f"\nStart Date: {str(self.start_date)}\n"
            str_ret += f"\nEnd Date: {str(self.end_date)}\n"
            str_ret += f"\nMagazine Active?: {self.rec_status}\n"
            str_ret += f"\nDate Record Created: {str(self.rec_create_stamp)}\n"
            
            return str_ret