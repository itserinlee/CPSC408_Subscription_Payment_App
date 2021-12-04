from os import stat

# helper class for preparing data for db operations
class db_helper():
        
        # given a list of model instances, 
        # create list consisting of tuples of each model's fields 
        @staticmethod
        def get_record_list(models):
                rec_list = []
                for m in models:
                        rec_list.append(m.get_fields())
                return rec_list
        
        @staticmethod
        def is_duplicate(pk, models) -> bool:
                for m in models:
                        if m.id == pk:
                                return True
                return False
        
        @staticmethod
        def is_duplicate_agency(name, origin, models) -> bool:
                for m in models:
                        if m.name == name and m.origin == origin:
                                return True
                return False
        
        @staticmethod
        def get_agency_id(name, origin, models) -> bool:
                for m in models:
                        if m.name == name and m.origin == origin:
                                return m.id
                return None
        
        @staticmethod
        def is_duplicate_astronaut(name, age, agency_id, models) -> bool:
                for m in models:
                        if m.name == name and m.age == age and m.agency_id == agency_id:
                                return True
                return False
        
        @staticmethod
        def is_duplicate_astro_exped(exped_id, astro_id, models) -> bool:
                for m in models:
                        if m.expedition_id == exped_id and m.astronaut_id == astro_id:
                                return True
                return False