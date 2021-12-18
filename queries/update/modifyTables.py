# in MySQLWorkbench I had to type this:
    # UPDATE final_project.profile
    # SET contactType = 1
    # WHERE custContID = 1;

import mysql.connector
import pprint


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nosplits35!",
    database = "final_project"
)

cursor = connection.cursor()


def convert(value: str):
    '''
    converts the given string passed as a parameter to be the most restrictive data type for the execute() function
    so that when the cursor executes a query, it will try to force the types to match
    '''
    
    types = [int, float, str]   # order needs to be this way bc int is most restrictive data type conversion
    if value == '':
        return None
    for t in types:
        try:
            return t(value)
        except:
            pass


def dataCleaner(path: str):
    '''
    reads in a CSV files & type converts to a list of tuples
    returns a variable called dataCleaned of a list type
    '''

    with open(path, 'r', encoding = 'utf-8') as f:
        data = f.readlines()

    data = [line.strip().split(',') for line in data]
    dataCleaned = []

    for row in data[:]:
        row = [convert(element) for element in row]
        dataCleaned.append(tuple(row))
    
    return dataCleaned


def modifyContactType(userInput: int, userID: int, staging: list):  # fulfills UPDATE requirement of project
    '''
    takes in a boolean value: 1 for text and 0 for call
    this function is to update a preference about the way customer is notified about subscription
    '''

    query = ''
    # profileData = list(set([(row[7], row[0]) for row in staging]))    # not needed

    if userInput == 1:
        query = "UPDATE profile SET contactType = " + str(userInput) + " WHERE custContID = " + str(userID) + ";"
    
    elif userInput == 0:
        query = "UPDATE profile SET contactType = " + str(userInput) + " WHERE custContID = " + str(userID) + ";"
        # query = "UPDATE profile SET contactType = ? WHERE custContID = ?"
        # query = "UPDATE profile SET contactType = userInput WHERE custContID = userID"

    cursor.execute(query)
    connection.commit()

    print(f'{cursor.rowcount} record(s) updated')
    print(f'Process completed.')


def loadStagingCSV(path: str):
    '''
    reads in & parses Profile.CSV using dataCleaner() function
    loading this CSV into a list to be passed throughout program is used in lieu of inserting data via staging table
    '''

    staging = dataCleaner(path)
    staging = staging[1:]                                                  # this throws away the headers of the CSV

    return staging


# set up
receiveStaging = loadStagingCSV('../../data/Profile.csv')

# gets input
print(f'How do you want to receive notifications about your subscription?')
userInput = input('Enter 1 for text or 0 for call: ')
userID = input('Enter your ID to update your preferences: ')
# invoke function
modifyContactType(int(userInput), int(userID), receiveStaging)