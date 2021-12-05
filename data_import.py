# data_import.py
# Connor Lydon


from mysql_interface import mysql_interface
from helper import helper

import mysql.connector


func_obj = mysql_interface()


func_obj.run_sql_script("sql/assignment07_queries.sql", show_out=False) 
    # recreate db tables, can turn to True to see each line after it has ran

read_data = helper.data_cleaner("data/expeditionData.csv")
raw_rows = read_data[1:] # excluding first element which is the column names

data = []
for row in raw_rows:
    data.append(list(row))
    
# take raw 2d array to form individual tables, 
# first bool is for autoincriment compatability
# second bool is for only getting uniqe data
agency = helper.list_to_table(data, [6,7], True, get_uniques=True) 
    # agency, agencyOrigin
    
astronaut = helper.list_to_table(data, [1,2,6], True, get_uniques=True) 
    # astronaut, age, agency
    
expedition = helper.list_to_table(data, [0,5], False, get_uniques=True) 
    # expedition, duration (only non autoincrimenting table)
    
astronaut_expedition = helper.list_to_table(data, [0,1], True, get_uniques=True) 
    # expedition, astronaut


# built these here because they rely on connection
def bulk_insert(data, table_name):
    counter = len(data[0]) #length of first row
    tempHolder = ("%s,"*counter)[:-1] # makes a %s for every datapoint, and takes out last ','
    query = "INSERT INTO " + str(table_name) + " VALUES("+tempHolder+")"
    func_obj.insert_all(query, data) #execute many queries with the inserted data

def get_records(atr1, atr2, table):
    query = "SELECT " + atr1 + ", " + atr2 + " FROM " + table + ";"
    result = func_obj.fetchall_records(query)
    return result

# using this to go from least constrictive to most constrictive
def match_constraints(atr1, atr2, table1_name, table2_obj):
    matched_table = []
    query_records = get_records(atr1, atr2, table1_name)
    for id, item in query_records:
        for table2_item in table2_obj:
            table2_item = list(table2_item) 
                # each of these comes out as a whole row from the original table
            for i in range(len(table2_item)):
                if table2_item[i] == item: # if table2 item matches the pulled data, 
                    table2_item[i] = id # then it is assigned add it over the original id
                    table2_item = tuple(table2_item) # so it can be sql compatible
                    matched_table.append(table2_item) # append this to the new table
                    break # break from for loop, item has been found
    return matched_table
    
# no dependencies in here
print("building expedition")
bulk_insert(expedition, "expedition")


# many tables depent on this
print("building agency")
bulk_insert(agency, "agency")


# need to make sure it properly references the agency table
    # the agency table has do constraints and it imposes constraints on astronaut
print("matching constraints for astronaut and agency")
matched_astronaut = match_constraints("agencyID", "Name", "agency", astronaut)

print("building astronaut")
bulk_insert(matched_astronaut, "astronaut")

# matching constraints for astonaut expedition
print("matching constraints for astronaut_expedition and astronaut")
matched_astro_expeditions = match_constraints("astronautID", "Name", "astronaut", astronaut_expedition)

# building this table last so it doesn't conflict with foreign key constrainsts
#   is also builds the id by itself
print("building astro_expedition") 
bulk_insert(matched_astro_expeditions, "astro_expedition")

func_obj.close_connection()